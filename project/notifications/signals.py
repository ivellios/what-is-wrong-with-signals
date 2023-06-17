import logging

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from todo.models import ToDo

logger = logging.getLogger(__file__)


@receiver(pre_save, sender=ToDo)
def handle_todo_pre_save(sender, **kwargs):
    logger.info("TODO is about to be saved...")


@receiver(post_save, sender=ToDo)
def handle_todo_pre_save(sender, instance: ToDo, **kwargs):
    logger.info("TODO has been saved...")
    if instance.status == "archived":
        logger.info("Note has been archived?")
