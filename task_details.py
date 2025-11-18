tasks=[]
def add_task(tasks):
    Title=input("Enter the title of you task: ")
    Date=input("Enter due date(dd/mm/yyyy)")
    Priority=input("Enter priority level (Critical/High/Medium/Low)")

    task = {
        "Title" : Title,
        "Due" : Date if Date else "N/A",
        "Priority" : Priority,
    }

    tasks.append(task)
    print(f"Task'{Title}' added")

#check
   
add_task(tasks)
print(tasks)
