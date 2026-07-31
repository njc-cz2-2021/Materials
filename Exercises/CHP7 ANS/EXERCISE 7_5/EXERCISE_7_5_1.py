from flask import Flask
from flask import render_template 
from EXERCISE_7_5_2 import task2, meann, qual

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
    )   

@app.route("/round1")
def round1():
    return render_template(
        "round1.html",
        scores=task2(1)
    )

@app.route("/round2")
def round2():
    return render_template(
        "round1.html",
        scores=task2(2)
    )

@app.route("/round3")
def round3():
    return render_template(
        "round1.html",
        scores=task2(3)
    )

@app.route("/mean")
def mean():
    return render_template(
        "mean.html",
        scores=meann()
    )

@app.route("/qualifiers")
def qualifiers():
    return render_template(
        "qualifiers.html",
        scores=qual()
    )

if __name__ == "__main__":
    app.run(debug=True) 