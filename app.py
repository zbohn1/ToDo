import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from datetime import datetime
from helpers import apology

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True


# # Configure session to use filesystem (instead of signed cookies)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///todo.db")


@app.route("/", methods=["GET", "POST"])
def index():
    """Show to do list"""
    if request.method == "GET":

        # Get a table with the to-do item id, priority, timestamp, text, grouping, and userid for only those with a status of not yet done (i.e. "1"). Order them by category by grouping (i.e. today, this week, long-term), and then priority and then date inputted onto to-do-list.
        rows = db.execute("SELECT * FROM todo WHERE isdone = 1 ORDER BY grouping, priority, todoid")

        # If there's nothing to show from the database, then don't display a category
        if len(rows) < 1:
            return render_template("index.html", rows=rows)

        # If there is only one task to show from the database, store its grouping to be shown
        if len(rows) == 1:
            rows[0]["change"] = rows[0]["grouping"]
            return render_template("index.html", rows=rows)

        # If the number of tasks is greater than one, then the category of the first task should be stored for showing
        rows[0]["change"] = rows[0]["grouping"]

        for i in range(1, len(rows)):

            # If the grouping of the task is tomorrow and the previous task has a grouping of today, store its grouping to be shown
            if rows[i]["grouping"] == 2 and rows[i-1]["grouping"] == 1:
                rows[i]["change"] = 2

            # If the grouping of the task is long term and the previous task grouping is today, store its grouping to be shown
            elif rows[i]["grouping"] == 3 and rows[i-1]["grouping"] == 1:
                rows[i]["change"] = 3

            # If the grouping of the task is long term and the previous task grouping is tomorrow, then store its grouping to be shown
            elif rows[i]["grouping"] == 3 and rows[i-1]["grouping"] == 2:
                rows[i]["change"] = 3
            else:

                # Otherwise, store 0, which means on the front-end the grouping will not be shown
                rows[i]["change"] = 0

        return render_template("index.html", rows=rows)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "GET":

        # Get all of the tasks that are not yet completed
        rows = db.execute("SELECT * FROM todo WHERE isdone = 1 ORDER BY grouping, priority, todoid")

        # Get the todo id from the front-end
        q = request.args.get("q")
        if q:

            # Mark the task as completed
            db.execute("UPDATE todo SET isdone = 2 WHERE todoid = ?", q)
    return jsonify({"message": "okay"})


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":

        # If the category is not provided, provide apology
        if not request.form.get("category"):
            return apology("must provide a category of today, tomorrow, or long term", 400)

        # If the priority is not provided, provide apology
        if not request.form.get("priority"):
            return apology("must provide a valid priority of 1, 2, or 3", 400)

        # If the task is not provided, provide apology
        if not request.form.get("task"):
            return apology("task must not be blank", 400)

        # Initialize the appropriate category variable
        if request.form.get("category") == "Today":
            category = 1
        elif request.form.get("category") == "Tomorrow":
            category = 2
        else:
            category = 3

        # Initialize the appropriate priority, task, and time variables
        priority = request.form.get("priority")
        task = request.form.get("task")
        tasktime = datetime.now()

        # Mark the task as not yet done
        isdone = 1

        # Load the category, priority, task, time, and isdone into the database
        db.execute("INSERT INTO todo (grouping, priority, task, date, isdone) VALUES (?,?,?,?,?)",
                   category, priority, task, tasktime, isdone)
        # Get a table with the to-do item id, priority, timestamp, text, grouping, and userid for only those with a status of not yet done (i.e. "1"). Order them by category by grouping (i.e. today, this week, long-term), and then priority and then date inputted onto to-do-list.
        rows = db.execute("SELECT * FROM todo WHERE isdone = 1 ORDER BY grouping, priority, todoid")

        # If there's nothing to show from the database, then don't display a category
        if len(rows) < 1:
            return render_template("index.html", rows=rows)

        # If there is only one task to show from the database, store its grouping to be shown
        if len(rows) == 1:
            rows[0]["change"] = rows[0]["grouping"]
            return render_template("index.html", rows=rows)

        # If the number of tasks is greater than one, then the category of the first task should be stored for showing
        rows[0]["change"] = rows[0]["grouping"]

        for i in range(1, len(rows)):

            # If the grouping of the task is tomorrow and the previous task has a grouping of today, store its grouping to be shown
            if rows[i]["grouping"] == 2 and rows[i-1]["grouping"] == 1:
                rows[i]["change"] = 2

            # If the grouping of the task is long term and the previous task grouping is today, store its grouping to be shown
            elif rows[i]["grouping"] == 3 and rows[i-1]["grouping"] == 1:
                rows[i]["change"] = 3

            # If the grouping of the task is long term and the previous task grouping is tomorrow, then store its grouping to be shown
            elif rows[i]["grouping"] == 3 and rows[i-1]["grouping"] == 2:
                rows[i]["change"] = 3
            else:

                # Otherwise, store 0, which means on the front-end the grouping will not be shown
                rows[i]["change"] = 0

        return render_template("index.html", rows=rows)

    if request.method == "GET":
        rows = db.execute("SELECT * FROM todo WHERE isdone = 1 ORDER BY grouping, priority, todoid")

        # If there's nothing to show from the database, then don't display a category
        if len(rows) < 1:
            return render_template("index.html", rows=rows)

        # If there is only one task to show from the database, store its grouping to be shown
        if len(rows) == 1:
            rows[0]["change"] = rows[0]["grouping"]
            return render_template("index.html", rows=rows)

        # If the number of tasks is greater than one, then the category of the first task should be stored for showing
        rows[0]["change"] = rows[0]["grouping"]

        for i in range(1, len(rows)):

            # If the grouping of the task is tomorrow and the previous task has a grouping of today, store its grouping to be shown
            if rows[i]["grouping"] == 2 and rows[i-1]["grouping"] == 1:
                rows[i]["change"] = 2

            # If the grouping of the task is long term and the previous task grouping is today, store its grouping to be shown
            elif rows[i]["grouping"] == 3 and rows[i-1]["grouping"] == 1:
                rows[i]["change"] = 3

            # If the grouping of the task is long term and the previous task grouping is tomorrow, then store its grouping to be shown
            elif rows[i]["grouping"] == 3 and rows[i-1]["grouping"] == 2:
                rows[i]["change"] = 3
            else:

                # Otherwise, store 0, which means on the front-end the grouping will not be shown
                rows[i]["change"] = 0
        return render_template("index.html", rows=rows)


@app.route("/completed", methods=["GET", "POST"])
def completed():
    if request.method == "GET":

        # Return all of the completed tasks
        rows = db.execute("SELECT * FROM todo WHERE isdone = 2 ORDER BY todoid DESC")
        return render_template("completed.html", rows=rows)
