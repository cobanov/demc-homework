from flask import Flask, render_template, url_for, redirect, request, flash
from .database.db_utils import connect_db, retrieve_data, write_data

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'


@app.route("/main", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home():
    """ some codes """

    write_data(connect_db(), "entries",)
    return render_template("index.html")


@app.route("/entries", methods=["GET", "POST"])
def entries():
    """ some codes """

    entries = retrieve_data(connect_db(), collection="entries")
    return render_template("entries.html", entries=entries)
