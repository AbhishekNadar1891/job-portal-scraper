from scraper.naukri_scraper import NaukriScraper
from storage.csv_storage import CSVStorage
from storage.sqlite_storage import SQLiteStorage
from storage.json_storage import JSONStorage
from storage.excel_storage import ExcelStorage

from utils.logger import get_logger

logger = get_logger(__name__)


def main():

    scraper = None

    try:

        keyword = input("Enter job keyword: ").strip().lower()

        if not keyword:
            print("Keyword cannot be empty. Please enter a valid job keyword.")
            logger.warning("Scraping stopped because an empty keyword was provided")
            return

        logger.info(f"Started scraping for keyword: {keyword}")

        scraper = NaukriScraper()

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

    finally:

        if scraper is not None:

            try:
                scraper.client.close()
                logger.info("Browser closed")
            except Exception:
                logger.exception("Failed to close browser")


if __name__ == "__main__":
    main()
