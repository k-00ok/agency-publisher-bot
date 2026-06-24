from dataclasses import dataclass


@dataclass(slots=True)
class Client:
    id: int
    name: str
