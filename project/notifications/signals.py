import logging

from messagesignals.signals import async_receiver
from shared.messages import ToDoMessage
from shared.signals import todo_archived

logger = logging.getLogger(__file__)


@async_receiver(todo_archived, ToDoMessage)
def handle_todo_archived(sender, message: ToDoMessage, **kwargs):
    logger.info("TODO has been archived title=%s", message.title)
