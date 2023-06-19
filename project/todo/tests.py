from unittest import mock

import pytest

from todo.signals import ToDoData
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


@pytest.mark.django_db
@mock.patch("todo.signals.todo_archived.send")
def test_sending_archive_signal(archived_signal_mock: mock.Mock):
    todo = ToDo.objects.create(title="Some TODO", status="active")
    todo.archive()
    archived_signal_mock.assert_called_with(
        sender=ToDo, data=ToDoData(id=todo.pk, title=str(todo.title))
    )


@pytest.mark.django_db
@mock.patch("todo.signals.todo_archived.send")
def test_not_sending_archive_signal(archived_signal_mock: mock.Mock):
    todo = ToDo.objects.create(title="Some TODO", status="archived")
    todo.archive()
    archived_signal_mock.assert_not_called()
