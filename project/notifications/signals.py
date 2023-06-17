import logging

from django.dispatch import receiver

from todo.models import ToDo
from todo.signals import todo_archived

logger = logging.getLogger(__file__)


@receiver(todo_archived, sender=ToDo)
def handle_todo_archived(sender, instance: ToDo, **kwargs):
    logger.info("TODO has been archived")
