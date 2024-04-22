"""
Quiz
"""
from flask import Flask, render_template, request, flash, redirect, url_for, session
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route("/", methods=["POST", "GET"])
def start():
    """
    starting page
    """
    session["grade"] = 0
    session["previous"] = 0
    if request.method == "POST":
        name = request.form.get("name")
        if not name:
            flash("Enter your name")
            return render_template("start-page.html")
        return redirect(url_for("first"))
    return render_template("start-page.html")

def process_question(correct_answer):
    if request.form.get("button") == correct_answer:
        session["previous"] = session["grade"]
        session["grade"] += 1

@app.route("/question_one", methods=["POST", "GET"])
def first():
    """
    first question
    """
    process_question("correct")
    return redirect(url_for("second"))

# Routes for other questions follow a similar pattern
# Consolidate the question routes into a single function to avoid repetition

@app.route("/result", methods=["POST", "GET"])
def result():
    """
    Results page
    """
    if request.method == "POST":
        return redirect(url_for("start"))
    return render_template("result.html", grade=session["grade"])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
