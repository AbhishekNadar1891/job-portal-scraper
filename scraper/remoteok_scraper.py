from bs4 import BeautifulSoup

from scraper.http_client import HttpClient
from config import BASE_URL


class RemoteOKScraper:

    def __init__(self):
        self.client = HttpClient()

    def scrape(self):

        html = self.client.get(BASE_URL)

        soup = BeautifulSoup(html, "lxml")

        jobs = soup.find_all("div", class_="srp-jobtuple-wrapper")

        print(f"Jobs Found : {len(jobs)}")
        print("=" * 100)

        # This list will store every job
        all_jobs = []

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

            # Create one job record
            job_data = {
                "title": title,
                "company": company,
                "experience": experience,
                "location": location,
                "skills": skills,
                "link": link
            }

            # Store it in the list
            all_jobs.append(job_data)

        # Return the complete list of jobs
        return all_jobs