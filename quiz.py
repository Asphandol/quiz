"""
Quiz
"""
from flask import Flask, render_template, request, flash, redirect, url_for, session
import os

app = Flask(__name__)

app.secret_key = "mega_secret_key"

@app.route("/", methods=["POST", "GET"])
def start():
    """
    starting page
    """
    session["grade"] = 0
    if request.method == "POST":
        return redirect(url_for("first"))
    return render_template("start-page.html")

@app.route("/question_one", methods=["POST", "GET"])
def first():
    """
    first question
    """
    dct_quiz = {
        "name": "Яку роль відігравав Микола Ільницький у збереженні та популяризації української мови та культури?",
        "in1": "Писав вірші до гуцулів с просьбою зберегти нашу культуру",
        "in2": "Займався наверненням в католицизм",
        "in3": "Побудував стійкий політичий базис країни",
        "correct":"Був активним борцем за українську мову, виступав проти русифікації України"
    }
    if request.method == "POST":
        if request.form["button"] == dct_quiz["correct"]:
            session["grade"] = session["grade"] + 1
        return redirect(url_for("second"))
    return render_template("question.html",
                           name = dct_quiz["name"],
                           one = dct_quiz["in1"],
                           two = dct_quiz["in2"],
                           three = dct_quiz["correct"],
                           four = dct_quiz["in3"])

@app.route("/question_two", methods=["POST", "GET"])
def second():
    """
    second question
    """
    dct_quiz = {
        "name": "Які висновки робить автор щодо ролі міфів у житті міста (про міфи Львову)?",
        "in1":"Міфи - кладязбь брехні",
        "in2":"Міфи зроблені для зомбування людей",
        "in3":"Міфи - це кладязь знань до якого потрібно прислховуватись",
        "correct":"Міфи можуть як об'єднувати людей, так і роз'єднувати, тому важливо критично ставитися до них"
    }
    if request.method == "POST":
        if request.form["button"] == dct_quiz["correct"]:
            session["grade"] = session["grade"] + 1
        return redirect(url_for("third"))
    return render_template("question.html",
                           name = dct_quiz["name"],
                           one = dct_quiz["in1"],
                           two = dct_quiz["in2"],
                           three = dct_quiz["correct"],
                           four = dct_quiz["in3"])

@app.route("/question_three", methods=["POST", "GET"])
def third():
    """
    third question
    """
    dct_quiz = {
        "name": "Який вірш із збірки 'Вулиця' вважається найвідомішим?",
        "in1": "Сталінград",
        "in2": "Надвірна",
        "in3": "Харків",
        "correct": "Львів"
    }
    if request.method == "POST":
        if request.form["button"] == dct_quiz["correct"]:
            session["grade"] = session["grade"] + 1
        return redirect(url_for("fourth"))
    return render_template("question.html",
                           name = dct_quiz["name"],
                           one = dct_quiz["in1"],
                           two = dct_quiz["in2"],
                           three = dct_quiz["correct"],
                           four = dct_quiz["in3"])

@app.route("/question_four", methods=["POST", "GET"])
def fourth():
    """
    fourth question
    """
    dct_quiz = {
        "name": "Які основні теми віршів, що увійшли до збірки 'Вулиці'?",
        "in1": "Народ, повсання, пролетарії",
        "in2": "Віра, надія, сподівання",
        "in3": "Кримінал, проблематика несправедливості життя",
        "correct": "Львів, мешканці, історія"
    }
    if request.method == "POST":
        if request.form["button"] == dct_quiz["correct"]:
            session["grade"] = session["grade"] + 1
        return redirect(url_for("fifth"))
    return render_template("question.html",
                           name = dct_quiz["name"],
                           one = dct_quiz["in1"],
                           two = dct_quiz["in2"],
                           three = dct_quiz["correct"],
                           four = dct_quiz["in3"])

@app.route("/question_five", methods=["POST", "GET"])
def fifth():
    """
    fifth question
    """
    dct_quiz = {
        "name": "У якому році вийшла друком повість 'Метелики на шпильках'",
        "in1": "1903",
        "in2": "1488",
        "in3": "69",
        "correct":"1935"
    }
    if request.method == "POST":
        if request.form["button"] == dct_quiz["correct"]:
            session["grade"] = session["grade"] + 1
        return redirect(url_for("sixth"))
    return render_template("question.html",
                           name = dct_quiz["name"],
                           one = dct_quiz["in1"],
                           two = dct_quiz["in2"],
                           three = dct_quiz["correct"],
                           four = dct_quiz["in3"])

@app.route("/question_six", methods=["POST", "GET"])
def sixth():
    """
    sixth question
    """
    dct_quiz = {
        "name": "Хто така Марія з повісті 'Метелики на шпильках'?",
        "in1": "Молодий філолог, який шукає правду світу",
        "in2": "Метелик на шпильці",
        "in3": "Печево",
        "correct": "Людина, яка шукає себе та своє місце в житті"
    }
    if request.method == "POST":
        if request.form["button"] == dct_quiz["correct"]:
            session["grade"] = session["grade"] + 1
        return redirect(url_for("seventh"))
    return render_template("question.html",
                           name = dct_quiz["name"],
                           one = dct_quiz["in1"],
                           two = dct_quiz["in2"],
                           three = dct_quiz["correct"],
                           four = dct_quiz["in3"])

