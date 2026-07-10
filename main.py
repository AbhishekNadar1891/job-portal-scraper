from scraper.remoteok_scraper import RemoteOKScraper
from storage.csv_storage import CSVStorage


def main():

    keyword = input("Enter job keyword: ").strip().lower()

    scraper = RemoteOKScraper()

    jobs = scraper.scrape(keyword)

    storage = CSVStorage()

    storage.save(jobs, f"{keyword}_jobs.csv")


if __name__ == "__main__":
    main()