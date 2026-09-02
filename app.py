"""
To-Do List Management System
-----------------------------
Backend written in a FUNCTIONAL style: each operation (insert, delete,
update, display) is a pure-ish function that takes the current task
list as input and returns a NEW task list, instead of using classes
or mutating objects.

Flask is only used as a thin web layer that calls these functions.
"""

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change-this-secret-key"  # needed for flash messages

# ---------------------------------------------------------------------
# In-memory "database". In a real functional design we'd pass this list
# around explicitly, but since Flask handles one request at a time and
# we need the data to persist between requests, we keep it as module
# level state and always replace it wholesale (never mutate in place).
# ---------------------------------------------------------------------
tasks = []          # list[dict]  e.g. {"id": 1, "title": "Buy milk"}
next_id_counter = [1]  # mutable container so functions can "increment" it


# ---------------------------------------------------------------------
# Pure(ish) functional core — no classes, each fn does ONE job
# ---------------------------------------------------------------------

def insert_task(task_list, title, next_id):
    """Return a NEW list with a new task appended."""
    new_task = {"id": next_id, "title": title.strip()}
    return task_list + [new_task], next_id + 1


def delete_task(task_list, task_id):
    """Return a NEW list with the task removed. Raises if not found."""
    if not any(t["id"] == task_id for t in task_list):
        raise ValueError(f"Task ID {task_id} does not exist.")
    return [t for t in task_list if t["id"] != task_id]


def update_task(task_list, task_id, new_title):
    """Return a NEW list with the given task's title replaced."""
    if not any(t["id"] == task_id for t in task_list):
        raise ValueError(f"Task ID {task_id} does not exist.")
    return [
        {**t, "title": new_title.strip()} if t["id"] == task_id else t
        for t in task_list
    ]


def display_tasks(task_list):
    """Return the list sorted by id — a read-only view."""
    return sorted(task_list, key=lambda t: t["id"])


def validate_task_id(raw_value, task_list):
    """Turn raw form input into a valid int task id, or raise ValueError."""
    try:
        task_id = int(raw_value)
    except (TypeError, ValueError):
        raise ValueError("Task ID must be a number.")
    if not any(t["id"] == task_id for t in task_list):
        raise ValueError(f"Task ID {task_id} does not exist.")
    return task_id


# ---------------------------------------------------------------------
# Web routes — thin glue between HTTP and the functions above
# ---------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html", tasks=display_tasks(tasks))


@app.route("/insert", methods=["POST"])
def insert():
    global tasks, next_id_counter
    title = request.form.get("title", "")
    if not title.strip():
        flash("Task title cannot be empty.", "error")
        return redirect(url_for("index"))

    tasks, new_counter = insert_task(tasks, title, next_id_counter[0])
    next_id_counter[0] = new_counter
    flash(f"Task added successfully.", "success")
    return redirect(url_for("index"))


@app.route("/delete", methods=["POST"])
def delete():
    global tasks
    if not tasks:
        flash("Task list is empty. Nothing to delete.", "error")
        return redirect(url_for("index"))
    try:
        task_id = validate_task_id(request.form.get("task_id"), tasks)
        tasks = delete_task(tasks, task_id)
        flash(f"Task {task_id} deleted successfully.", "success")
    except ValueError as e:
        flash(str(e), "error")
    return redirect(url_for("index"))


@app.route("/update", methods=["POST"])
def update():
    global tasks
    if not tasks:
        flash("Task list is empty. Nothing to update.", "error")
        return redirect(url_for("index"))
    try:
        task_id = validate_task_id(request.form.get("task_id"), tasks)
        new_title = request.form.get("new_title", "")
        if not new_title.strip():
            raise ValueError("New task title cannot be empty.")
        tasks = update_task(tasks, task_id, new_title)
        flash(f"Task {task_id} updated successfully.", "success")
    except ValueError as e:
        flash(str(e), "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
