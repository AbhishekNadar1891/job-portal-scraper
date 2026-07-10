from bs4 import BeautifulSoup

from scraper.http_client import HttpClient
from config import MAX_PAGES

from utils.logger import get_logger

logger = get_logger(__name__)


class RemoteOKScraper:

    def __init__(self):
        self.client = HttpClient()

    def scrape(self, keyword):

        all_jobs = []

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

                    tag_elements = job.find_all("li", class_="tag-li")
                    skills = [tag.get_text(strip=True) for tag in tag_elements]

                    job_data = {
                        "title": title,
                        "company": company,
                        "experience": experience,
                        "location": location,
                        "skills": skills,
                        "link": link
                    }

                    all_jobs.append(job_data)

            except Exception:

                logger.exception(f"Failed to scrape page {page}")

                print(f"Skipping Page {page}")

                continue

        return all_jobs