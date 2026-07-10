from scraper.remoteok_scraper import RemoteOKScraper
from storage.csv_storage import CSVStorage

from utils.logger import get_logger

logger = get_logger(__name__)


def main():

    try:

        keyword = input("Enter job keyword: ").strip().lower()

        logger.info(f"Started scraping for keyword: {keyword}")

        scraper = RemoteOKScraper()

        jobs = scraper.scrape(keyword)

        logger.info(f"Scraped {len(jobs)} jobs")

        storage = CSVStorage()

        storage.save(jobs, f"{keyword}_jobs.csv")

        logger.info("CSV exported successfully")

    except Exception:

        logger.exception("Unexpected error occurred")

        raise


if __name__ == "__main__":
    main()