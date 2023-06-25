import dataclasses


@dataclasses.dataclass
class ToDoMessage:
    id: int
    title: str
