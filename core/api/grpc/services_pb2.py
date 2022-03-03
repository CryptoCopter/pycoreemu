# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/api/grpc/services.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63ore/api/grpc/services.proto\x12\x08services\"\x8a\x01\n\rServiceConfig\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x0f\n\x07startup\x18\x03 \x03(\t\x12\x10\n\x08validate\x18\x04 \x03(\t\x12\x10\n\x08shutdown\x18\x05 \x03(\t\x12\r\n\x05\x66iles\x18\x06 \x03(\t\x12\x13\n\x0b\x64irectories\x18\x07 \x03(\t\"Q\n\x11ServiceFileConfig\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x0c\n\x04\x66ile\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\"J\n\x15ServiceValidationMode\"1\n\x04\x45num\x12\x0c\n\x08\x42LOCKING\x10\x00\x12\x10\n\x0cNON_BLOCKING\x10\x01\x12\t\n\x05TIMER\x10\x02\"G\n\rServiceAction\"6\n\x04\x45num\x12\t\n\x05START\x10\x00\x12\x08\n\x04STOP\x10\x01\x12\x0b\n\x07RESTART\x10\x02\x12\x0c\n\x08VALIDATE\x10\x03\"6\n\x0fServiceDefaults\x12\x11\n\tnode_type\x18\x01 \x01(\t\x12\x10\n\x08services\x18\x02 \x03(\t\"&\n\x07Service\x12\r\n\x05group\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xf7\x01\n\x0fNodeServiceData\x12\x13\n\x0b\x65xecutables\x18\x01 \x03(\t\x12\x14\n\x0c\x64\x65pendencies\x18\x02 \x03(\t\x12\x0c\n\x04\x64irs\x18\x03 \x03(\t\x12\x0f\n\x07\x63onfigs\x18\x04 \x03(\t\x12\x0f\n\x07startup\x18\x05 \x03(\t\x12\x10\n\x08validate\x18\x06 \x03(\t\x12=\n\x0fvalidation_mode\x18\x07 \x01(\x0e\x32$.services.ServiceValidationMode.Enum\x12\x18\n\x10validation_timer\x18\x08 \x01(\x05\x12\x10\n\x08shutdown\x18\t \x03(\t\x12\x0c\n\x04meta\x18\n \x01(\t\"\xc3\x01\n\x11NodeServiceConfig\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\'\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x19.services.NodeServiceData\x12\x35\n\x05\x66iles\x18\x04 \x03(\x0b\x32&.services.NodeServiceConfig.FilesEntry\x1a,\n\nFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"/\n\x19GetServiceDefaultsRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x05\"I\n\x1aGetServiceDefaultsResponse\x12+\n\x08\x64\x65\x66\x61ults\x18\x01 \x03(\x0b\x32\x19.services.ServiceDefaults\"\\\n\x19SetServiceDefaultsRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x05\x12+\n\x08\x64\x65\x66\x61ults\x18\x02 \x03(\x0b\x32\x19.services.ServiceDefaults\",\n\x1aSetServiceDefaultsResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\"M\n\x15GetNodeServiceRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x05\x12\x0f\n\x07node_id\x18\x02 \x01(\x05\x12\x0f\n\x07service\x18\x03 \x01(\t\"D\n\x16GetNodeServiceResponse\x12*\n\x07service\x18\x01 \x01(\x0b\x32\x19.services.NodeServiceData\"_\n\x19GetNodeServiceFileRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x05\x12\x0f\n\x07node_id\x18\x02 \x01(\x05\x12\x0f\n\x07service\x18\x03 \x01(\t\x12\x0c\n\x04\x66ile\x18\x04 \x01(\t\"*\n\x1aGetNodeServiceFileResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"z\n\x14ServiceActionRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x05\x12\x0f\n\x07node_id\x18\x02 \x01(\x05\x12\x0f\n\x07service\x18\x03 \x01(\t\x12,\n\x06\x61\x63tion\x18\x04 \x01(\x0e\x32\x1c.services.ServiceAction.Enum\"\'\n\x15ServiceActionResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x62\x06proto3')



