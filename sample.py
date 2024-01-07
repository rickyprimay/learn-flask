from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "testingsecret"

@app.route("/")
def index():
    # loop
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # conditional if else
    feeling = "Sad"
    return render_template("index.html", value=days, feeling=feeling)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

# parsing value int,string
@app.route("/parsing/<string:myVal>")
def parsing(myVal):
    return "value is : {}".format(myVal)

# parsing argument
@app.route("/argument")
def argument():
    data = request.args.get("value")
    return "Value from argument parser is {}".format(data)

# login / create session
@app.route("/page/<int:value>")
def create_session(value):
    session["valueSes"] = value
    return "successful session access"

@app.route("/page/view")
def view_session():
    try:
        data = session["valueSes"]
        return "Ur Session value is : {}".format(data)
    except:
        return "u not have session value"

# logout / destroy session
@app.route("/page/logout")
def logout_session():
    session.pop("valueSes")
    return "Logout success"

if __name__ == "__main__":
    app.run(debug=True, port=5002)
