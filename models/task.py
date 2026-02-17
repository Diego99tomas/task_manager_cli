from datetime import date
import uuid


class Task:
    def __init__(self,title:str,description:str,priority:str,id=None,created_at=None,status="pending"):
        status_options=['pending',"completed"]
        priority_options=["high","medium","low"]
        
        self.id=id if id else uuid.uuid4().__str__()
        self.title=title
        self.description=description
        
        if priority not in priority_options:
            raise ValueError(f"Invalid option. Choice {priority_options} " )
        self.priority=priority
        
        if status not in status_options:
            raise ValueError(f"Invalid option. Choice {status_options}" )
        self.status=status
        self.created_at=created_at if created_at else date.today().__str__()

    def to_dict(self):
        return {
            "id": self.id,
            "title":self.title,
            "description":self.description,
            "priority":self.priority,
            "status":self.status,
            "created_at":self.created_at
        }  

    @staticmethod
    def from_dict(data):
        return Task(id=data["id"],title=data["title"],description=data["description"],priority=data["priority"],status=data["status"],created_at=data["created_at"])
    
    def __str__(self):
        return f"{self.id} | Task: {self.title} | Description: {self.description} | Priority: {self.priority} | Status: {self.status} | Date created: {self.created_at} "

