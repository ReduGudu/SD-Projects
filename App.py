from flask import Flask, render_template, request, redirect, url_for, flash
from task import tasks, add_task_logic, edit_task_logic, delete_task_logic, mark_complete_logic
from view import view_tasks
from datetime import datetime

app = Flask(__name__)
app.secret_key = "x"   


# ---------- ROUTES ----------

@app.route("/")
def main_menu():
    display = view_tasks(tasks)
    return render_template("main_menu.html", tasks=display)


@app.route("/add", methods=["GET", "POST"])
def add_route():
    if request.method == "POST":
        title = request.form["title"]
        due_date = request.form["due_date"]
        due_time = request.form["due_time"]
        priority = request.form["priority"]

        
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
        today = datetime.today().date()
        if due_date_obj < today:
            flash("Due date cannot be in the past!", "error")
            return redirect(url_for("add_route"))

        add_task_logic(title, due_date, due_time, priority)
        flash("Task added successfully!", "success")
        return redirect(url_for("main_menu"))

    return render_template("add_task.html")


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_route(task_id):
    if task_id < 0 or task_id >= len(tasks):
        return redirect(url_for("main_menu"))

    task = tasks[task_id]

    if request.method == "POST":
        title = request.form["title"]
        due_date = request.form["due_date"]
        due_time = request.form["due_time"]
        priority = request.form["priority"]

        
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
        today = datetime.today().date()
        if due_date_obj < today:
            flash("Due date cannot be in the past!", "error")
            return redirect(url_for("edit_route", task_id=task_id))

        edit_task_logic(task_id, title, due_date, due_time, priority)
        flash("Task updated!", "success")
        return redirect(url_for("main_menu"))

    return render_template("edit_task.html", task=task, task_id=task_id)


@app.route("/delete/<int:task_id>")
def delete_route(task_id):
    if task_id < 0 or task_id >= len(tasks):
        return redirect(url_for("main_menu"))

    delete_task_logic(task_id)
    flash("Task deleted!", "success")
    return redirect(url_for("main_menu"))


@app.route("/mark/<int:task_id>")
def mark_route(task_id):
    if task_id < 0 or task_id >= len(tasks):
        return redirect(url_for("main_menu"))

    mark_complete_logic(task_id)
    flash("Task marked completed!", "success")
    return redirect(url_for("main_menu"))


if __name__ == "__main__":
    app.run(debug=True)
