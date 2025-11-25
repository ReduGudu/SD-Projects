

tasks = []


def add_task_logic(title, due_date, due_time, priority):
    task = {
        "Title": title,
        "Due_date": due_date,
        "Due_time": due_time,
        "Priority": priority,
        "Completed": False
    }
    tasks.append(task)


def edit_task_logic(index, title, due_date, due_time, priority):
    task = tasks[index]
    task["Title"] = title
    task["Due_date"] = due_date
    task["Due_time"] = due_time
    task["Priority"] = priority


def delete_task_logic(index):
    tasks.pop(index)


def mark_complete_logic(index):
    tasks[index]["Completed"] = True
