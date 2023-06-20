import logging

from django.dispatch import receiver

from todo.signals import todo_archived, ToDoMessage

logger = logging.getLogger(__file__)


@receiver(todo_archived)
def handle_todo_archived(sender, message: ToDoMessage, **kwargs):
    logger.info("TODO has been archived title=%s", message.title)
