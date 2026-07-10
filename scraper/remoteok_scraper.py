from bs4 import BeautifulSoup

from scraper.http_client import HttpClient
from config import BASE_URL


class RemoteOKScraper:

    def __init__(self):
        self.client = HttpClient()

    def scrape(self):

        response = self.client.get(BASE_URL)

        soup = BeautifulSoup(response.text, "lxml")

        jobs = soup.find_all("tr", class_="job")

        print(f"Jobs Found : {len(jobs)}")
        print("=" * 100)

        for job in jobs:

            title = "N/A"
            company = "N/A"
            location = "Remote"

            title_tag = job.find("h2")
            if title_tag:
                title = title_tag.text.strip()

            company_tag = job.find("h3")
            if company_tag:
                company = company_tag.text.strip()

            location_tag = job.find("div", class_="location")
            if location_tag:
                location = location_tag.text.strip()

            tag_elements = job.find_all("div", class_="tag")
            tags = [tag.text.strip() for tag in tag_elements]

            print(f"Title    : {title}")
            print(f"Company  : {company}")
            print(f"Location : {location}")
            print(f"Skills   : {', '.join(tags)}")
            print("-" * 100)

        return jobs