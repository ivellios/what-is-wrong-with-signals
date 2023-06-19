import dataclasses

from datasignals.signals import DataSignal


@dataclasses.dataclass
class ToDoData:
    id: int
    title: str


todo_archived = DataSignal(ToDoData)
