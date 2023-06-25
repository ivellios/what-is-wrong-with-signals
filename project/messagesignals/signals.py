import json
import typing
from functools import wraps

from django.dispatch import Signal
from django.dispatch import receiver

from project.celery import app


class MessageSignal(Signal):
    """

    Example of defining the signal

        @dataclasses.dataclass
        SomeSignalMessage:
            some_field: int

        some_signal = MessageSignal(SomeSignalMessage)

    Example of sending the signal:

        some_signal.send(
            sender=SomeSenderClass,
            message=SomeSignalMessage(
                some_field=5
            )
        )

    Example of receiving the signal data:

        @receiver(some_signal)
        def handle_some_signal(sender, message: SomeSignalMessage, **kwargs):
            print(message.some_field)

    """

    def __init__(self, message_class: typing.Type, use_caching=False):
        # NOTE: In pre 4.0 Django versions you would need
        #       to add providing_args param also.
        super().__init__(use_caching=use_caching)
        self.message_class = message_class

    def send(self, sender, message=None, **named):
        if not isinstance(message, self.message_class):
            raise ValueError(
                f"Wrong message dataclass passed to the signal send: {message.__class__}. Expected {self.message_class}"
            )

        return super().send(sender, message=message, **named)


def celery_signal_receiver(task, signal, **kwargs):
    @wraps(task)
    @receiver(signal, **kwargs)
    def handler(
        signal=None, sender=None, message: typing.Type = None, *_args, **_kwargs
    ):
        message_data = json.dumps(message.__dict__) if message else ""
        return task.delay(message_data, *_args, **_kwargs)

    return handler


def celery_adapter(func, message_type: typing.Type):
    @wraps(func)
    def inner(message_data: str, *args, **kwargs):
        message = message_type(**json.loads(message_data)) if message_data else None
        return func(sender=None, message=message, *args, **kwargs)

    return inner


def event_receiver(
    signal,
    message_type: typing.Type,
    celery_task_options: typing.Optional[typing.Dict] = None,
    **options,
):
    if celery_task_options is None:
        celery_task_options = dict()

    def decorator(func):
        adapter = celery_adapter(func, message_type)
        task = app.task(**celery_task_options)(adapter)
        celery_signal_receiver(task, signal, **options)
        app.register_task(task)
        return func

    return decorator
