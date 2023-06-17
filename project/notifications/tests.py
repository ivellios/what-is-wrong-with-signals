from unittest import mock

import pytest

from todo.models import ToDo


# Create your tests here.



@pytest.mark.django_db
@mock.patch("logging.Logger.info")
def test_saving_todo_calls_info(logging_mock: mock.Mock):
    todo = ToDo.objects.create(title="Some todo", status="active")
    logging_mock.reset_mock()
    todo.status = "archived"

    todo.save()

    logging_mock.assert_called_with("TODO has been archived")
