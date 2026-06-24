from dataclasses import dataclass


@dataclass(slots=True)
class Client:
    id: int
    name: str


@dataclass(slots=True)
class Post:
    id: int
    client_id: int
    media_type: str
    media_paths: str
    caption: str
    status: str
