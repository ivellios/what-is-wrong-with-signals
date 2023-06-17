import logging

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from todo.models import ToDo

logger = logging.getLogger(__file__)


@receiver(pre_save, sender=ToDo)
def handle_todo_pre_save(sender, instance: ToDo, **kwargs):
    instance.pre_save_status = ToDo.objects.get(pk=instance.pk).status if instance.pk else None
    logger.info("TODO is about to be saved...")
    logger.info("TODO presave status %s", instance.pre_save_status)


@receiver(post_save, sender=ToDo)
def handle_todo_pre_save(sender, instance: ToDo, **kwargs):
    logger.info("TODO has been saved...")
    if instance.status == "archived" and instance.pre_save_status == "active":
        logger.info("TODO has been archived")
