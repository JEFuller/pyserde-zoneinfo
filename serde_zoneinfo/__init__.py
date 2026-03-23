from datetime import timedelta
from plum import dispatch
from typing import Type, Any
from zoneinfo import ZoneInfo
import serde


class Serializer:
    @dispatch
    def serialize(self, value: ZoneInfo) -> Any:
        return value.key


class Deserializer:
    @dispatch
    def deserialize(self, cls: Type[ZoneInfo], value: Any) -> ZoneInfo:
        return ZoneInfo(value)


def init() -> None:
    """
    Initialize pyserde-zoneinfo extension.
    Be sure to call this function before declaring pyserde class.
    """
    serde.add_serializer(Serializer())
    serde.add_deserializer(Deserializer())
