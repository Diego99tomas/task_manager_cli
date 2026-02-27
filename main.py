from services.task_manager import TaskManager
from storage.json_storage import Storage
from core.custom_exceptions import RangeError

storage=Storage()
task_manager=TaskManager(storage)

def print_tasks(list_tasks:list):
    for i,task in enumerate(list_tasks):
        i+=1
        print(f"{i}. {task}")


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
                            print(f"{ValueError}")
    
                    case 2:
                        show_task=task_manager.show_all_tasks()
                        if not show_task:
                            print("List task empty")
                        else:
                            print_tasks(show_task)

                    case 3:
                        try:
                            pos=int(input("Enter the position of the completed task: "))
                            task_id=task_manager.get_id(pos)
                            t=task_manager.task_completed(task_id)
                            print(t)
                            print("Task modified correctly") 
                                    
                        except ValueError:
                            print("Enter a number")
                        except RangeError as e:
                            print(f"Error: {e}") 
                            

                    case 4:
                        status=input("Enter completed or pending: ").lower().strip()
                        list_status=task_manager.filtered_task_pending_or_completed(status)
                        
                        print(f"{len(list_status)} matches found")
                        print_tasks(list_status)
                    

                    case 5:
                        summary=task_manager.general_summary()
                        print(f"Tasks completed: {summary[0]}")
                        print(f"Tasks pendig: {summary[1]}")
                        print(f"Completion rate: {summary[2]}%")


                    case 6:
                        tasks_by_priority=task_manager.tasks_for_priority()
                        print(f"High: {tasks_by_priority[0]}")
                        print(f"Medium: {tasks_by_priority[1]}")
                        print(f"Low: {tasks_by_priority[2]}")
                    
                    case 7:
                        show_tasks=task_manager.show_all_tasks()
                        if not show_tasks: print("List task empty")
                        else:
                            print_tasks(show_tasks)

                            try:
                                pos=int(input("Enter the position of the completed task: "))
                                if str(input("Sure?  s/n: ").strip().lower())=="s":
                                    task_manager.delete_task(pos)
                                    print("Task removed")

                            except ValueError:
                                print("Enter a number")
                            except RangeError as e:
                                print(f"Error: {e}") 
                            
                                
                
                    case 0:
                        print("Thanks")
                        break
show_menu()