# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/api/grpc/wlan.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from core.api.grpc import common_pb2 as core_dot_api_dot_grpc_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63ore/api/grpc/wlan.proto\x12\x04wlan\x1a\x1a\x63ore/api/grpc/common.proto\"z\n\nWlanConfig\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12,\n\x06\x63onfig\x18\x02 \x03(\x0b\x32\x1c.wlan.WlanConfig.ConfigEntry\x1a-\n\x0b\x43onfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\";\n\x14GetWlanConfigRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x05\x12\x0f\n\x07node_id\x18\x02 \x01(\x05\"\x95\x01\n\x15GetWlanConfigResponse\x12\x37\n\x06\x63onfig\x18\x01 \x03(\x0b\x32\'.wlan.GetWlanConfigResponse.ConfigEntry\x1a\x43\n\x0b\x43onfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.common.ConfigOption:\x02\x38\x01\"Q\n\x14SetWlanConfigRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x05\x12%\n\x0bwlan_config\x18\x02 \x01(\x0b\x32\x10.wlan.WlanConfig\"\'\n\x15SetWlanConfigResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\"g\n\x0fWlanLinkRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x05\x12\x0c\n\x04wlan\x18\x02 \x01(\x05\x12\x10\n\x08node1_id\x18\x03 \x01(\x05\x12\x10\n\x08node2_id\x18\x04 \x01(\x05\x12\x0e\n\x06linked\x18\x05 \x01(\x08\"\"\n\x10WlanLinkResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x62\x06proto3')



_WLANCONFIG = DESCRIPTOR.message_types_by_name['WlanConfig']
_WLANCONFIG_CONFIGENTRY = _WLANCONFIG.nested_types_by_name['ConfigEntry']
_GETWLANCONFIGREQUEST = DESCRIPTOR.message_types_by_name['GetWlanConfigRequest']
_GETWLANCONFIGRESPONSE = DESCRIPTOR.message_types_by_name['GetWlanConfigResponse']
_GETWLANCONFIGRESPONSE_CONFIGENTRY = _GETWLANCONFIGRESPONSE.nested_types_by_name['ConfigEntry']
_SETWLANCONFIGREQUEST = DESCRIPTOR.message_types_by_name['SetWlanConfigRequest']
_SETWLANCONFIGRESPONSE = DESCRIPTOR.message_types_by_name['SetWlanConfigResponse']
_WLANLINKREQUEST = DESCRIPTOR.message_types_by_name['WlanLinkRequest']
_WLANLINKRESPONSE = DESCRIPTOR.message_types_by_name['WlanLinkResponse']
WlanConfig = _reflection.GeneratedProtocolMessageType('WlanConfig', (_message.Message,), {

  'ConfigEntry' : _reflection.GeneratedProtocolMessageType('ConfigEntry', (_message.Message,), {
    'DESCRIPTOR' : _WLANCONFIG_CONFIGENTRY,
    '__module__' : 'core.api.grpc.wlan_pb2'
    # @@protoc_insertion_point(class_scope:wlan.WlanConfig.ConfigEntry)
    })
  ,
  'DESCRIPTOR' : _WLANCONFIG,
  '__module__' : 'core.api.grpc.wlan_pb2'
  # @@protoc_insertion_point(class_scope:wlan.WlanConfig)
  })
_sym_db.RegisterMessage(WlanConfig)
_sym_db.RegisterMessage(WlanConfig.ConfigEntry)

GetWlanConfigRequest = _reflection.GeneratedProtocolMessageType('GetWlanConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETWLANCONFIGREQUEST,
  '__module__' : 'core.api.grpc.wlan_pb2'
  # @@protoc_insertion_point(class_scope:wlan.GetWlanConfigRequest)
  })
_sym_db.RegisterMessage(GetWlanConfigRequest)

