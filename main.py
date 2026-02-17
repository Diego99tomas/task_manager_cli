from services.task_manager import TaskManager
menu=TaskManager()

def show_menu():
        while True:
                try:
                    opcion = int(input(
                        "1. Add task\n"
                        "2. Show all task\n"
                        "3. Mark task completed\n"
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
                            menu.add_task(title,description,priority)
                        except ValueError:
                            print("Choose one of the option mentioned")
    
                    case 2:
                        menu.show_all_tasks()

                    case 3:
                        try:
                            pos=int(input("Enter the position of the completed task: "))
                            if pos>len(menu.list_of_tasks) or pos<=0:
                                 print("Out of range")
                            else:
                                menu.task_completed(pos) 

                        except ValueError:
                            print("Enter a number")

                    case 0:
                        print("Thanks")
                        break
show_menu()