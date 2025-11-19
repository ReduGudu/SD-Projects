from task_details import tasks

def view():
    if not tasks:                                       
        print("No tasks today")
        return

    for i,task in enumerate(tasks, start=1):
        title=task["Title"]
        due= task.get("Due", "N/A")
        priority= task.get("Priority", "Low")

        print(f"{i}.{title} |Due: {due} | Priority: {priority}" )

#check
view(tasks)




