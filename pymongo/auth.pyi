from typing import Any, Dict, FrozenSet, NamedTuple

from pymongo.pool import SocketInfo

MECHANISMS: FrozenSet[str] = ...

class MongoCredential(NamedTuple):
    mechanism: str
    source: str
    username: str
    password: str
    props: Any
class GSSAPIProperties(NamedTuple):
    service_name: str
    canonicalize_host_name: bool
    service_realm: Any
def _build_credentials_tuple(mech: str, source: str, user: str, passwd: str, extra: Dict[str, Any]) -> MongoCredential: ...
def _parse_scram_response(response: bytes) -> Dict[bytes, int]: ...
def _authenticate_scram_sha1(credentials: MongoCredential, sock_info: SocketInfo) -> None: ...
def _password_digest(username: str, password: str) -> str: ...
def _auth_key(nonce: str, username: str, password: str) -> str: ...
def _authenticate_gssapi(credentials: MongoCredential, sock_info: SocketInfo) -> None: ...
def _authenticate_plain(credentials: MongoCredential, sock_info: SocketInfo) -> None: ...
def _authenticate_cram_md5(credentials: MongoCredential, sock_info: SocketInfo) -> None: ...
def _authenticate_x509(credentials: MongoCredential, sock_info: SocketInfo) -> None: ...
def _authenticate_mongo_cr(credentials: MongoCredential, sock_info: SocketInfo) -> None: ...
def _authenticate_default(credentials: MongoCredential, sock_info: SocketInfo) -> None: ...
def authenticate(credentials: MongoCredential, sock_info: SocketInfo) -> None: ...
def logout(source: str, sock_info: SocketInfo) -> None: ...
