from flask import Flask, render_template, request
import jobscrapper
import csv

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="ben")

@app.route("/search")
def hello():
    keyword = request.args.get("keyword")

    job_scraper = jobscrapper.JobScraper(keyword)
    jobs = job_scraper.run_app()

    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run("127.0.0.1", port=8080, debug=True)