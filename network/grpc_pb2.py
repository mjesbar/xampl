# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: grpc.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'grpc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngrpc.proto\"!\n\x0e\x43lientResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"!\n\x0eServerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x8f\x02\n\x0bMessageEcho\x12\x30\n\nServerEcho\x12\x0f.ClientResponse\x1a\x0f.ServerResponse\"\x00\x12\x38\n\x10ServerEchoStream\x12\x0f.ClientResponse\x1a\x0f.ServerResponse\"\x00\x30\x01\x12\x42\n\x1aServerEchoFromClientStream\x12\x0f.ClientResponse\x1a\x0f.ServerResponse\"\x00(\x01\x12P\n&ServerEchoStreamFromStreamClientStream\x12\x0f.ClientResponse\x1a\x0f.ServerResponse\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CLIENTRESPONSE']._serialized_start=14
  _globals['_CLIENTRESPONSE']._serialized_end=47
  _globals['_SERVERRESPONSE']._serialized_start=49
  _globals['_SERVERRESPONSE']._serialized_end=82
  _globals['_MESSAGEECHO']._serialized_start=85
  _globals['_MESSAGEECHO']._serialized_end=356
# @@protoc_insertion_point(module_scope)
