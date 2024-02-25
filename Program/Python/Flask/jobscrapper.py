from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

class JobScraper():
    def __init__(self, keywords):
        self.keywords = keywords

    def get_content(self, keyword):
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")

        for x in range(5):
            time.sleep(2)
            page.keyboard.down("End")
        
        content = page.content()

        p.stop()

        return content

    def get_job_lists(self, content):
        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__FqChn")
        
        jobs_db = []

        for job in jobs:
            link = f"https://www.wanted.co.kr{job.find('a')['href']}"
            title = job.find("strong", class_="JobCard_title__ddkwM").text
            company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
            reward = job.find("span", class_="JobCard_reward__sdyHn").text

            job = {
                "title": title,
                "company_name": company_name,
                "reward": reward,
                "link": link,
            }

            jobs_db.append(job)

        return jobs_db

    def create_csv(self, keyword, jobs_db):
        if len(jobs_db) <= 0:
            return

        file = open(f"{keyword}_jobs.csv", mode="w", encoding="utf-8", newline="")
        writer = csv.writer(file)
        writer.writerow(jobs_db[0].keys())

        for job in jobs_db:
            writer.writerow(job.values())

        file.close()

    def job_scraper(self, keyword):
        content = self.get_content(keyword)
        jobs_db = self.get_job_lists(content)
        return jobs_db

    def run_app(self):
        return self.job_scraper(self.keywords)
