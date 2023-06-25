import logging

from django.dispatch import receiver

from shared.messages import ToDoMessage
from shared.signals import todo_archived

logger = logging.getLogger(__file__)


@receiver(todo_archived)
def handle_todo_archived(sender, message: ToDoMessage, **kwargs):
    logger.info("TODO has been archived title=%s", message.title)
