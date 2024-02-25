from flask import Flask, render_template, request
# import jobscrapper
# import csv

from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
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


    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")

    for x in range(5):
        time.sleep(2)
        page.keyboard.down("End")
    
    content = page.content()

    p.stop()


    soup = BeautifulSoup(content, "html.parser")
    jobs = soup.find_all("div", class_="JobCard_container__FqChn")
    
    jobs_db = []

    for job in jobs:
        link = f"https://www.wanted.co.kr{job.find('a')['href']}"
        title = job.find("strong", class_="JobCard_title__ddkwM").text
        company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
        # location = job.find("span", class_="JobCard_location__2EOr5").text
        reward = job.find("span", class_="JobCard_reward__sdyHn").text

        job = {
            "title": title,
            "company_name": company_name,
            # "location": location,
            "reward": reward,
            "link": link,
        }

        jobs_db.append(job)

    # print(jobs_db)




    # job_scraper = jobscrapper.JobScraper(keyword)
    # jobs = job_scraper.run_app()
    # print(job_scraper.run_app())

    # old version
    # indeed = extract_indeed_jobs(keyword)
    # wwr = extract_wwr_jobs(keyword)
    # jobs = indeed + wwr
    # return render_template("search.html", keyword=keyword, jobs=jobs)

    # return render_template("search.html", keyword=keyword)
    return render_template("search.html", keyword=keyword, jobs=jobs_db)

app.run("127.0.0.1", port=8080, debug=True)