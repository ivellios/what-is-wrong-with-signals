import logging

from datasignals.signals import async_receiver
from todo.signals import todo_archived, ToDoMessage

logger = logging.getLogger(__file__)


@async_receiver(todo_archived, ToDoMessage)
def handle_todo_archived(sender, message: ToDoMessage, **kwargs):
    logger.info("TODO has been archived title=%s", message.title)
