from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)

@app.route("/") #decorator function
def root():
    return render_template("form1.html")

@app.route("/submit",methods=["POST",'GET'])
# def calculate():
#     output= 'Hello Worlds'
#     return output

def calculate(): #remember that form method has to be POST before it gets processed
    print(request.form)
    output= f"Hello, {request.form['Name']}. Your email address is {request.form['Email']}"
    return output

app.run()
