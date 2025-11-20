tasks=[]
def add_task(tasks):
    while True:
        while True:
            Title=input("Enter the title of you task (Enter 'Quit' to stop adding): ")
            if Title=="Quit":
                confirm=input("Are you sure you want to quit?(Y/N)")
                if confirm=="Y":
                    return
                elif confirm=="N":
                    continue
            if not Title:
                print("Title can not be empty")
                continue
            break
                        
            
        Date=input("Enter due date(dd/mm/yyyy)")
        Priority=input("Enter priority level (Critical/High/Medium/Low)")

        task = {
                "Title" : Title,
                "Due" : Date if Date else "N/A",
                "Priority" : Priority,
                "Completed" : False
            }

        tasks.append(task)
        print(f"Task'{Title}' added")
        

#check
   
add_task(tasks)
print(tasks)
