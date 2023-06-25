import dataclasses

from datasignals.signals import MessageSignal


@dataclasses.dataclass
class ToDoMessage:
    id: int
    title: str


todo_archived = MessageSignal(ToDoMessage)
