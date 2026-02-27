from services.task_manager import TaskManager
from models.task import Status

import pytest

class FakeStorage():
    def __init__(self):
       self.save_to_do_list=[]
       self.was_saved=False

    def loading_tasks(self)->list:
        return self.save_to_do_list
    
    def save_task(self,new_list):
        self.save_to_do_list=new_list
        self.was_saved=True
        

@pytest.fixture
def fake_storage():
    fake_storage=FakeStorage()
    task_manager=TaskManager(fake_storage)
    return task_manager

#only if add_task return new task
def test_if_added_task(fake_storage):
    created_task=fake_storage.add_task("Title","Descr","high")

    assert created_task.title=="Title"
    assert created_task.description=="Descr"
    assert created_task.status.value==Status.PENDING


def test_add_task_calls_storage(fake_storage):
    fake_storage.add_task("Title","Descr","high")
    assert fake_storage.my_storage.was_saved is True


def test_add_task_with_invalid_priority(fake_storage):
    with pytest.raises(ValueError):
        fake_storage.add_task("Title","Descr","super-high")


def test_task_completed(fake_storage):
    fake_storage.add_task("Title","Descr","high")
    status_completed=fake_storage.task_completed(1)

    assert status_completed.status == Status.COMPLETED
    

        