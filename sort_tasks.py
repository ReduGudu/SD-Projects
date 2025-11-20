from view_tasks import view
from task_details import tasks

def sort(tasks):

                if not tasks:
                        print("No tasks to sort. Add some tasks")

                print("Tell us how you want your tasks sorted:")
                print("1. By Title")
                print("2. By Date")
                print("3. By Priority \n")


                choice= input("Enter your choice (1/2/3)")
                if not choice.isdigit or choice=="":
                        print("Not a valid choice. Check your response and try again.")
                        exit()
                choice_int=int(choice)

                if choice_int<0 or choice_int>len(tasks):
                        print("Invalid choice")
                
                if choice=="1":
                        key= "Title"
               
                elif choice=="2":
                        key="Due"

                elif choice=="3":
                        key="Priority"
                       

                tasks.sort(key= lambda task:task[key])

                print(f"Tasks sorted by '{key}'")
                view(tasks)
#check
sort(tasks)
