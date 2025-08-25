from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

path = "Materials/Exercises/resources/Task4.db"

def get_data(round_number):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT c.name AS name, s.score
        FROM competitor c
        JOIN scores s ON c.id = s.id
        WHERE s.round = ?
        ORDER BY s.score DESC;
    """, (round_number,))
    rows = cursor.fetchall()
    connection.close()
    return rows

def qualifiers():
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT 
            c.name AS competitor_name,
            SUM(s.score) AS total_score,
            CASE 
                WHEN SUM(s.score) > 250 THEN 'Qualified'
                ELSE 'Not Qualified'
            END AS qualification_status
        FROM competitor c
        JOIN scores s ON c.id = s.id
        WHERE s.round IN (1, 2, 3)
        GROUP BY c.id, c.name
        ORDER BY total_score DESC;
    """)
    rows = cursor.fetchall()
    connection.close()
    return rows

@app.route("/")
def home():
    return render_template(
        "index.html",
    )   

@app.route("/results/<int:round_number>")
def results(round_number):
    rows = get_data(round_number)
    return render_template("results.html", round_number=round_number, results=rows)

@app.route("/qualifiers")
def qualifying():
    rows = qualifiers()
    return render_template("qualifiers.html", results=rows)

if __name__ == "__main__":
    app.run(debug=True)
