from flask import Flask, render_template, url_for, redirect, request, flash
from database import db_utils
from app import queries

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'


@app.route("/main", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home():
    """ some codes """

    return render_template("index.html")


@app.route("/rick", methods=["GET", "POST"])
def rick():
    """ some codes """
    conn = db_utils.connect_db()
    top_avg = db_utils.read_data(conn, queries.top_avg)
    worst_avg = db_utils.read_data(conn, queries.worst_avg)
    top_vote = db_utils.read_data(conn, queries.top_vote)
    worst_vote = db_utils.read_data(conn, queries.worst_vote)
    results = [top_avg, worst_avg, top_vote, worst_vote]
    # results = [top_avg, worst_avg]

    print(results)
    return render_template("rick.html", results=results)


@app.route("/general", methods=["GET", "POST"])
def general():
    conn = db_utils.connect_db()
    seven_b = db_utils.read_data(conn, queries.seven_b)
    seven_c = db_utils.read_data(conn, queries.seven_c)

    return render_template("general.html", seven_b=seven_b, seven_c=seven_c)