_SERVICECONFIG = DESCRIPTOR.message_types_by_name['ServiceConfig']
_SERVICEFILECONFIG = DESCRIPTOR.message_types_by_name['ServiceFileConfig']
_SERVICEVALIDATIONMODE = DESCRIPTOR.message_types_by_name['ServiceValidationMode']
_SERVICEACTION = DESCRIPTOR.message_types_by_name['ServiceAction']
_SERVICEDEFAULTS = DESCRIPTOR.message_types_by_name['ServiceDefaults']
_SERVICE = DESCRIPTOR.message_types_by_name['Service']
_NODESERVICEDATA = DESCRIPTOR.message_types_by_name['NodeServiceData']
_NODESERVICECONFIG = DESCRIPTOR.message_types_by_name['NodeServiceConfig']
_NODESERVICECONFIG_FILESENTRY = _NODESERVICECONFIG.nested_types_by_name['FilesEntry']
_GETSERVICEDEFAULTSREQUEST = DESCRIPTOR.message_types_by_name['GetServiceDefaultsRequest']
_GETSERVICEDEFAULTSRESPONSE = DESCRIPTOR.message_types_by_name['GetServiceDefaultsResponse']
_SETSERVICEDEFAULTSREQUEST = DESCRIPTOR.message_types_by_name['SetServiceDefaultsRequest']
_SETSERVICEDEFAULTSRESPONSE = DESCRIPTOR.message_types_by_name['SetServiceDefaultsResponse']
_GETNODESERVICEREQUEST = DESCRIPTOR.message_types_by_name['GetNodeServiceRequest']
_GETNODESERVICERESPONSE = DESCRIPTOR.message_types_by_name['GetNodeServiceResponse']
_GETNODESERVICEFILEREQUEST = DESCRIPTOR.message_types_by_name['GetNodeServiceFileRequest']
_GETNODESERVICEFILERESPONSE = DESCRIPTOR.message_types_by_name['GetNodeServiceFileResponse']
_SERVICEACTIONREQUEST = DESCRIPTOR.message_types_by_name['ServiceActionRequest']
_SERVICEACTIONRESPONSE = DESCRIPTOR.message_types_by_name['ServiceActionResponse']
_SERVICEVALIDATIONMODE_ENUM = _SERVICEVALIDATIONMODE.enum_types_by_name['Enum']
_SERVICEACTION_ENUM = _SERVICEACTION.enum_types_by_name['Enum']
ServiceConfig = _reflection.GeneratedProtocolMessageType('ServiceConfig', (_message.Message,), {
  'DESCRIPTOR' : _SERVICECONFIG,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.ServiceConfig)
  })
_sym_db.RegisterMessage(ServiceConfig)

ServiceFileConfig = _reflection.GeneratedProtocolMessageType('ServiceFileConfig', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEFILECONFIG,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.ServiceFileConfig)
  })
_sym_db.RegisterMessage(ServiceFileConfig)

ServiceValidationMode = _reflection.GeneratedProtocolMessageType('ServiceValidationMode', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEVALIDATIONMODE,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.ServiceValidationMode)
  })
_sym_db.RegisterMessage(ServiceValidationMode)

ServiceAction = _reflection.GeneratedProtocolMessageType('ServiceAction', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEACTION,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.ServiceAction)
  })
_sym_db.RegisterMessage(ServiceAction)

ServiceDefaults = _reflection.GeneratedProtocolMessageType('ServiceDefaults', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEDEFAULTS,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.ServiceDefaults)
  })
_sym_db.RegisterMessage(ServiceDefaults)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), {
  'DESCRIPTOR' : _SERVICE,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.Service)
  })
_sym_db.RegisterMessage(Service)

NodeServiceData = _reflection.GeneratedProtocolMessageType('NodeServiceData', (_message.Message,), {
  'DESCRIPTOR' : _NODESERVICEDATA,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.NodeServiceData)
  })
_sym_db.RegisterMessage(NodeServiceData)

NodeServiceConfig = _reflection.GeneratedProtocolMessageType('NodeServiceConfig', (_message.Message,), {

  'FilesEntry' : _reflection.GeneratedProtocolMessageType('FilesEntry', (_message.Message,), {
    'DESCRIPTOR' : _NODESERVICECONFIG_FILESENTRY,
    '__module__' : 'core.api.grpc.services_pb2'
    # @@protoc_insertion_point(class_scope:services.NodeServiceConfig.FilesEntry)
    })
  ,
  'DESCRIPTOR' : _NODESERVICECONFIG,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.NodeServiceConfig)
  })
_sym_db.RegisterMessage(NodeServiceConfig)
_sym_db.RegisterMessage(NodeServiceConfig.FilesEntry)

GetServiceDefaultsRequest = _reflection.GeneratedProtocolMessageType('GetServiceDefaultsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVICEDEFAULTSREQUEST,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.GetServiceDefaultsRequest)
  })
_sym_db.RegisterMessage(GetServiceDefaultsRequest)

GetServiceDefaultsResponse = _reflection.GeneratedProtocolMessageType('GetServiceDefaultsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVICEDEFAULTSRESPONSE,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.GetServiceDefaultsResponse)
  })
_sym_db.RegisterMessage(GetServiceDefaultsResponse)

SetServiceDefaultsRequest = _reflection.GeneratedProtocolMessageType('SetServiceDefaultsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETSERVICEDEFAULTSREQUEST,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.SetServiceDefaultsRequest)
  })
_sym_db.RegisterMessage(SetServiceDefaultsRequest)

