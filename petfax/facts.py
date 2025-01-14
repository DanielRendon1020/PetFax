import json
from . import models
from flask import Blueprint, render_template, request, redirect

bp_facts = Blueprint(
    "facts",
    __name__,
    url_prefix="/facts")


@bp_facts.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # print(request.form)
        submitter = request.form["submitter"]
        fact = request.form["fact"]

        new_fact = models.Fact(submitter, fact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        return redirect('/facts')
    
    results = models.Fact.query.all()

    return render_template("facts/index.html", facts = results)


@bp_facts.route("/new")
def facts_new():
    return render_template("facts/new_facts.html")
