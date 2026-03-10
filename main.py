from services.task_manager import TaskManager
from storage.json_storage import Storage
from core.custom_exceptions import TaskNotFoundError
from models.task import Status

storage=Storage()
task_manager=TaskManager(storage)

def print_tasks(list_tasks):
    if not list_tasks:
        print("List task empty")
        return 
    for i,task in enumerate(list_tasks):
        i+=1
        print(f"{i}. {task}")

def task_by_id(pos:int)->str:
    id_list=list(task_manager.tasks.keys())
    return id_list[pos-1]



def show_menu():
        while True:
                try:
                    opcion = int(input(
                        "1. Add task\n"
                        "2. Show all task\n"
                        "3. Mark task completed\n"
                        "4. Filterd task for status\n"
                        "5. Dashboard\n"
                        "6. Task for priority\n"
                        "7. Delete task\n"
                        "0. Salir\n"
                    ))
                except ValueError:
                    print("Opción invalida")
                    continue

                match opcion:
                    case 1:
                        try:
                            title=input("Title of task: ").strip()
                            description=input("Enter task description : ").strip()
                            priority=input("Priority: high,medium,low : ").lower().strip()
                            new_task=task_manager.add_task(title,description,priority)
                            print(new_task)
                            print("Task added correctly")
                        except ValueError:
                            print(f"Error Priority option: high, medium or low")
    
                    case 2:
                        show_task=task_manager.show_all_tasks()
                        print_tasks(show_task)

                    case 3:
                        
                        try:
                            pos=int(input("Enter the position of the completed task: "))
                            task_id=task_by_id(pos)
                            t=task_manager.task_completed(task_id)
                            print(t)
                            print("Task modified correctly") 
                                    
                        except ValueError:
                            print("Enter a number")
                        except IndexError:
                            print(f"Out of range.")
                        except TaskNotFoundError as e:
                            print(f"Error: {e} ")
                            

                    case 4:
                        status=input("Enter completed or pending: ").lower().strip()
                        
                        try:
                            list_status=task_manager.filtered_task_pending_or_completed(Status(status))
                            print(f"{len(list_status)} matches found")
                            print_tasks(list_status)
                    
                        except ValueError:
                            print(f"{status} not valid, write completed or pending")
                        except TypeError:
                            print("Not instance of Status")
                    

                    case 5:
                        summary=task_manager.general_summary()
                        print(f"Tasks completed: {summary['completed']}")
                        print(f"Tasks pending: {summary['pending']}")
                        print(f"Completion rate: {summary['rate']}%")


                    case 6:
                        tasks_by_priority=task_manager.tasks_for_priority()
                        print(f"High: {tasks_by_priority['High']}")
                        print(f"Medium: {tasks_by_priority['Medium']}")
                        print(f"Low: {tasks_by_priority['Low']}")
                    
                    case 7:
                        show_tasks=task_manager.show_all_tasks()
                        print_tasks(show_tasks)

                        try:
                            pos=int(input("Enter the position of the completed task: "))
                            id_task=task_by_id(pos)
                            if str(input("Are you sure?  s/n: ").strip().lower())=="s":
                                task_removed=task_manager.delete_task(id_task)
                                print(f"Task removed : {task_removed.title}")

                        except ValueError:
                            print("Enter a number")
                        except IndexError:
                            print(f"Out of range.")
                        except TaskNotFoundError as e:
                            print(f"Error: {e} ")
                            
                                
                
                    case 0:
                        print("Thanks")
                        break
show_menu()