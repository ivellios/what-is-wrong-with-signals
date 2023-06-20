import dataclasses

from datasignals.signals import DataSignal


@dataclasses.dataclass
class ToDoMessage:
    id: int
    title: str


todo_archived = DataSignal(ToDoMessage)