GetWlanConfigResponse = _reflection.GeneratedProtocolMessageType('GetWlanConfigResponse', (_message.Message,), {

  'ConfigEntry' : _reflection.GeneratedProtocolMessageType('ConfigEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETWLANCONFIGRESPONSE_CONFIGENTRY,
    '__module__' : 'core.api.grpc.wlan_pb2'
    # @@protoc_insertion_point(class_scope:wlan.GetWlanConfigResponse.ConfigEntry)
    })
  ,
  'DESCRIPTOR' : _GETWLANCONFIGRESPONSE,
  '__module__' : 'core.api.grpc.wlan_pb2'
  # @@protoc_insertion_point(class_scope:wlan.GetWlanConfigResponse)
  })
_sym_db.RegisterMessage(GetWlanConfigResponse)
_sym_db.RegisterMessage(GetWlanConfigResponse.ConfigEntry)

SetWlanConfigRequest = _reflection.GeneratedProtocolMessageType('SetWlanConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETWLANCONFIGREQUEST,
  '__module__' : 'core.api.grpc.wlan_pb2'
  # @@protoc_insertion_point(class_scope:wlan.SetWlanConfigRequest)
  })
_sym_db.RegisterMessage(SetWlanConfigRequest)

SetWlanConfigResponse = _reflection.GeneratedProtocolMessageType('SetWlanConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETWLANCONFIGRESPONSE,
  '__module__' : 'core.api.grpc.wlan_pb2'
  # @@protoc_insertion_point(class_scope:wlan.SetWlanConfigResponse)
  })
_sym_db.RegisterMessage(SetWlanConfigResponse)

WlanLinkRequest = _reflection.GeneratedProtocolMessageType('WlanLinkRequest', (_message.Message,), {
  'DESCRIPTOR' : _WLANLINKREQUEST,
  '__module__' : 'core.api.grpc.wlan_pb2'
  # @@protoc_insertion_point(class_scope:wlan.WlanLinkRequest)
  })
_sym_db.RegisterMessage(WlanLinkRequest)

WlanLinkResponse = _reflection.GeneratedProtocolMessageType('WlanLinkResponse', (_message.Message,), {
  'DESCRIPTOR' : _WLANLINKRESPONSE,
  '__module__' : 'core.api.grpc.wlan_pb2'
  # @@protoc_insertion_point(class_scope:wlan.WlanLinkResponse)
  })
_sym_db.RegisterMessage(WlanLinkResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WLANCONFIG_CONFIGENTRY._options = None
  _WLANCONFIG_CONFIGENTRY._serialized_options = b'8\001'
  _GETWLANCONFIGRESPONSE_CONFIGENTRY._options = None
  _GETWLANCONFIGRESPONSE_CONFIGENTRY._serialized_options = b'8\001'
  _WLANCONFIG._serialized_start=62
  _WLANCONFIG._serialized_end=184
  _WLANCONFIG_CONFIGENTRY._serialized_start=139
  _WLANCONFIG_CONFIGENTRY._serialized_end=184
  _GETWLANCONFIGREQUEST._serialized_start=186
  _GETWLANCONFIGREQUEST._serialized_end=245
  _GETWLANCONFIGRESPONSE._serialized_start=248
  _GETWLANCONFIGRESPONSE._serialized_end=397
  _GETWLANCONFIGRESPONSE_CONFIGENTRY._serialized_start=330
  _GETWLANCONFIGRESPONSE_CONFIGENTRY._serialized_end=397
  _SETWLANCONFIGREQUEST._serialized_start=399
  _SETWLANCONFIGREQUEST._serialized_end=480
  _SETWLANCONFIGRESPONSE._serialized_start=482
  _SETWLANCONFIGRESPONSE._serialized_end=521
  _WLANLINKREQUEST._serialized_start=523
  _WLANLINKREQUEST._serialized_end=626
  _WLANLINKRESPONSE._serialized_start=628
  _WLANLINKRESPONSE._serialized_end=662
# @@protoc_insertion_point(module_scope)
