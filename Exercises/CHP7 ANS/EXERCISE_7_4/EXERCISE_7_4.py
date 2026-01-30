from flask import Flask, render_template 

app = Flask(__name__)

with open('people.txt') as f:
    people = [line.strip().split(',') for line in f]

@app.route("/")
def hello():
    return render_template('index.html') 
if __name__ == "__main__":
    app.run(debug=True)
