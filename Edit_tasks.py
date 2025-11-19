from task_details import tasks
from view_tasks import view

def edit(tasks):
                if not tasks:
                   print("No tasks to edit")
                   return
                
                view(tasks)

                n=input("which task do you want to edit: ")

                if not n.isdigit or n=="":
                        print("Enter a valid task number")
                        exit()

                n_int =int(n)
                if n_int<1 or n_int> len(tasks):
                        print("Task not found. Try again!")
                        exit()
                

                task=tasks[n_int-1]
                print("\nYour current task details are: \n")
                print(f"Title : '{task["Title"]}")
                print(f"Due on : '{task["Due"]}")
                print(f"Priority : '{task["Priority"]}")


                field=input("Which field do you want to edit (Title, Due, Priority): ")
                if field not in task:
                        print("Invalid Entry. Check spelling, punctuation, availability of the field and try again ")
                        exit()

                new_field=input("Enter new entry: ")
                if not new_field:
                        print(f"{field.capitalize()} can not be empty")
                        return

                old_task=task[field]
                task[field]=new_field

                print(f"Task number {n} has been updated from '{old_task}' to '{new_field}'")
#check
edit(tasks)
print("Updated task:")
view(tasks)