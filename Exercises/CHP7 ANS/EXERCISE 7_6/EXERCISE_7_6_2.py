from flask import Flask, render_template
from EXERCISE_7_6_1 import task_2

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html", ans = task_2())

if __name__ == "__main__":
    app.run(debug=True)