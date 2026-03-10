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
    assert created_task.status==Status.PENDING


def test_add_task_calls_storage(task_manager):
    task_manager.add_task("Title","Descr","high")
    assert task_manager.my_storage.save_calls == 1


def test_add_task_with_invalid_priority(task_manager):
    with pytest.raises(ValueError):
        task_manager.add_task("Title","Descr","super-high")

#testing task_completed feature
def test_task_completed_updates_status(task_manager):
    task=task_manager.add_task("title","desc","medium")
    task_manager.task_completed(task.id)
    task_status_after_update=task.status

    assert task_manager.my_storage.save_calls == 2
    assert task_status_after_update==Status.COMPLETED


def test_if_updates_status_with_an_invalid_id(task_manager):
    task_manager.add_task("title","desc","medium")
    
    with pytest.raises(TaskNotFoundError):
        task_manager.task_completed("321-non_existent_id")

#testing filtered by status
def test_if_filtered_by_status_incorrect(task_manager):
    task_manager.add_task("title","desc","medium")
    with pytest.raises(TypeError):
        task_manager.filtered_task_pending_or_completed("super_completed")
    with pytest.raises(ValueError):
        task_manager.filtered_task_pending_or_completed(Status("super_completed"))

def test_if_filtered_return_result_correctly(task_manager):
    completed=task_manager.add_task("title1","desc","medium")
    task_manager.add_task("title2","desc","low")
    task_manager.add_task("title3","desc","high")
    task_manager.task_completed(completed.id)

    pending=task_manager.filtered_task_pending_or_completed(Status.PENDING)

    assert len(pending)==2

def test_if_filtered_return_empty_list(task_manager):
    empty_list=task_manager.filtered_task_pending_or_completed(Status.PENDING)
    
    assert empty_list == []

def test_delete_task_raises_if_list_empty(task_manager):
    fake_id="1234-non-existent-id"

    with pytest.raises(TaskNotFoundError):
        task_manager.delete_task(fake_id)

    assert task_manager.my_storage.save_calls == 0


def test_delete_task_really_delete(task_manager):
    new_task1=task_manager.add_task("title1","desc1","medium")
    task_manager.add_task("title2","desc2","low")

    task_id=new_task1.id
    task_manager.delete_task(task_id)

    assert task_id not in task_manager.tasks

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

        