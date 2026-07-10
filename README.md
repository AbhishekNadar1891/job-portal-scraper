# Job Portal Web Scraper

A modular Python-based web scraper that extracts job listings from Naukri using Selenium and BeautifulSoup. The scraper supports multi-page scraping, multiple export formats, logging, retry mechanisms, duplicate detection, and incremental data storage using SQLite.

---

## Features

- Dynamic keyword-based job search
- Multi-page scraping
- Selenium for JavaScript-rendered pages
- BeautifulSoup (lxml parser) for HTML parsing
- CSV export
- JSON export
- Excel (.xlsx) export
- SQLite database storage
- Incremental scraping using SQLite
- Duplicate detection
- Logging
- Retry mechanism
- Exception handling
- Extracts:
  - Job Title
  - Company
  - Experience
  - Location
  - Skills
  - Salary (when available)
  - Posted Date
  - Work Mode
  - Job Description
  - Job URL
  - Scraped Timestamp

---

## Technologies Used

- Python 3.x
- Selenium
- BeautifulSoup4
- lxml
- webdriver-manager
- SQLite3
- OpenPyXL
- JSON
- CSV
- Logging
- Git & GitHub

---

## Project Structure

```text
job-portal-scraper/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── scraper/
│   ├── http_client.py
│   └── remoteok_scraper.py
│
├── storage/
│   ├── csv_storage.py
│   ├── json_storage.py
│   ├── excel_storage.py
│   └── sqlite_storage.py
│
├── utils/
│   ├── job_filter.py
│   └── logger.py
│
└── output/
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd job-portal-scraper
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Start the scraper using

```bash
python main.py
```

Enter the desired job keyword when prompted.

Example:

```text
Enter job keyword: python
```

The scraper automatically:

- Scrapes multiple pages
- Extracts job details
- Removes duplicate records
- Stores results in multiple formats

---