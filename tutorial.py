from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index.html",content = [1,2,3],r="go", name="Robert")

@app.route("/admin")
def admin():
    return redirect(url_for("home", name="User!"))


if __name__ == "__main__":
    app.run()