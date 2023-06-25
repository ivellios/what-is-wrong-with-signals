import dataclasses

from django.dispatch import receiver
from django.test import TestCase

from .signals import MessageSignal


@dataclasses.dataclass
class DataMock:
    required_field: int
    optional_field: int = 5


class SenderMock:
    pass


class MessageSignalTestCase(TestCase):
    def test_send_signal_without_data(self):
        # given
        signal = MessageSignal(DataMock)

        # when, then
        with self.assertRaises(ValueError):
            signal.send(SenderMock)

    def test_send_signal_with_wrong_data_type(self):
        # given
        signal = MessageSignal(DataMock)

        @dataclasses.dataclass
        class OtherDataMock:
            pass

        # when, then
        with self.assertRaises(ValueError):
            signal.send(SenderMock, OtherDataMock())

    def test_send_signal_with_proper_data_type(self):
        # given
        signal = MessageSignal(DataMock)

        @receiver(signal)
        def handle_signal(sender, message: DataMock, **kwargs):
            self.assertEqual(message.required_field, 10)

        # when
        signal.send(
            self.__class__,
            DataMock(
                required_field=10,
            ),
        )
