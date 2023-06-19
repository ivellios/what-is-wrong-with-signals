import logging

from django.dispatch import receiver

from todo.signals import todo_archived, ToDoData

logger = logging.getLogger(__file__)


@receiver(todo_archived)
def handle_todo_archived(sender, data: ToDoData, **kwargs):
    logger.info("TODO has been archived title=%s", data.title)
