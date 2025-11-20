from task_details import tasks

def view(tasks):
    if not tasks:                                       
        print("No tasks today")
        return
    #colour codes
    Red = "\033[91m"
    Orange = "\033[38;2;255;100;0m"  
    Yellow = "\033[93m"
    Blue = "\033[94m"
    Green = "\033[92m"
    RESET = "\033[0m"

    for i,task in enumerate(tasks, start=1):
        title=task["Title"]
        due= task.get("Due", "N/A")
        priority= task.get("Priority", "Low")
        
        if priority == "Critical":
            color = Red
        elif priority == "High":
            color = Orange
        elif priority == "Medium":
            color = Yellow
        elif priority == "Low":
            color = Blue
        else:
            color = RESET

        status ="Completed" if task.get("Completed") else "Not Completed"
        if task.get("Completed"):
            color = Green

        print(f"{color}{i}.{title} |Due: {due} | Priority: {priority} | Status: {status}{RESET}" )
    
    print("----------------")
    
#check
view(tasks)




