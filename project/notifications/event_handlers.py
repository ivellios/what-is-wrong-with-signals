import logging

from celery_signals import receiver_task

from shared.messages import ToDoMessage
from shared.signals import todo_archived

logger = logging.getLogger(__file__)


@receiver_task(todo_archived)
def handle_todo_archived(sender, message: ToDoMessage, **kwargs):
    logger.info("TODO has been archived title=%s", message.title)
