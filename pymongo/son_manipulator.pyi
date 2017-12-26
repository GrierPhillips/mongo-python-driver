from typing import Any, Dict, Mapping

from pymongo.collection import Collection
from pymongo.database import Database


class SONManipulator(object):
    def will_copy(self) -> bool: ...
    def transform_incoming(self, son: Mapping[str, Any], collection: Collection) -> Dict[str, Any]: ...
    def transform_outgoing(self, son: Mapping[str, Any], collection: Collection) -> Dict[str, Any]: ...

class ObjectIdInjector(SONManipulator):
    def transform_incoming(self, son: Mapping[str, Any], collection: Collection) -> Dict[str, Any]: ...

class ObjectIdShuffler(SONManipulator):
    def will_copy(self) -> bool: ...
    def transform_incoming(self, son: Mapping[str, Any], collection: Collection) -> Dict[str, Any]: ...

class NamespaceInjector(SONManipulator):
    def transform_incoming(self, son: Mapping[str, Any], collection: Collection) -> Dict[str, Any]: ...

class AutoReference(SONManipulator):
    def __init__(self, db: Database) -> None: ...
    def will_copy(self) -> bool: ...
    def transform_incoming(self, son: Mapping[str, Any], collection: Collection) -> Dict[str, Any]: ...
    def transform_outgoing(self, son: Mapping[str, Any], collection: Collection) -> Dict[str, Any]: ...