SetServiceDefaultsResponse = _reflection.GeneratedProtocolMessageType('SetServiceDefaultsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETSERVICEDEFAULTSRESPONSE,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.SetServiceDefaultsResponse)
  })
_sym_db.RegisterMessage(SetServiceDefaultsResponse)

GetNodeServiceRequest = _reflection.GeneratedProtocolMessageType('GetNodeServiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETNODESERVICEREQUEST,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.GetNodeServiceRequest)
  })
_sym_db.RegisterMessage(GetNodeServiceRequest)

GetNodeServiceResponse = _reflection.GeneratedProtocolMessageType('GetNodeServiceResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETNODESERVICERESPONSE,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.GetNodeServiceResponse)
  })
_sym_db.RegisterMessage(GetNodeServiceResponse)

GetNodeServiceFileRequest = _reflection.GeneratedProtocolMessageType('GetNodeServiceFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETNODESERVICEFILEREQUEST,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.GetNodeServiceFileRequest)
  })
_sym_db.RegisterMessage(GetNodeServiceFileRequest)

GetNodeServiceFileResponse = _reflection.GeneratedProtocolMessageType('GetNodeServiceFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETNODESERVICEFILERESPONSE,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.GetNodeServiceFileResponse)
  })
_sym_db.RegisterMessage(GetNodeServiceFileResponse)

ServiceActionRequest = _reflection.GeneratedProtocolMessageType('ServiceActionRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEACTIONREQUEST,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.ServiceActionRequest)
  })
_sym_db.RegisterMessage(ServiceActionRequest)

ServiceActionResponse = _reflection.GeneratedProtocolMessageType('ServiceActionResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEACTIONRESPONSE,
  '__module__' : 'core.api.grpc.services_pb2'
  # @@protoc_insertion_point(class_scope:services.ServiceActionResponse)
  })
_sym_db.RegisterMessage(ServiceActionResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NODESERVICECONFIG_FILESENTRY._options = None
  _NODESERVICECONFIG_FILESENTRY._serialized_options = b'8\001'
  _SERVICECONFIG._serialized_start=43
  _SERVICECONFIG._serialized_end=181
  _SERVICEFILECONFIG._serialized_start=183
  _SERVICEFILECONFIG._serialized_end=264
  _SERVICEVALIDATIONMODE._serialized_start=266
  _SERVICEVALIDATIONMODE._serialized_end=340
  _SERVICEVALIDATIONMODE_ENUM._serialized_start=291
  _SERVICEVALIDATIONMODE_ENUM._serialized_end=340
  _SERVICEACTION._serialized_start=342
  _SERVICEACTION._serialized_end=413
  _SERVICEACTION_ENUM._serialized_start=359
  _SERVICEACTION_ENUM._serialized_end=413
  _SERVICEDEFAULTS._serialized_start=415
  _SERVICEDEFAULTS._serialized_end=469
  _SERVICE._serialized_start=471
  _SERVICE._serialized_end=509
  _NODESERVICEDATA._serialized_start=512
  _NODESERVICEDATA._serialized_end=759
  _NODESERVICECONFIG._serialized_start=762
  _NODESERVICECONFIG._serialized_end=957
  _NODESERVICECONFIG_FILESENTRY._serialized_start=913
  _NODESERVICECONFIG_FILESENTRY._serialized_end=957
  _GETSERVICEDEFAULTSREQUEST._serialized_start=959
  _GETSERVICEDEFAULTSREQUEST._serialized_end=1006
  _GETSERVICEDEFAULTSRESPONSE._serialized_start=1008
  _GETSERVICEDEFAULTSRESPONSE._serialized_end=1081
  _SETSERVICEDEFAULTSREQUEST._serialized_start=1083
  _SETSERVICEDEFAULTSREQUEST._serialized_end=1175
  _SETSERVICEDEFAULTSRESPONSE._serialized_start=1177
  _SETSERVICEDEFAULTSRESPONSE._serialized_end=1221
  _GETNODESERVICEREQUEST._serialized_start=1223
  _GETNODESERVICEREQUEST._serialized_end=1300
  _GETNODESERVICERESPONSE._serialized_start=1302
  _GETNODESERVICERESPONSE._serialized_end=1370
  _GETNODESERVICEFILEREQUEST._serialized_start=1372
  _GETNODESERVICEFILEREQUEST._serialized_end=1467
  _GETNODESERVICEFILERESPONSE._serialized_start=1469
  _GETNODESERVICEFILERESPONSE._serialized_end=1511
  _SERVICEACTIONREQUEST._serialized_start=1513
  _SERVICEACTIONREQUEST._serialized_end=1635
  _SERVICEACTIONRESPONSE._serialized_start=1637
  _SERVICEACTIONRESPONSE._serialized_end=1676
# @@protoc_insertion_point(module_scope)
