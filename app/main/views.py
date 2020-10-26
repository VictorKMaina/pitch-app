from flask import render_template, request, redirect, url_for, abort
from . import main

@main.route("/")
def index():
    """
    View function that returns root page
    """
    return render_template("index.html")