import requests


def main():
    url = "https://example.com"

    try:
        response = requests.get(url, timeout=10)

        print("=" * 50)
        print(f"Status Code : {response.status_code}")
        print(f"Reason      : {response.reason}")
        print(f"URL         : {response.url}")
        print("=" * 50)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()