
import json
from models.task import Task

class TaskManager:
    NAME_STORAGE="storage/json_storage.json"

    def __init__(self):
       self.list_of_tasks=[]
       self.loading_tasks()
    
    def loading_tasks(self):
        try:
            with open(self.NAME_STORAGE,"r") as loading_task:
                tasks=json.load(loading_task) 
                self.list_of_tasks=[Task.from_dict(t) for t in tasks]
                print("Loading tasks correctly")
        except FileNotFoundError:
            self.list_of_tasks=[]
            print("The file was not found, a new one is being created")


    def add_task(self):
        try:
            title=input("Title of task: ").strip()
            description=input("Enter task description : ").strip()
            priority=input("Priority: high,medium,low : ").lower().strip()

            new_task=Task(title,description,priority)
            self.list_of_tasks.append(new_task)

            with open(self.NAME_STORAGE,"w") as add_task:
                json.dump([task.to_dict() for task in self.list_of_tasks],
                          add_task,indent=4)
                print("Task added correctly")
        
        except ValueError:
            print("Choose one of the option mentioned")
           
    def show_all_tasks(self):
        if not self.list_of_tasks:
            print("There are no tasks")
            return
        for i,task in enumerate(self.list_of_tasks):
            i+=1
            print(f"{i}. ",task)

    
    def show_menu(self):
        while True:
                try:
                    opcion = int(input(
                        "1. Add task\n"
                        "2. Show all task\n"
                        "0. Salir\n"
                    ))
                except ValueError:
                    print("Opción invalida")
                    continue

                match opcion:
                    case 1:
                        self.add_task()
                    case 2:
                        self.show_all_tasks()
                    case 0:
                        print("Thanks")
                        break

        


