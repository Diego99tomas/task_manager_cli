
import json
from models.task import Task
from storage.json_storage import Storage

class TaskManager:
    def __init__(self):
        self.my_storage=Storage()
        self.list_of_tasks=self.my_storage.save_to_do_list
        

    def add_task(self,title:str,description:str, priority:str):
            new_task=Task(title,description,priority)
            self.list_of_tasks.append(new_task)
            self.my_storage.save_task(self.list_of_tasks)
            
           
    def show_all_tasks(self):
        if not self.list_of_tasks:
            print("There are no tasks")
            return
        for i,task in enumerate(self.list_of_tasks):
            i+=1
            print(f"{i}. ",task)
    

    def task_completed(self,pos):
        self.list_of_tasks[pos-1].status="completed"
        self.my_storage.save_task(self.list_of_tasks)

    
    def filtered_task_pending_or_completed(self,status):
        filtered_tasks_list=[print(task) for task in self.list_of_tasks if task.status==status]
        print(f"{len(filtered_tasks_list)} match were found")  



        


