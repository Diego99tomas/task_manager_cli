from models.task import Task,Status,Priority
from core.custom_exceptions import TaskNotFoundError

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
            if not task_id in self.tasks:
                raise TaskNotFoundError(task_id)
            
            task=self.tasks[task_id]
            task.status=Status.COMPLETED
            self.my_storage.save_task(list(self.tasks.values())) 
            return task


    def filtered_task_pending_or_completed(self,status:str)-> list:
        filtered_tasks_list=[task for task in self.tasks.values() if task.status==status]
        return filtered_tasks_list 


    def general_summary(self)->list:
        if not self.tasks:
            return [(0),(0),(0.0)]
        
        completed=[] 
        pending=[] 
        
        for task_status in self.tasks.values():
            if task_status.status == "completed":
                completed.append(task_status)
            else:
                pending.append(task_status)        
        
        rate=(len(completed)*100)/len(self.tasks.values())
        summary=[len(completed),len(pending),rate]
        return summary
            
    
    def tasks_for_priority(self):
        priority_high=[]
        priority_medium=[]
        priority_low=[]

        for task in self.tasks.values():
            if task.priority=="high":
                priority_high.append(task)
            elif task.priority=="medium":
                priority_medium.append(task)
            else:
                priority_low.append(task)
        
        return len(priority_high),len(priority_medium),len(priority_low)

    
    def delete_task(self,id_for_delete):
        if not id_for_delete in self.tasks:
            raise TaskNotFoundError(id_for_delete)

        t=self.tasks.pop(id_for_delete)
        self.my_storage.save_task(list(self.tasks.values())) 
        return t
              