from flask import Flask, render_template, request
import csv

# old version
# from extractors.indeed import exxtract_indeed_jobs
# from extractors.wwr import extract_wwr_jobs

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="ben")

@app.route("/search")
def hello():
    # print(request.args)
    keyword = request.args.get("keyword")

    # old version
    # indeed = extract_indeed_jobs(keyword)
    # wwr = extract_wwr_jobs(keyword)
    # jobs = indeed + wwr
    # return render_template("search.html", keyword=keyword, jobs=jobs)

    return render_template("search.html", keyword=keyword)

app.run("127.0.0.1", port=8080, debug=True)