from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="Sameer", age="36")


# access parameters from the URL 
@views.route("/profile")
def profile():
    args = request.args
    name = args.get("name")
    return render_template("index.html", name=name)


# return json 
@views.route("/json")
def get_json():
    return jsonify({"name": "sameer", "age": 36})


@views.route("/data")
def get_data():
    data = request.json 
    return jsonify(data) 


# redirect
@views.route("/go-to-home")
def go_home(): 
    return redirect(url_for("views.home"))