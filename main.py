from services.task_manager import TaskManager
task_manager=TaskManager()

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
                            verification=task_manager.add_task(title,description,priority)
                            if verification:
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
                            if pos>len(task_manager.list_of_tasks) or pos<=0:
                                print("Out of range")
                            
                            else:
                                task_manager.task_completed(pos)
                                print("Task modified correctly") 
                                    
                        except ValueError:
                            print("Enter a number")

                    case 4:
                        status=input("Enter completed or pending: ").lower().strip()
                        list_status=task_manager.filtered_task_pending_or_completed(status)
                        
                        print(f"{len(list_status)} matches found")
                        for t in list_status:
                            print(t)
                    

                    case 5:
                        if not task_manager.list_of_tasks:
                           print("There are no tasks.") 
                        else:
                            summary=task_manager.general_summary()
                            print(f"Tasks completed: {summary[0]}")
                            print(f"Tasks pendig: {summary[1]}")
                            print(f"Completion rate: {summary[2]}%")

                    case 6:
                        tasks_by_priority=task_manager.tasks_for_priority()
                        print(f"High: {tasks_by_priority[0]}")
                        print(f"Medium: {tasks_by_priority[1]}")
                        print(f"Low: {tasks_by_priority[2]}")         
                
                    case 0:
                        print("Thanks")
                        break
show_menu()