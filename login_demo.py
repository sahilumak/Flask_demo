from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated database for registered users
users_db = {}

@app.route("/", methods=["GET", "POST"])
def welcome():
    if request.method == "GET":
        return render_template("home.html")
    else:
        # Handle any POST data if needed
        pass

@app.route("/log", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("log.html")
    else:
        email = request.form["email"]
        password = request.form["password"]

        # Check if the user is registered
        if email in users_db and users_db[email] == password:
            return redirect(url_for("result", email=email))
        else:
            return "Invalid email or password"

@app.route("/result/<email>")
def result(email):
    return f"Your Email {email} is Successfully registered"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        key = request.form["email"]
        value = request.form["password"]

        # Check if the email is already registered
        if key in users_db:
            return "The email ID is already used"
        else:
            users_db[key] = value  # Register the new user
            return redirect(url_for("result", email=key))

if __name__ == "__main__":
    app.run(debug=True)
