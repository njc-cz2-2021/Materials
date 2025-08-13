from flask import Flask, render_template

with open("/workspaces/Materials/Exercises/CHP7 ANS/EXERCISE 7_7/decompressedimage.txt", "r") as f:
    lines = f.readlines()
    decompressed_image = [line.strip() for line in lines]

color_map = {
    "000": "red",
    "001": "white",
    "010": "yellow",
    "011 ": "blue",
    "100": "black",
    "110": "green"
}

colors = [color_map.get(code) for code in decompressed_image]  
grid = [colors[i:i+9] for i in range(0, len(colors), 9)]

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])

def index():
    return render_template("index.html", grid=grid)

if __name__ == "__main__":
    app.run(debug=True)
