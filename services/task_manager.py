from models.task import Task
from storage.json_storage import Storage

class TaskManager:
    def __init__(self):
        self.my_storage=Storage()
        self.list_of_tasks=self.my_storage.loading_tasks()
        

    def add_task(self,title:str,description:str, priority:str):
            new_task=Task(title,description,priority)
            self.list_of_tasks.append(new_task)
            added_task=self.my_storage.save_task(self.list_of_tasks)
            return added_task 
            
           
    def show_all_tasks(self):
        return self.list_of_tasks
    

    def task_completed(self,pos:int):
        if pos<0 or pos>len(self.list_of_tasks):
            return
        
        self.list_of_tasks[pos-1].status="completed"
        self.my_storage.save_task(self.list_of_tasks)
    
    def filtered_task_pending_or_completed(self,status:str):
        filtered_tasks_list=[task for task in self.list_of_tasks if task.status==status]
        return filtered_tasks_list 


    def general_summary(self):
        if not self.list_of_tasks:
            return 
        completed=[task_completed for task_completed in self.list_of_tasks if task_completed.status=="completed"] 
        pending=[task_pending for task_pending in self.list_of_tasks if task_pending.status=="pending"] 
        rate=(len(completed)*100)/len(self.list_of_tasks)
        
        return len(completed),len(pending),rate
            
    
    def tasks_for_priority(self):
        priority_high=[task for task in self.list_of_tasks if task.priority=="high"]
        priority_medium=[task for task in self.list_of_tasks if task.priority=="medium"]
        priority_low=[task for task in self.list_of_tasks if task.priority=="low"]
        
        return len(priority_high),len(priority_medium),len(priority_low)
        