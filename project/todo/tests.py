from unittest import mock

import pytest

from .models import ToDo


# Create your tests here.


@pytest.mark.django_db
@mock.patch("django.db.models.signals.pre_save.send")
def test_saving_todo_dispatches_pre_save_signal(pre_save_send_mock: mock.Mock):
    ToDo.objects.create(title="Some todo")
    pre_save_send_mock.assert_called_once()


@pytest.mark.django_db
@mock.patch("django.db.models.signals.post_save.send")
def test_saving_todo_dispatches_post_save_signal(post_save_send_mock: mock.Mock):
    ToDo.objects.create(title="Some todo")
    post_save_send_mock.assert_called_once()
