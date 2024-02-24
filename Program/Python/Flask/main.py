from flask import Flask, render_template

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="ben")

@app.route("/search")
def hello():
    return render_template("search.html")

app.run("127.0.0.1", port=8080, debug=True)