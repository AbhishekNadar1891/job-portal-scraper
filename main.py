import requests
from bs4 import BeautifulSoup


def main():
    url = "https://example.com"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        print("=" * 50)
        print("TITLE")
        print(soup.title.text)

        print("=" * 50)
        print("H1")
        print(soup.find("h1").text)

        print("=" * 50)
        print("P")
        print(soup.find("p").text)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()