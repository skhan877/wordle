from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from wordle import get_vocab, historical_answers, generate_word, check_word

views = Blueprint(__name__, "views")

@views.route("/", methods=["GET"])
def home():
    vocab = get_vocab(source="nltk")
    history = historical_answers()
    new_word = generate_word(vocab, history)
    check = check_word(new_word, history)
    return render_template("index.html",  new_word=new_word, word_status=check)

@views.route("/check", methods=["POST"])
def check():
    history = historical_answers()
    user_word = [str(w).upper() for w in request.form.values()][0]
    print(user_word)
    check = check_word(user_word, history)
    return render_template("index.html", check=check, user_word=user_word)


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
    return redirect(url_for("views.home")) # function name here 


@views.route("/call-python-function")
def call_python_function():
    my_func() 
    return 'Python func called successfully'


def my_func():
    print("function called")