from services.task_manager import TaskManager
from models.task import Status
from core.custom_exceptions import TaskNotFoundError

import pytest

class FakeStorage():
    def __init__(self):
       self.save_to_do_list=[]
       self.save_calls=0

    def loading_tasks(self)->list:
        return self.save_to_do_list
    
    def save_task(self,new_list):
        self.save_to_do_list=new_list
        self.save_calls+=1
        

@pytest.fixture
def task_manager():
    fake_storage=FakeStorage()
    task_manager=TaskManager(fake_storage)
    return task_manager


def test_add_task_creates_task_with_default_status(task_manager):
    created_task=task_manager.add_task("Title","Descr","high")

    assert created_task.title=="Title"
    assert created_task.description=="Descr"
    assert created_task.status.value==Status.PENDING


def test_add_task_calls_storage(task_manager):
    task_manager.add_task("Title","Descr","high")
    assert task_manager.my_storage.save_calls == 1


def test_add_task_with_invalid_priority(task_manager):
    with pytest.raises(ValueError):
        task_manager.add_task("Title","Descr","super-high")

def test_delete_task_raises_if_list_empty(task_manager):
    fake_id="1234-non-existent-id"

    with pytest.raises(TaskNotFoundError):
        task_manager.delete_task(fake_id)

    assert task_manager.my_storage.save_calls == 0


def test_delete_task_invalid_id_does_not_modify_list(task_manager):
    created=task_manager.add_task("Title", "Desc", "high")
    create_id=created.id
    cont=task_manager.my_storage.save_calls
    initial_length = len(task_manager.tasks)

    with pytest.raises(TaskNotFoundError):
        task_manager.delete_task("fake-id")

    assert len(task_manager.tasks) == initial_length
    assert task_manager.my_storage.save_calls == cont
    assert create_id in task_manager.tasks

        