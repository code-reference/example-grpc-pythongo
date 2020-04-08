# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: toupper.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='toupper.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\rtoupper.proto\x12\x05proto\"\x1c\n\x0cUpperRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nUpperReply\x12\x0f\n\x07message\x18\x01 \x01(\t2<\n\x07ToUpper\x12\x31\n\x05Upper\x12\x13.proto.UpperRequest\x1a\x11.proto.UpperReply\"\x00\x62\x06proto3'
)




_UPPERREQUEST = _descriptor.Descriptor(
  name='UpperRequest',
  full_name='proto.UpperRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.UpperRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=52,
)


_UPPERREPLY = _descriptor.Descriptor(
  name='UpperReply',
  full_name='proto.UpperReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='proto.UpperReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=83,
)

DESCRIPTOR.message_types_by_name['UpperRequest'] = _UPPERREQUEST
DESCRIPTOR.message_types_by_name['UpperReply'] = _UPPERREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpperRequest = _reflection.GeneratedProtocolMessageType('UpperRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPPERREQUEST,
  '__module__' : 'toupper_pb2'
  # @@protoc_insertion_point(class_scope:proto.UpperRequest)
  })
_sym_db.RegisterMessage(UpperRequest)

UpperReply = _reflection.GeneratedProtocolMessageType('UpperReply', (_message.Message,), {
  'DESCRIPTOR' : _UPPERREPLY,
  '__module__' : 'toupper_pb2'
  # @@protoc_insertion_point(class_scope:proto.UpperReply)
  })
_sym_db.RegisterMessage(UpperReply)



_TOUPPER = _descriptor.ServiceDescriptor(
  name='ToUpper',
  full_name='proto.ToUpper',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=85,
  serialized_end=145,
  methods=[
  _descriptor.MethodDescriptor(
    name='Upper',
    full_name='proto.ToUpper.Upper',
    index=0,
    containing_service=None,
    input_type=_UPPERREQUEST,
    output_type=_UPPERREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TOUPPER)

DESCRIPTOR.services_by_name['ToUpper'] = _TOUPPER

# @@protoc_insertion_point(module_scope)