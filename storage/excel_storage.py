import os

from openpyxl import Workbook

from config import OUTPUT_DIR


class ExcelStorage:

    def save(self, jobs, filename):

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        filepath = os.path.join(OUTPUT_DIR, filename)

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Jobs"

        sheet.append([
            "Title",
            "Company",
            "Experience",
            "Location",
            "Skills",
            "Link",
            "Scraped Timestamp"
        ])

        for job in jobs:

            sheet.append([
                job["title"],
                job["company"],
                job["experience"],
                job["location"],
                ", ".join(job["skills"]),
                job["link"],
                job["scraped_timestamp"]
            ])

        workbook.save(filepath)

        print(f"Saved {len(jobs)} jobs to {filepath}")