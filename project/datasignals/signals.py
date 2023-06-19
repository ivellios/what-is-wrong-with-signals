import typing

from django.dispatch import Signal


class DataSignal(Signal):
    """

    Example of defining the signal

        @dataclasses.dataclass
        SomeSignalDataClass:
            some_field: int

        some_signal = DataSignal(SomeSignalDataClass)

    Example of sending the signal:

        some_signal.send(
            sender=SomeSenderClass,
            data=SomeSignalDataClass(
                some_field=5
            )
        )

    Example of receiving the signal data:

        @receiver(some_signal)
        def handle_some_signal(sender, data: SomeSignalDataClass, **kwargs):
            print(data.some_field)

    """
    def __init__(self, data_class: typing.Type, use_caching=False):
        # NOTE: In pre 4.0 Django versions you would need
        #       to add providing_args param also.
        super().__init__(use_caching=use_caching)
        self.data_class = data_class

    def send(self, sender, data=None, **named):
        if not isinstance(data, self.data_class):
            raise ValueError(
                f"Wrong dataclass passed to the signal send: {data.__class__}. Expected {self.data_class}"
            )

        return super().send(sender, data=data, **named)
