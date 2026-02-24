from datetime import date
from enum import Enum
import uuid

class Status(str,Enum):
    PENDING='pending'
    COMPLETED='completed'

class Priority(str,Enum):
    HIGH='high'
    MEIDUM='medium'
    LOW='low'

class Task:
    def __init__(self,title:str,description:str,priority:Priority,status=Status.PENDING,id=None,created_at=None): 
        
        self.id=id if id else uuid.uuid4().__str__()
        self.title=title
        self.description=description
        
        if not isinstance(priority,Priority):
            raise ValueError(f"Invalid option ." )
        self.priority=priority

        if not isinstance(status,Status):
            raise ValueError(f"Invalid option." )
        self.status=status
        
        self.created_at=created_at if created_at else date.today().__str__()

 
    def __str__(self):
        return f"{self.id} | Task: {self.title} | Description: {self.description} | Priority: {self.priority.value} | Status: {self.status.value} | Date created: {self.created_at} "
