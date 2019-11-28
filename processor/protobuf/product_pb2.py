# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: product.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='product.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rproduct.proto\"\xc2\x02\n\x07Product\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ompany\x18\x02 \x01(\t\x12\x1b\n\x04info\x18\x03 \x01(\x0b\x32\r.Product.Info\x12\"\n\x04type\x18\x04 \x01(\x0e\x32\x14.Product.ProductType\x12\r\n\x05\x66ield\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\x04\x1a:\n\x08\x44ocument\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x1a\x41\n\x04Info\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12$\n\tdocuments\x18\x02 \x03(\x0b\x32\x11.Product.Document\"6\n\x0bProductType\x12\r\n\tHARVESTED\x10\x00\x12\r\n\tPROCESSED\x10\x01\x12\t\n\x05\x46INAL\x10\x02\"-\n\x10ProductContainer\x12\x19\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x08.Productb\x06proto3')
)



_PRODUCT_PRODUCTTYPE = _descriptor.EnumDescriptor(
  name='ProductType',
  full_name='Product.ProductType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HARVESTED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROCESSED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINAL', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=286,
  serialized_end=340,
)
_sym_db.RegisterEnumDescriptor(_PRODUCT_PRODUCTTYPE)


_PRODUCT_DOCUMENT = _descriptor.Descriptor(
  name='Document',
  full_name='Product.Document',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='Product.Document.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hash', full_name='Product.Document.hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='Product.Document.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=217,
)

_PRODUCT_INFO = _descriptor.Descriptor(
  name='Info',
  full_name='Product.Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='Product.Info.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='documents', full_name='Product.Info.documents', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=284,
)

_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Product.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='company', full_name='Product.company', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='Product.info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Product.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field', full_name='Product.field', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Product.timestamp', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PRODUCT_DOCUMENT, _PRODUCT_INFO, ],
  enum_types=[
    _PRODUCT_PRODUCTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=340,
)


_PRODUCTCONTAINER = _descriptor.Descriptor(
  name='ProductContainer',
  full_name='ProductContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='ProductContainer.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=387,
)

_PRODUCT_DOCUMENT.containing_type = _PRODUCT
_PRODUCT_INFO.fields_by_name['documents'].message_type = _PRODUCT_DOCUMENT
_PRODUCT_INFO.containing_type = _PRODUCT
_PRODUCT.fields_by_name['info'].message_type = _PRODUCT_INFO
_PRODUCT.fields_by_name['type'].enum_type = _PRODUCT_PRODUCTTYPE
_PRODUCT_PRODUCTTYPE.containing_type = _PRODUCT
_PRODUCTCONTAINER.fields_by_name['entries'].message_type = _PRODUCT
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
DESCRIPTOR.message_types_by_name['ProductContainer'] = _PRODUCTCONTAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), dict(

  Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), dict(
    DESCRIPTOR = _PRODUCT_DOCUMENT,
    __module__ = 'product_pb2'
    # @@protoc_insertion_point(class_scope:Product.Document)
    ))
  ,

  Info = _reflection.GeneratedProtocolMessageType('Info', (_message.Message,), dict(
    DESCRIPTOR = _PRODUCT_INFO,
    __module__ = 'product_pb2'
    # @@protoc_insertion_point(class_scope:Product.Info)
    ))
  ,
  DESCRIPTOR = _PRODUCT,
  __module__ = 'product_pb2'
  # @@protoc_insertion_point(class_scope:Product)
  ))
_sym_db.RegisterMessage(Product)
_sym_db.RegisterMessage(Product.Document)
_sym_db.RegisterMessage(Product.Info)

ProductContainer = _reflection.GeneratedProtocolMessageType('ProductContainer', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCTCONTAINER,
  __module__ = 'product_pb2'
  # @@protoc_insertion_point(class_scope:ProductContainer)
  ))
_sym_db.RegisterMessage(ProductContainer)


# @@protoc_insertion_point(module_scope)