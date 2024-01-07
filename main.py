from flask import Flask, render_template, url_for, redirect, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "testingsecret"

@app.route("/", methods=["POST", "GET"])
def index():
    if "username" in session:
        return redirect(url_for('success'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'root':
            session['username'] = username
            return redirect(url_for('success'))
        else:
            return redirect(url_for('index'))

    return render_template("index.html")

@app.route("/success")
def success():
    value = "U sucess to log in"
    return render_template("success.html", value=value)

@app.route("/logout")
def logout():
    if "username" not in session:
        return redirect(url_for("index"))
    session.pop("username")
    return redirect(url_for('index'))

@app.route("/about")
def about():
    dataJson = [
        {"no": 1, "fruit": "apple", "animal": "lion"},
        {"no": 2, "fruit": "banana", "animal": "elephant"},
        {"no": 3, "fruit": "orange", "animal": "tiger"},
        {"no": 4, "fruit": "grape", "animal": "zebra"},
        {"no": 5, "fruit": "watermelon", "animal": "giraffe"}
    ]

    if "username" in session:
        return render_template("about.html", data=dataJson)
    else:
        return redirect(url_for('index'))

@app.route("/contact")
def contact():
    if "username" in session:
        return render_template("contact.html")
    else:
        return redirect(url_for('index'))

@app.route("/redirect-index")
def redirect_index():
    return redirect(url_for('index'))

@app.route("/redirect-about")
def redirect_about():
    return redirect(url_for('about'))

@app.route("/redirect-contact")
def redirect_contact():
    return redirect(url_for('contact'))

if __name__ == "__main__":
    app.run(debug=True, port=5003)
