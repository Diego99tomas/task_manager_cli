import pytest
from models.task import Task,Priority,Status


def test_tasks_invalid_priority():
    title="CREATE TESTS"
    description="using pytest"
    invalid_priority="super_high"
    with pytest.raises(ValueError):
        Task(title,description,invalid_priority)
    

def test_default_status_is_pending():

    new_task=Task(
        title="CREATE TESTS",
        description="using pytest",
        priority=Priority.HIGH,
        )

    assert new_task.status is Status.PENDING


