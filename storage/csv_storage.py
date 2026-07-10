import csv
import os


class CSVStorage:

    def save(self, jobs, filename):

        os.makedirs("output", exist_ok=True)

        filepath = os.path.join("output", filename)

        with open(filepath, "w", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "title",
                    "company",
                    "experience",
                    "location",
                    "skills",
                    "link",
                    "salary",
                    "posted_date",
                    "work_mode",
                    "job_description",
                    "scraped_timestamp"
                ]
            )

            writer.writeheader()

            for job in jobs:

                writer.writerow({
                    "title": job["title"],
                    "company": job["company"],
                    "experience": job["experience"],
                    "location": job["location"],
                    "skills": ", ".join(job["skills"]),
                    "link": job["link"],
                    "salary": job["salary"],
                    "posted_date": job["posted_date"],
                    "work_mode": job["work_mode"],
                    "job_description": job["job_description"],
                    "scraped_timestamp": job["scraped_timestamp"]
                })

        print(f"\nSaved {len(jobs)} jobs to {filepath}")