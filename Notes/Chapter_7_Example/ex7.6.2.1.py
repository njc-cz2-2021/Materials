from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route('/notice',methods=['GET','POST'])
def notice_me():
    print(request.form)
    return render_template('notice.html',first=request.form['first_name'],last=request.form['last_name'])

if __name__ == '__main__':
    app.run(debug=True)
