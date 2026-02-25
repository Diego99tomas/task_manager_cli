import pytest
from models.task import Task,Priority,Status
from datetime import datetime
import uuid


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



def test_auto_id_is_valid():

    new_task=Task(
        title="Auto Id",
        description="testing auto id",
        priority=Priority.MEDIUM,
        )

    assert uuid.UUID(new_task.id)



def test_date_is_valid():

    new_task=Task(
        title="Auto Id",
        description="testing auto id",
        priority=Priority.MEDIUM,
        )
        
    datetime.strptime(new_task.created_at,"%Y-%m-%d")
    assert new_task.created_at is not None
    




