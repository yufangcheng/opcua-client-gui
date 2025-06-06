import logging

from PyQt5.QtCore import QSettings
from asyncua import crypto
from asyncua import ua
from asyncua.sync import Client, SyncNode
from asyncua.tools import endpoint_to_strings

logger = logging.getLogger(__name__)


class UaClient(object):
    """
    OPC-Ua client specialized for the need of GUI client
    return exactly what GUI needs, no customization possible
    """

    def __init__(self):
        self.settings = QSettings()
        self.application_uri = "urn:freeopcua:client-gui"
        self.client = None
        self._connected = False
        self._datachange_sub = None
        self._event_sub = None
        self._subs_dc = {}
        self._subs_ev = {}
        self.security_mode = None
        self.security_policy = None
        self.user_certificate_path = None
        self.user_private_key_path = None
        self.application_certificate_path = None
        self.application_private_key_path = None
        self.load_application_certificate_settings()

    def _reset(self):
        self.client = None
        self._connected = False
        self._datachange_sub = None
        self._event_sub = None
        self._subs_dc = {}
        self._subs_ev = {}

    @staticmethod
    def get_endpoints(uri):
        client = Client(uri, timeout=2)
        edps = client.connect_and_get_server_endpoints()
        for i, ep in enumerate(edps, start=1):
            logger.info('Endpoint %s:', i)
            for (n, v) in endpoint_to_strings(ep):
                logger.info('  %s: %s', n, v)
            logger.info('')
        return edps

    def load_security_settings(self, uri):
        self.security_mode = None
        self.security_policy = None
        self.user_certificate_path = None
        self.user_private_key_path = None

        mysettings = self.settings.value("security_settings", None)
        if mysettings is None:
            return
        if uri in mysettings:
            mode, policy, cert, key = mysettings[uri]
            self.security_mode = mode
            self.security_policy = policy
            self.user_certificate_path = cert
            self.user_private_key_path = key

    def save_security_settings(self, uri):
        mysettings = self.settings.value("security_settings", None)
        if mysettings is None:
            mysettings = {}
        mysettings[uri] = [self.security_mode,
                           self.security_policy,
                           self.user_certificate_path,
                           self.user_private_key_path]
        self.settings.setValue("security_settings", mysettings)

    def load_application_certificate_settings(self):
        self.application_certificate_path = None
        self.application_private_key_path = None

        mysettings = self.settings.value("application_certificate_settings", None)
        if mysettings is None:
            return
        self.application_certificate_path = mysettings["application_certificate"]
        self.application_private_key_path = mysettings["application_private_key"]

    def save_application_certificate_settings(self):
        mysettings = self.settings.value("application_certificate_settings", None)
        if mysettings is None:
            mysettings = {}
        mysettings["application_certificate"] = self.application_certificate_path
        mysettings["application_private_key"] = self.application_private_key_path
        self.settings.setValue("application_certificate_settings", mysettings)

    def get_node(self, nodeid):
        return self.client.get_node(nodeid)

    def connect(self, uri):
        self.disconnect()
        logger.info("Connecting to %s with parameters %s, %s, %s, %s", uri, self.security_mode, self.security_policy,
                    self.user_certificate_path, self.user_private_key_path)
        self.client = Client(uri)
        self.client.application_uri = self.application_uri
        self.client.description = "OpcUa Client GUI"

        # Set user identity token
        if self.user_private_key_path:
            self.client.load_private_key(self.user_private_key_path)
        if self.user_certificate_path:
            self.client.load_client_certificate(self.user_certificate_path)

        # Set security mode and security policy
        if self.security_mode is not None and self.security_policy is not None:
            self.client.set_security(
                getattr(crypto.security_policies, 'SecurityPolicy' + self.security_policy),
                self.application_certificate_path,
                self.application_private_key_path,
                mode=getattr(ua.MessageSecurityMode, self.security_mode)
            )
        self.client.connect()
        self._connected = True
        self.client.load_data_type_definitions()
        try:
            self.client.load_enums()
            self.client.load_type_definitions()
        except Exception:
            logger.exception("Loading custom stuff with spec <= 1.03 did not work")
        self.save_security_settings(uri)

    def disconnect(self):
        if self._connected:
            print("Disconnecting from server")
            self._connected = False
            try:
                self.client.disconnect()
            finally:
                self._reset()

    def subscribe_datachange(self, node, handler):
        if not self._datachange_sub:
            self._datachange_sub = self.client.create_subscription(500, handler)
        handle = self._datachange_sub.subscribe_data_change(node)
        self._subs_dc[node.nodeid] = handle
        return handle

    def unsubscribe_datachange(self, node):
        self._datachange_sub.unsubscribe(self._subs_dc[node.nodeid])

    def subscribe_events(self, node, handler):
        if not self._event_sub:
            print("subscirbing with handler: ", handler, dir(handler))
            self._event_sub = self.client.create_subscription(500, handler)
        handle = self._event_sub.subscribe_events(node)
        self._subs_ev[node.nodeid] = handle
        return handle

    def unsubscribe_events(self, node):
        self._event_sub.unsubscribe(self._subs_ev[node.nodeid])

    def get_node_attrs(self, node):
        if not isinstance(node, SyncNode):
            node = self.client.get_node(node)
        attrs = node.read_attributes([ua.AttributeIds.DisplayName, ua.AttributeIds.BrowseName, ua.AttributeIds.NodeId])
        return node, [attr.Value.Value.to_string() for attr in attrs]

    @staticmethod
    def get_children(node):
        descs = node.get_children_descriptions()
        descs.sort(key=lambda x: x.BrowseName)
        return descs
