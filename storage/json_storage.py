import json
from models.task import Task

class Storage:
    NAME_STORAGE="storage/stored_tasks.json"
    
    def __init__(self):
       self.save_to_do_list=[]
       self.loading_tasks()

    
    def loading_tasks(self)->list:
        try:
            with open(self.NAME_STORAGE,"r") as loading_tasks:
                tasks=json.load(loading_tasks) 
                self.save_to_do_list=[self.from_dict(t) for t in tasks]
                return self.save_to_do_list
        except FileNotFoundError:
            self.save_to_do_list=[]
            return self.save_to_do_list
    

    def save_task(self,new_list)->bool:
            with open(self.NAME_STORAGE,"w") as add_task:
                    json.dump([self.to_dict(task) for task in new_list],
                            add_task,indent=4)
                    return True


    @staticmethod
    def to_dict(task):
        return {
            "id": task.id,
            "title":task.title,
            "description":task.description,
            "priority":task.priority,
            "status":task.status,
            "created_at":task.created_at
        }  
    
    
    @staticmethod
    def from_dict(data):
        return Task(id=data["id"],title=data["title"],description=data["description"],priority=data["priority"],status=data["status"],created_at=data["created_at"])
    
