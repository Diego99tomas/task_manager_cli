from datetime import date
import uuid


class Task:
    def __init__(self,title:str,description:str,priority:str,id=None,created_at=None,status="pending"):
        priority_options=["high","medium","low"]
        
        self.id=id if id else uuid.uuid4().__str__()
        self.title=title
        self.description=description
        
        if priority not in priority_options:
            raise ValueError(f"Invalid option. Choice {priority_options} " )
        self.priority=priority

        self.status=status
        self.created_at=created_at if created_at else date.today().__str__()

 
    def __str__(self):
        return f"{self.id} | Task: {self.title} | Description: {self.description} | Priority: {self.priority} | Status: {self.status} | Date created: {self.created_at} "

