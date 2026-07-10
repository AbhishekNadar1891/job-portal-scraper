from bs4 import BeautifulSoup
from datetime import datetime

from scraper.http_client import HttpClient
from config import MAX_PAGES

from utils.logger import get_logger

logger = get_logger(__name__)


class NaukriScraper:

    def __init__(self):
        self.client = HttpClient()

    def scrape(self, keyword):

        all_jobs = []
        seen_links = set()

        scraped_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Build the search URL dynamically
        base_url = f"https://www.naukri.com/{keyword}-jobs?k={keyword}"

        for page in range(1, MAX_PAGES + 1):

            try:

                if page == 1:
                    url = base_url
                else:
                    url = base_url.replace(
                        f"{keyword}-jobs",
                        f"{keyword}-jobs-{page}"
                    )

                print(f"\nScraping Page {page}")
                print(url)

                logger.info(f"Scraping page {page}")
                logger.info(f"URL: {url}")

                html = self.client.get(url)

                soup = BeautifulSoup(html, "lxml")

                jobs = soup.find_all("div", class_="srp-jobtuple-wrapper")

                print(f"Jobs Found : {len(jobs)}")
                print("=" * 100)

                logger.info(f"Page {page}: {len(jobs)} jobs found")

                for job in jobs:

                    title = "N/A"
                    company = "N/A"
                    experience = "N/A"
                    location = "N/A"
                    link = "N/A"
                    skills = []

                    salary = "N/A"
                    posted_date = "N/A"
                    work_mode = "N/A"
                    job_description = "N/A"

                    title_tag = job.find("a", class_="title")
                    if title_tag:
                        title = title_tag.get_text(strip=True)
                        link = title_tag.get("href")

                    company_tag = job.find("a", class_="comp-name")
                    if company_tag:
                        company = company_tag.get_text(strip=True)

                    exp_tag = job.find("span", class_="expwdth")
                    if exp_tag:
                        experience = exp_tag.get_text(strip=True)

                    location_tag = job.find("span", class_="locWdth")
                    if location_tag:
                        location = location_tag.get_text(strip=True)

                    # Salary
                    salary_wrap = job.find("span", class_="sal-wrap")
                    if salary_wrap:
                        salary_text = salary_wrap.find("span", title=True)
                        if salary_text:
                            salary = salary_text.get_text(strip=True)

                    posted_date_tag = job.find("span", class_="job-post-day")
                    if posted_date_tag:
                        posted_date = posted_date_tag.get_text(strip=True)

                    tag_elements = job.find_all("li", class_="tag-li")
                    skills = [tag.get_text(strip=True) for tag in tag_elements]

                    description_tag = job.find("span", class_="job-desc")
                    if description_tag:
                        job_description = description_tag.get_text(strip=True)

                    work_mode_tag = job.find("div", class_="jobType")
                    if work_mode_tag:
                        work_mode = work_mode_tag.get_text(strip=True)

                    # Skip duplicate job postings
                    if link in seen_links:
                        continue

                    seen_links.add(link)

                    job_data = {
                        "title": title,
                        "company": company,
                        "experience": experience,
                        "location": location,
                        "skills": skills,
                        "link": link,
                        "salary": salary,
                        "posted_date": posted_date,
                        "work_mode": work_mode,
                        "job_description": job_description,
                        "scraped_timestamp": scraped_timestamp
                    }

                    all_jobs.append(job_data)

            except Exception:

                logger.exception(f"Failed to scrape page {page}")

                print(f"Skipping Page {page}")

                continue

        return all_jobs