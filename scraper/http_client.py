from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

from config import REQUEST_TIMEOUT, MAX_RETRIES
from utils.logger import get_logger

logger = get_logger(__name__)


class HttpClient:

    def __init__(self):

        options = Options()

        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    def get(self, url):

        for attempt in range(1, MAX_RETRIES + 1):

            try:

                self.driver.get(url)

                # Allow JavaScript to render the page
                time.sleep(REQUEST_TIMEOUT)

                return self.driver.page_source

            except Exception as e:

                logger.warning(
                    f"Attempt {attempt}/{MAX_RETRIES} failed: {e}"
                )

                if attempt == MAX_RETRIES:
                    logger.exception("Maximum retry limit reached")
                    raise

                print(f"Retrying... ({attempt}/{MAX_RETRIES})")

                time.sleep(2)

    def close(self):

        self.driver.quit()