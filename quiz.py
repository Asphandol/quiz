"""
Quiz
"""
from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)

@app.route("/")
def start():
    """
    starting page
    """
    session["grade"] = 0
    session["previous"] = 0
    if request.method == "POST":
        name = request.form["name"]
        if not name:
            flash("Enter your name")
            return render_template("start-page.html")
        return redirect(url_for("first"))
    return render_template("start-page.html")

@app.route("/question_one", methods=["POST", "GET"])
def first():
    """
    first question
    """
    session["grade"] = session["previous"]
    if request.method == "POST":
        if request.form == "":
            session["previous"] = session["grade"]
            session["grade"] = session["grade"] + 1
        return redirect(url_for("second"))
    return render_template("question_one.html")

@app.route("/question_two", methods=["POST", "GET"])
def second():
    """
    first question
    """
    session["grade"] = session["previous"]
    if request.method == "POST":
        if request.form == "":
            session["previous"] = session["grade"]
            session["grade"] = session["grade"] + 1
        return redirect(url_for("third"))
    return render_template("question_two.html")

@app.route("/question_three", methods=["POST", "GET"])
def third():
    """
    first question
    """
    session["grade"] = session["previous"]
    if request.method == "POST":
        if request.form == "":
            session["previous"] = session["grade"]
            session["grade"] = session["grade"] + 1
        return redirect(url_for("fourth"))
    return render_template("question_three.html")

@app.route("/question_four", methods=["POST", "GET"])
def fourth():
    """
    first question
    """
    session["grade"] = session["previous"]
    if request.method == "POST":
        if request.form == "":
            session["previous"] = session["grade"]
            session["grade"] = session["grade"] + 1
        return redirect(url_for("fifth"))
    return render_template("question_four.html")

@app.route("/question_five", methods=["POST", "GET"])
def fifth():
    """
    first question
    """
    session["grade"] = session["previous"]
    if request.method == "POST":
        if request.form == "":
            session["previous"] = session["grade"]
            session["grade"] = session["grade"] + 1
        return redirect(url_for("sixth"))
    return render_template("question_five.html")

@app.route("/question_six", methods=["POST", "GET"])
def sixth():
    """
    first question
    """
    session["grade"] = session["previous"]
    if request.method == "POST":
        if request.form == "":
            session["previous"] = session["grade"]
            session["grade"] = session["grade"] + 1
        return redirect(url_for("seventh"))
    return render_template("question_six.html")

@app.route("/question_seven", methods=["POST", "GET"])
def seventh():
    """
    first question
    """
    session["grade"] = session["previous"]
    if request.method == "POST":
        if request.form == "":
            session["previous"] = session["grade"]
            session["grade"] = session["grade"] + 1
        return redirect(url_for("eighth"))
    return render_template("question_seven.html")

@app.route("/question_eight", methods=["POST", "GET"])
def eighth():
    """
    first question
    """
    session["grade"] = session["previous"]
    if request.method == "POST":
        if request.form == "":
            session["previous"] = session["grade"]
            session["grade"] = session["grade"] + 1
        return redirect(url_for("ninth"))
    return render_template("question_eight.html")


@app.route("/question_nine", methods=["POST", "GET"])
def ninth():
    """
    first question
    """
    session["grade"] = session["previous"]
    if request.method == "POST":
        if request.form == "":
            session["previous"] = session["grade"]
            session["grade"] = session["grade"] + 1
        return redirect(url_for("tenth"))
    return render_template("question_nine.html")

@app.route("/question_ten", methods=["POST", "GET"])
def tenth():
    """
    first question
    """
    session["grade"] = session["previous"]
    if request.method == "POST":
        if request.form == "":
            session["previous"] = session["grade"]
            session["grade"] = session["grade"] + 1
        return redirect(url_for("result"))
    return render_template("question_ten.html")

@app.route("/result", methods=["POST", "GET"])
def result():
    """
    first question
    """
    if request.method == "POST":
        return redirect(url_for("start"))
    return render_template("question_one.html", grade = session["grade"])

if __name__ == '__main__':
    app.run(debug=True)
