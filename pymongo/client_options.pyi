from typing import Any, Dict, Optional, Tuple

from bson.codec_options import CodecOptions
from pymongo.auth import MongoCredential
from pymongo.pool import PoolOptions
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import _ServerMode
from pymongo.ssl_support import SSLContext
from pymongo.write_concern import WriteConcern


def _parse_credentials(username: str, password: str, database: str, options: Dict[str, Any]) -> Optional[MongoCredential]: ...
def _parse_read_preference(options: Dict[str, Any]) -> _ServerMode: ...
def _parse_write_concern(options: Dict[str, Any]) -> WriteConcern: ...
def _parse_read_concern(options: Dict[str, Any]) -> ReadConcern: ...
def _parse_ssl_options(options: Dict[str, Any]) -> Tuple[Optional[SSLContext], bool]: ...
def _parse_pool_options(options: Dict[str, Any]) -> PoolOptions: ...

class ClientOptions(object):
    def __init__(self, username: str, password: str, database: str, options: Dict[str, Any]) -> None: ...
    @property
    def _options(self) -> Dict[str, Any]: ...
    @property
    def connect(self) -> bool: ...
    @property
    def codec_options(self) -> CodecOptions: ...
    @property
    def credentials(self) -> MongoCredential: ...
    @property
    def local_threshold_ms(self) -> int: ...
    @property
    def server_selection_timeout(self) -> int: ...
    @property
    def heartbeat_frequency(self) -> int: ...
    @property
    def pool_options(self) -> PoolOptions: ...
    @property
    def read_preference(self) -> _ServerMode: ...
    @property
    def replica_set_name(self) -> Optional[str]: ...
    @property
    def write_concern(self) -> WriteConcern: ...
    @property
    def read_concern(self) -> ReadConcern: ...
