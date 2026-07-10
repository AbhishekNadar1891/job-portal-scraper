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

## Output Formats

The scraper exports job listings in multiple formats:

- CSV (`output/<keyword>_jobs.csv`)
- JSON (`output/<keyword>_jobs.json`)
- Excel (`output/<keyword>_jobs.xlsx`)
- SQLite Database (`output/jobs.db`)

---

## SQLite Database

The SQLite database stores job listings while preventing duplicate entries using the job URL as a unique identifier.

Stored fields:

- Title
- Company
- Experience
- Location
- Skills
- Salary
- Posted Date
- Work Mode
- Job Description
- Job URL
- Scraped Timestamp

---

## Logging

The application logs important events including:

- Scraping progress
- Pages visited
- Number of jobs scraped
- Export status
- Errors and exceptions

Logs are stored in:

```text
scraper.log
```

---

## Future Improvements

Possible enhancements include:

- Support for additional job portals
- Concurrent scraping of job detail pages
- Configurable output formats
- Advanced filtering options
- Scheduled scraping
- Dashboard for analytics

---

## Author

**Abhishek Nadar**

GitHub: [AbhishekNadar1891](https://github.com/AbhishekNadar1891)