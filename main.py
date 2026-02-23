from services.task_manager import TaskManager
from models.custom_exceptions import RangeError
task_manager=TaskManager()

def print_tasks(list_tasks:list):
    for i,task in enumerate(list_tasks):
        i=+1
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
                            task_manager.add_task(title,description,priority)
                            print("Task added correctly")
                        except ValueError:
                            print("Choose one of the option mentioned")
    
                    case 2:
                        show_task=task_manager.show_all_tasks()
                        if not show_task:
                            print("List task empty")
                        else:
                            for i,task in enumerate(show_task):
                                i+=1
                                print(f"{i}.{task}")

                    case 3:
                        try:
                            pos=int(input("Enter the position of the completed task: "))
                            task_manager.task_completed(pos)
                            print("Task modified correctly") 
                                    
                        except ValueError:
                            print("Enter a number")
                        except RangeError as e:
                            print(f"Error: {e}") 
                            

                    case 4:
                        status=input("Enter completed or pending: ").lower().strip()
                        list_status=task_manager.filtered_task_pending_or_completed(status)
                        
                        print(f"{len(list_status)} matches found")
                        for i,t in enumerate(list_status):
                            i+=1
                            print(f"{i}. {t}")
                    

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
                        show_task=task_manager.show_all_tasks()
                        if not show_task: print("List task empty")
                        else:
                            for i,task in enumerate(show_task):
                                i+=1
                                print(f"{i}.{task}")

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