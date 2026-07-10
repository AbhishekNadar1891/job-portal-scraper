from scraper.remoteok_scraper import RemoteOKScraper
from storage.csv_storage import CSVStorage
from storage.sqlite_storage import SQLiteStorage
from storage.json_storage import JSONStorage
from storage.excel_storage import ExcelStorage

from utils.logger import get_logger

logger = get_logger(__name__)


def main():

    try:

        keyword = input("Enter job keyword: ").strip().lower()

        logger.info(f"Started scraping for keyword: {keyword}")

        scraper = RemoteOKScraper()

        jobs = scraper.scrape(keyword)

        logger.info(f"Scraped {len(jobs)} jobs")

        csv_storage = CSVStorage()
        csv_storage.save(jobs, f"{keyword}_jobs.csv")

        logger.info("CSV exported successfully")

        sqlite_storage = SQLiteStorage()
        sqlite_storage.save(jobs, "jobs.db")

        logger.info("SQLite database updated successfully")

        json_storage = JSONStorage()
        json_storage.save(jobs, f"{keyword}_jobs.json")

        logger.info("JSON exported successfully")

        excel_storage = ExcelStorage()
        excel_storage.save(jobs, f"{keyword}_jobs.xlsx")

        logger.info("Excel exported successfully")

    except Exception:

        logger.exception("Unexpected error occurred")

        raise


if __name__ == "__main__":
    main()