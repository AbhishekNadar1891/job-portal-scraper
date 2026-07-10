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
                    "scraped_timestamp": job["scraped_timestamp"]
                })

        print(f"\nSaved {len(jobs)} jobs to {filepath}")