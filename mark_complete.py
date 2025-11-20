from view_tasks import view
from task_details import tasks

def mark(tasks):

        if not tasks:
            print("No Tasks to mark")
            return

        for i, task in enumerate(tasks,1):
            status ="Completed" if task.get("Completed") else "Not Completed"
            print(f"{i}. {task['Title']} | {status}")


        task_number=input("Enter task number or Enter 'Quit' to quit ") 
        while True:
            if task_number=="Quit":
                confirm=input("Are you sure you want to quit?(Y/N)")
                if confirm=="Y":
                    return
                elif confirm=="N":
                     continue
            if task_number=="":
                 print("This field can not be empty")
                 continue
            break
        if task_number.isdigit and 1<=int(task_number)<=len(tasks):
             m=int(task_number)-1
             if tasks[m]["Completed"]==True:
                  print("Task  already completed\n")
                  return
             else:
                  tasks[m]["Completed"]= True
                  print(f"Task marked completed\n")
        else:
             print("Invalid input ")

#check
mark(tasks)
           
                  
             

                    
              