from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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

                try:
                    WebDriverWait(self.driver, REQUEST_TIMEOUT).until(
                        EC.presence_of_all_elements_located(
                            (By.CLASS_NAME, "srp-jobtuple-wrapper")
                        )
                    )
                except TimeoutException:
                    logger.warning(
                        "Job cards did not appear before timeout; "
                        "returning current page source"
                    )

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
