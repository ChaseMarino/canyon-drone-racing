# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VehicleStatus.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Route_pb2 as Route__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13VehicleStatus.proto\x12\x08tutorial\x1a\x0bRoute.proto\"2\n\x0fVehicleVelocity\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\";\n\x0fVehicleAttitude\x12\r\n\x05pitch\x18\x01 \x01(\x01\x12\x0b\n\x03yaw\x18\x02 \x01(\x01\x12\x0c\n\x04roll\x18\x03 \x01(\x01\"\xa2\x01\n\rVehicleStatus\x12$\n\x08location\x18\x01 \x01(\x0b\x32\x12.tutorial.Location\x12.\n\x0bvelocityXYZ\x18\x02 \x01(\x0b\x32\x19.tutorial.VehicleVelocity\x12+\n\x08\x61ttitude\x18\x03 \x01(\x0b\x32\x19.tutorial.VehicleAttitude\x12\x0e\n\x06status\x18\x04 \x01(\tB3\n/com.dji.sdk.sample.tigersalvage.proto.generatedP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'VehicleStatus_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n/com.dji.sdk.sample.tigersalvage.proto.generatedP\001'
  _VEHICLEVELOCITY._serialized_start=46
  _VEHICLEVELOCITY._serialized_end=96
  _VEHICLEATTITUDE._serialized_start=98
  _VEHICLEATTITUDE._serialized_end=157
  _VEHICLESTATUS._serialized_start=160
  _VEHICLESTATUS._serialized_end=322
# @@protoc_insertion_point(module_scope)
