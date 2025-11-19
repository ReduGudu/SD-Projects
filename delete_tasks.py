# import the function from necessary files
from view_tasks import view
from task_details import tasks
# Create a function

def delete(tasks):
# what the funtion does when target not in the list
            if not tasks:
                    print("No tasks to delete")
                    return
#show all stored tasks
#             
            view(tasks)

# what the function will do when target in  list
            n=int(input("Enter the number of the task you want to delete: "))
            if n < 0 or n > len(tasks):
                    print("Invalid task number. Try again")
                    return
            
            deleted= tasks.pop(n-1)
            print(f"Task'{deleted}'has been deleted successfully")

#Check code
delete(tasks)
print("Updated tasks:")
view(tasks)