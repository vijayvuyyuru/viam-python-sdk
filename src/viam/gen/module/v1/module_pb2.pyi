"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from ... import app
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
from ... import robot
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class AddResourceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONFIG_FIELD_NUMBER: builtins.int
    DEPENDENCIES_FIELD_NUMBER: builtins.int

    @property
    def config(self) -> app.v1.robot_pb2.ComponentConfig:
        ...

    @property
    def dependencies(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        ...

    def __init__(self, *, config: app.v1.robot_pb2.ComponentConfig | None=..., dependencies: collections.abc.Iterable[builtins.str] | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['config', b'config']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['config', b'config', 'dependencies', b'dependencies']) -> None:
        ...
global___AddResourceRequest = AddResourceRequest

@typing_extensions.final
class AddResourceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___AddResourceResponse = AddResourceResponse

@typing_extensions.final
class ReconfigureResourceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONFIG_FIELD_NUMBER: builtins.int
    DEPENDENCIES_FIELD_NUMBER: builtins.int

    @property
    def config(self) -> app.v1.robot_pb2.ComponentConfig:
        ...

    @property
    def dependencies(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        ...

    def __init__(self, *, config: app.v1.robot_pb2.ComponentConfig | None=..., dependencies: collections.abc.Iterable[builtins.str] | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['config', b'config']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['config', b'config', 'dependencies', b'dependencies']) -> None:
        ...
global___ReconfigureResourceRequest = ReconfigureResourceRequest

@typing_extensions.final
class ReconfigureResourceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___ReconfigureResourceResponse = ReconfigureResourceResponse

@typing_extensions.final
class RemoveResourceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___RemoveResourceRequest = RemoveResourceRequest

@typing_extensions.final
class RemoveResourceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___RemoveResourceResponse = RemoveResourceResponse

@typing_extensions.final
class HandlerDefinition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUBTYPE_FIELD_NUMBER: builtins.int
    MODELS_FIELD_NUMBER: builtins.int

    @property
    def subtype(self) -> robot.v1.robot_pb2.ResourceRPCSubtype:
        ...

    @property
    def models(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        ...

    def __init__(self, *, subtype: robot.v1.robot_pb2.ResourceRPCSubtype | None=..., models: collections.abc.Iterable[builtins.str] | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['subtype', b'subtype']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['models', b'models', 'subtype', b'subtype']) -> None:
        ...
global___HandlerDefinition = HandlerDefinition

@typing_extensions.final
class HandlerMap(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HANDLERS_FIELD_NUMBER: builtins.int

    @property
    def handlers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___HandlerDefinition]:
        ...

    def __init__(self, *, handlers: collections.abc.Iterable[global___HandlerDefinition] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['handlers', b'handlers']) -> None:
        ...
global___HandlerMap = HandlerMap

@typing_extensions.final
class ReadyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_ADDRESS_FIELD_NUMBER: builtins.int
    parent_address: builtins.str

    def __init__(self, *, parent_address: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['parent_address', b'parent_address']) -> None:
        ...
global___ReadyRequest = ReadyRequest

@typing_extensions.final
class ReadyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    READY_FIELD_NUMBER: builtins.int
    HANDLERMAP_FIELD_NUMBER: builtins.int
    ready: builtins.bool

    @property
    def handlermap(self) -> global___HandlerMap:
        ...

    def __init__(self, *, ready: builtins.bool=..., handlermap: global___HandlerMap | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['handlermap', b'handlermap']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['handlermap', b'handlermap', 'ready', b'ready']) -> None:
        ...
global___ReadyResponse = ReadyResponse

@typing_extensions.final
class ValidateConfigRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONFIG_FIELD_NUMBER: builtins.int

    @property
    def config(self) -> app.v1.robot_pb2.ComponentConfig:
        ...

    def __init__(self, *, config: app.v1.robot_pb2.ComponentConfig | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['config', b'config']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['config', b'config']) -> None:
        ...
global___ValidateConfigRequest = ValidateConfigRequest

@typing_extensions.final
class ValidateConfigResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DEPENDENCIES_FIELD_NUMBER: builtins.int

    @property
    def dependencies(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        ...

    def __init__(self, *, dependencies: collections.abc.Iterable[builtins.str] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['dependencies', b'dependencies']) -> None:
        ...
global___ValidateConfigResponse = ValidateConfigResponse