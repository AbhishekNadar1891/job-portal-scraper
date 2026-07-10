from scraper.remoteok_scraper import RemoteOKScraper
from storage.csv_storage import CSVStorage


def main():

    scraper = RemoteOKScraper()

    jobs = scraper.scrape()

    storage = CSVStorage()

    storage.save(jobs, "jobs.csv")


if __name__ == "__main__":
    main()