# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: advantech_afs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='advantech_afs.proto',
  package='tutorial',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x13\x61\x64vantech_afs.proto\x12\x08tutorial\">\n\nDataFromDF\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\t\x12\x13\n\x0b\x63olumnsName\x18\x02 \x03(\t\x12\r\n\x05\x64type\x18\x03 \x02(\t\"\x82\x01\n\x0cS3Credential\x12\x11\n\taccessKey\x18\x01 \x02(\t\x12\x17\n\x0fsecretAccessKey\x18\x02 \x02(\t\x12\x10\n\x08\x65ndPoint\x18\x03 \x02(\t\x12\x0e\n\x06\x62ucket\x18\x04 \x02(\t\x12\x12\n\nblobPrefix\x18\x05 \x01(\t\x12\x10\n\x08\x62lobList\x18\x06 \x03(\t\"r\n\x10\x41zureBlobStorage\x12\x13\n\x0b\x61\x63\x63ountName\x18\x01 \x02(\t\x12\x12\n\naccountKey\x18\x02 \x02(\t\x12\x11\n\tcontainer\x18\x03 \x02(\t\x12\x10\n\x08\x62lobType\x18\x04 \x02(\t\x12\x10\n\x08\x62lobList\x18\x05 \x03(\t')
)




_DATAFROMDF = _descriptor.Descriptor(
  name='DataFromDF',
  full_name='tutorial.DataFromDF',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='tutorial.DataFromDF.data', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columnsName', full_name='tutorial.DataFromDF.columnsName', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='tutorial.DataFromDF.dtype', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=95,
)


_S3CREDENTIAL = _descriptor.Descriptor(
  name='S3Credential',
  full_name='tutorial.S3Credential',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accessKey', full_name='tutorial.S3Credential.accessKey', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secretAccessKey', full_name='tutorial.S3Credential.secretAccessKey', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endPoint', full_name='tutorial.S3Credential.endPoint', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='tutorial.S3Credential.bucket', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blobPrefix', full_name='tutorial.S3Credential.blobPrefix', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blobList', full_name='tutorial.S3Credential.blobList', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=228,
)


_AZUREBLOBSTORAGE = _descriptor.Descriptor(
  name='AzureBlobStorage',
  full_name='tutorial.AzureBlobStorage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accountName', full_name='tutorial.AzureBlobStorage.accountName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accountKey', full_name='tutorial.AzureBlobStorage.accountKey', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='container', full_name='tutorial.AzureBlobStorage.container', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blobType', full_name='tutorial.AzureBlobStorage.blobType', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blobList', full_name='tutorial.AzureBlobStorage.blobList', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=344,
)

DESCRIPTOR.message_types_by_name['DataFromDF'] = _DATAFROMDF
DESCRIPTOR.message_types_by_name['S3Credential'] = _S3CREDENTIAL
DESCRIPTOR.message_types_by_name['AzureBlobStorage'] = _AZUREBLOBSTORAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataFromDF = _reflection.GeneratedProtocolMessageType('DataFromDF', (_message.Message,), dict(
  DESCRIPTOR = _DATAFROMDF,
  __module__ = 'advantech_afs_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.DataFromDF)
  ))
_sym_db.RegisterMessage(DataFromDF)

S3Credential = _reflection.GeneratedProtocolMessageType('S3Credential', (_message.Message,), dict(
  DESCRIPTOR = _S3CREDENTIAL,
  __module__ = 'advantech_afs_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.S3Credential)
  ))
_sym_db.RegisterMessage(S3Credential)

AzureBlobStorage = _reflection.GeneratedProtocolMessageType('AzureBlobStorage', (_message.Message,), dict(
  DESCRIPTOR = _AZUREBLOBSTORAGE,
  __module__ = 'advantech_afs_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.AzureBlobStorage)
  ))
_sym_db.RegisterMessage(AzureBlobStorage)


# @@protoc_insertion_point(module_scope)
