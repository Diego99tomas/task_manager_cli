from models.task import Task,Status,Priority
from core.custom_exceptions import TaskNotFoundError
from collections import Counter

class TaskManager:
    def __init__(self,storage):
        self.my_storage=storage
        loaded_tasks=self.my_storage.loading_tasks()
        self.tasks={task.id:task for task in loaded_tasks}

        
    def add_task(self,title:str,description:str, priority:str):
            new_task=Task(title,description,Priority(priority))
            self.tasks[new_task.id]=new_task
            self.my_storage.save_task(list(self.tasks.values())) 
            return new_task  
            
           
    def show_all_tasks(self)->dict:
        """ Returm they values of dict"""
        return self.tasks.values()
    

    def task_completed(self,task_id:str)->Task:
            """Seach by id and change status to completed"""
            self._get_task_or_raise(task_id)
            
            task=self.tasks[task_id]
            task.status=Status.COMPLETED
            self.my_storage.save_task(list(self.tasks.values())) 
            return task


    def filtered_task_pending_or_completed(self,status:Status)-> list[Task]:
        """Filtered tasks by status (completed or pending) and return list"""
        if not isinstance(status,Status):
             raise TypeError
        filtered_tasks_list=[task for task in self.tasks.values() if task.status==status]
        return filtered_tasks_list 


    def general_summary(self)->dict:
        """Show a summary the tasks completed and pending
         and rate of tasks completed """
        total=len(self.tasks)
        if total==0:
            return {"completed":0,"pending":0,"rate":0.0}
        
        counts_status=Counter(task.status for task in self.tasks.values())
        completed=counts_status[Status.COMPLETED] 
        pending=counts_status[Status.PENDING]
        
        rate=(completed * 100) / total
        return {"completed":completed,
                "pending":pending,
                "rate":round(rate,2)
                }
        
    
    def tasks_for_priority(self):
        """Show quantity the tasks by priority"""
        counts=Counter(task.priority for task in self.tasks.values())
        return{
            "High": counts[Priority.HIGH],
            "Medium": counts[Priority.MEDIUM],
            "Low": counts[Priority.LOW]
        }

    
    def delete_task(self,id_for_delete:str):
        self._get_task_or_raise(id_for_delete)

        t=self.tasks.pop(id_for_delete)
        self.my_storage.save_task(list(self.tasks.values())) 
        return t
    
    
    def _get_task_or_raise(self,task_id):
        if not task_id in self.tasks:
            raise TaskNotFoundError(task_id)