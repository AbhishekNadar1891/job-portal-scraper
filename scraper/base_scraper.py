from abc import ABC, abstractmethod


class BaseScraper(ABC):
    """Contract for portal scrapers that return the shared job dictionary format."""

    @abstractmethod
    def scrape(self, keyword):
        pass
