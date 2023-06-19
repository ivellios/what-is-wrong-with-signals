import dataclasses

from django.dispatch import receiver
from django.test import TestCase

from .signals import DataSignal


@dataclasses.dataclass
class DataMock:
    required_field: int
    optional_field: int = 5


class SenderMock:
    pass


class DataSignalTestCase(TestCase):

    def test_send_signal_without_data(self):
        # given
        signal = DataSignal(DataMock)

        # when, then
        with self.assertRaises(ValueError):
            signal.send(SenderMock)

    def test_send_signal_with_wrong_data_type(self):
        # given
        signal = DataSignal(DataMock)

        @dataclasses.dataclass
        class OtherDataMock:
            pass

        # when, then
        with self.assertRaises(ValueError):
            signal.send(SenderMock, OtherDataMock())

    def test_send_signal_with_proper_data_type(self):
        # given
        signal = DataSignal(DataMock)

        @receiver(signal)
        def handle_signal(sender, data: DataMock, **kwargs):
            self.assertEqual(data.required_field, 10)

        # when
        signal.send(self.__class__, DataMock(
            required_field=10,
        ))
