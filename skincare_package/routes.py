from flask import render_template, request, redirect, url_for
from skincare_package import app, db
from skincare_package.models import Routine, Task


@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks=tasks)


@app.route("/routine")
def routine():
    routine = list(routine.query.order_by(routine.routine_name).all())
    return render_template("routine.html", routine=routine)


@app.route("/add_routine", methods=["GET", "POST"])
def add_routine():
    if request.method == "POST":
        routine = Routine(routine_name=request.form.get("routine_name"))
        db.session.add(routine)
        db.session.commit()
        return redirect(url_for("routine"))
    return render_template("add_routine.html")


