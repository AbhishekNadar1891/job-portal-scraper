import requests
from config import HEADERS, REQUEST_TIMEOUT


class HttpClient:

    def get(self, url):

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        return response