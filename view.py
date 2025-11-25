def get_color(task):
    if task["Completed"]:
        return "green"
    if task["Priority"] == "Critical":
        return "red"
    if task["Priority"] == "High":
        return "orange"
    if task["Priority"] == "Medium":
        return "gold"
    return "blue"


def view_tasks(tasks):
    
    formatted = []
    for i, task in enumerate(tasks):
        t = task.copy()
        t["index"] = i
        t["color"] = get_color(task)
        formatted.append(t)
    return formatted
