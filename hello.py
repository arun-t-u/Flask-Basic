from flask import Flask, make_response, redirect, render_template, request, url_for, session

app = Flask(__name__)

#################################
@app.route("/hello")
def hello():
    return "Hello World!"

#################################
@app.route("/hello/<name>")
def hello_name(name):
    return "Hello %s!" %name

@app.route("/number/<int:id>")
def number_url(id):
    return "number : %d" %id

@app.route("/float_number/<float:id>")
def float_url(id):
    return "float number : %f" %id

########   URL BUILDING   #######
@app.route("/admin")
def hello_admin():
    return "Hello Admin!"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Hello %s as Guest" %guest

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guest=name))

#######    HTTP RESPONSE    ########
@app.route("/success/<name>")
def success(name):
    return "Welcome %s " %name

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("success", name=user))
    else:
        user = request.args.get("name")
        return redirect(url_for("success", name=user))

#######    FLASK TEMPLATE    ########
@app.route("/hello_page/<user>")
def hello_page(user):
    return render_template("hello.html", name=user)

#######     PASS OR FAIL      ########
@app.route("/result/<int:mark>")
def result(mark):
    return render_template("result.html", result=mark)

####  DISPLAY MARK IN DICTIONARY  #####
@app.route("/mark")
def mark():
    dict = {"physic":80, "maths": 74, "computer":82}
    return render_template("marks.html", marks=dict)

####  SENDING FORM DATA TO TEMPLATE  #####
@app.route("/student_mark")
def student_mark():
    return render_template("mark_details.html")

@app.route("/marks_display", methods=["POST", "GET"])
def marks_display():
    if request.method == "POST":
        mark = request.form
        return render_template("marks_display.html", mark=mark)

######       FLASK COOKIES      #######
@app.route("/cookies_index")
def cookies_index():
    return render_template("cookies_index.html")

@app.route("/setcookies", methods=["POST"])
def setcookies():
    if request.method == "POST":
        user = request.form["name"]
    resp = make_response(render_template("readcookie.html"))
    resp.set_cookie('userID', user)
    return resp

@app.route('/getcookies')
def get_cookies():
    name = request.cookies.get("userID")
    return "<h1>Welcome "+ name  +"</h1>"

######       FLASK SESSION     #######
@app.route('/session_demo')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
         "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"



if __name__ == "__main__":
    app.run(debug=True)