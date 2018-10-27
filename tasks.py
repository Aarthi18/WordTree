from flask import Blueprint, redirect,render_template,request,url_for,Response
from abstract_cleaning import abstract_cleaning
import json



bp = Blueprint("tasks", __name__, url_prefix="/tasks")

@bp.route("/")
def index():
    phrases = abstract_cleaning("abstracts.csv", "teachers")
    return render_template("wordTree.html", phrases = phrases, keyword = 'student')