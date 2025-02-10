from flask import Blueprint, render_template, request, redirect

todo_bp = Blueprint("todo_bp", __name__)

tasks = []

@todo_bp.route("/")
def home():
    return render_template("todo.html", tasks=tasks, edit_task=None)

@todo_bp.route("/add_task", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task and task not in tasks:
        tasks.append(task)
    return redirect("/")

@todo_bp.route("/edit_task/<task>")
def edit_task(task):
    if task in tasks:
        return render_template("todo.html", tasks=tasks, edit_task=task)
    return redirect("/")

@todo_bp.route("/update_task/<task>", methods=["POST"])
def update_task(task):
    updated_task = request.form.get("updated_task")
    if updated_task and task in tasks:
        index = tasks.index(task)
        tasks[index] = updated_task
    return redirect("/")

@todo_bp.route("/delete_task/<task>")
def delete_task(task):
    if task in tasks:
        tasks.remove(task)
    return redirect("/")

@todo_bp.route("/clear_tasks", methods=["POST"])
def clear_tasks():
    tasks.clear()
    return redirect("/")
