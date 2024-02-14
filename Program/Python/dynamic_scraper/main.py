from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

def job_scraper(keyword):
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
        location = job.find("span", class_="JobCard_location__2EOr5").text
        reward = job.find("span", class_="JobCard_reward__sdyHn").text

        job = {
            "title": title,
            "company_name": company_name,
            "location": location,
            "reward": reward,
            "link": link,
        }

        jobs_db.append(job)

    return jobs_db

def create_csv(keyword):
    file = open(f"{keyword} jobs.csv", "w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(
        [
            "Title",
            "Company",
            "Location",
            "Reward",
            "Link",
        ]
    )

    jobs_db = job_scraper(keyword)

    for job in jobs_db:
        writer.writerow(job.values())

    file.close()

keywords = [
    "flutter",
    "nextjs",
    "kotlin",
    "python",
    "javascript",
]

for keyword in keywords:
    create_csv(keyword)