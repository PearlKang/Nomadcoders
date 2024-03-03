from flask import Flask, render_template, request, redirect, send_file
import jobscrapper
from file import save_to_file

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html", name="ben")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")

    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        job_scraper = jobscrapper.JobScraper(keyword)
        jobs = job_scraper.run_app()
        db[keyword] = jobs

    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")

    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")

    save_to_file(keyword, db[keyword])

    return send_file(f"{keyword}.csv", as_attachment=True)

app.run("127.0.0.1", port=8080, debug=True)