from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time


class HttpClient:

    def __init__(self):

        options = Options()

        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    def get(self, url):

        self.driver.get(url)

        # Wait for JavaScript to fully render the page
        time.sleep(10)

        return self.driver.page_source

    def close(self):

        self.driver.quit()