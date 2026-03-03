from models.task import Task,Status,Priority
from core.custom_exceptions import TaskNotFoundError

class TaskManager:
    def __init__(self,storage):
        self.my_storage=storage
        self.list_of_tasks=self.my_storage.loading_tasks()
        

    def add_task(self,title:str,description:str, priority:str):
            new_task=Task(title,description,Priority(priority))
            self.list_of_tasks.append(new_task)
            self.my_storage.save_task(self.list_of_tasks) 
            return new_task  
            
           
    def show_all_tasks(self):
        return self.list_of_tasks
    

    def task_completed(self,task_id):
            for task in self.list_of_tasks:
                if task.id==task_id:
                    task.status=Status.COMPLETED
                    self.my_storage.save_task(self.list_of_tasks)
                    return task
            raise TaskNotFoundError(task_id)


    def filtered_task_pending_or_completed(self,status:str)-> list:
        filtered_tasks_list=[task for task in self.list_of_tasks if task.status==status]
        return filtered_tasks_list 


    def general_summary(self)->list:
        if not self.list_of_tasks:
            return [(0),(0),(0.0)]
        
        completed=[] 
        pending=[] 
        
        for task_status in self.list_of_tasks:
            if task_status.status == "completed":
                completed.append(task_status)
            else:
                pending.append(task_status)        
        
        rate=(len(completed)*100)/len(self.list_of_tasks)
        summary=[len(completed),len(pending),rate]
        return summary
            
    
    def tasks_for_priority(self):
        priority_high=[]
        priority_medium=[]
        priority_low=[]

        for task in self.list_of_tasks:
            if task.priority=="high":
                priority_high.append(task)
            elif task.priority=="medium":
                priority_medium.append(task)
            else:
                priority_low.append(task)
        
        return len(priority_high),len(priority_medium),len(priority_low)

    
    def delete_task(self,id_for_delete):
        # if not self.list_of_tasks:
        #     return
        for task in self.list_of_tasks:
            if task.id==id_for_delete:
                self.list_of_tasks.remove(task)
                self.my_storage.save_task(self.list_of_tasks)
                return task
        raise TaskNotFoundError(id_for_delete)
              