@app.route("/question_seven", methods=["POST", "GET"])
def seventh():
    """
    seventh question
    """
    dct_quiz = {
        "name": "Які періоди розвитку українського мистецтва виділяє Ігор Антонич в 'Національне мистецтво'",
        "in1": "Палеоліт та неоліт з детальним описом австралійських аборигенів",
        "in2": "Доба великих відкритів та ренесансу",
        "in3": "Київська Русь та Запорізька Січ",
        "correct": "Київська Русь, козацька доба, XIX століття, XX століття"
    }
    if request.method == "POST":
        if request.form["button"] == dct_quiz["correct"]:
            session["grade"] = session["grade"] + 1
        return redirect(url_for("eighth"))
    return render_template("question.html",
                           name = dct_quiz["name"],
                           one = dct_quiz["in1"],
                           two = dct_quiz["in2"],
                           three = dct_quiz["correct"],
                           four = dct_quiz["in3"])

@app.route("/question_eight", methods=["POST", "GET"])
def eighth():
    """
    eighth question
    """
    dct_quiz = {
        "name": "Якому жанру належить, 'Національне мистецтво'",
        "in1": "Детективний ліричний вірш",
        "in2": "Трагедія-бойовик",
        "in3": "Історичний роман",
        "correct": "Літературознавче дослідження"
    }
    if request.method == "POST":
        if request.form["button"] == dct_quiz["correct"]:
            session["grade"] = session["grade"] + 1
        return redirect(url_for("ninth"))
    return render_template("question.html",
                           name = dct_quiz["name"],
                           one = dct_quiz["in1"],
                           two = dct_quiz["in2"],
                           three = dct_quiz["correct"],
                           four = dct_quiz["in3"])


@app.route("/question_nine", methods=["POST", "GET"])
def ninth():
    """
    ninth question
    """
    dct_quiz = {
        "name": "Які особливості стилю Дебори Фоґель?",
        "in1": "Жорстокість з вкрапленнями боді хоррора",
        "in2": "Змішання закарпатської говірки та львівського діалекту",
        "in3": "Розпусність та старослов'янізми",
        "correct": "Ліризм, образність, філософські роздуми"
    }
    if request.method == "POST":
        if request.form["button"] == dct_quiz["correct"]:
            session["grade"] = session["grade"] + 1
        return redirect(url_for("tenth"))
    return render_template("question.html",
                           name = dct_quiz["name"],
                           one = dct_quiz["in1"],
                           two = dct_quiz["in2"],
                           three = dct_quiz["correct"],
                           four = dct_quiz["in3"])

@app.route("/question_ten", methods=["POST", "GET"])
def tenth():
    """
    tenth question
    """
    dct_quiz = {
        "name": "Хто такий Лео з роману 'Фігури днів'?",
        "in1": "Албанський кілер, який закохується в Марію",
        "in2": "Польський націоналіст, який закохується в Марію",
        "in3": "Французький будівельник, який закохується в Марію",
        "correct":"Австрійський художник, який закохується в Марію"
    }
    if request.method == "POST":
        if request.form["button"] == dct_quiz["correct"]:
            session["grade"] = session["grade"] + 1
        return redirect(url_for("eleventh"))
    return render_template("question.html",
                           name = dct_quiz["name"],
                           one = dct_quiz["in1"],
                           two = dct_quiz["in2"],
                           three = dct_quiz["correct"],
                           four = dct_quiz["in3"])

@app.route("/question_eleven", methods=["POST", "GET"])
def eleventh():
    """
    eleventh question
    """
    dct_quiz = {
        "name": "Де народився Михайло Гончар?",
        "in1": "Антициклон",
        "in2": "Буревій",
        "in3": "Альпіністи",
        "correct": "Циклон"
    }
    if request.method == "POST":
        if request.form["button"] == dct_quiz["correct"]:
            session["grade"] = session["grade"] + 1
        return redirect(url_for("twelfth"))
    return render_template("question.html",
                           name = dct_quiz["name"],
                           one = dct_quiz["in1"],
                           two = dct_quiz["in2"],
                           three = dct_quiz["correct"],
                           four = dct_quiz["in3"])

@app.route("/question_twelve", methods=["POST", "GET"])
def twelfth():
    """
    twelfth question
    """
    dct_quiz = {
        "name": "Де народився Михайло Гончар?",
        "in1": "Єрки Катеринопільського р-ну, Київської області",
        "in2": "Житомир",
        "in3": "Місто Надвірна, Івано-Франківськ",
        "correct": "Село Мар'ївка, Донецька область, Україна"
    }
    if request.method == "POST":
        if request.form["button"] == dct_quiz["correct"]:
            session["grade"] = session["grade"] + 1
        return redirect(url_for("result"))
    return render_template("question.html",
                           name = dct_quiz["name"],
                           one = dct_quiz["in1"],
                           two = dct_quiz["in2"],
                           three = dct_quiz["correct"],
                           four = dct_quiz["in3"])

@app.route("/result", methods=["POST", "GET"])
def result():
    """
    first question
    """
    if request.method == "POST":
        return redirect(url_for("start"))
    return render_template("result.html", grade = session["grade"])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
