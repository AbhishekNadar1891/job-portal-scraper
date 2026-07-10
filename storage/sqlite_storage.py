import sqlite3
import os

from config import OUTPUT_DIR


class SQLiteStorage:

    def save(self, jobs, database_name):

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        database_path = os.path.join(OUTPUT_DIR, database_name)

        inserted_jobs = 0

        with sqlite3.connect(database_path) as connection:

            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS jobs (

                    title TEXT,
                    company TEXT,
                    experience TEXT,
                    location TEXT,
                    skills TEXT,
                    link TEXT UNIQUE,
                    salary TEXT,
                    employment_type TEXT,
                    posted_date TEXT,
                    work_mode TEXT,
                    job_description TEXT,
                    scraped_timestamp TEXT
                )
            """)

            cursor.execute("PRAGMA table_info(jobs)")
            existing_columns = [column[1] for column in cursor.fetchall()]

            if "employment_type" not in existing_columns:
                cursor.execute(
                    "ALTER TABLE jobs "
                    "ADD COLUMN employment_type TEXT DEFAULT 'Not specified'"
                )

            for job in jobs:

                cursor.execute("""
                    INSERT OR IGNORE INTO jobs (
                        title,
                        company,
                        experience,
                        location,
                        skills,
                        link,
                        salary,
                        employment_type,
                        posted_date,
                        work_mode,
                        job_description,
                        scraped_timestamp
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (

                    job["title"],
                    job["company"],
                    job["experience"],
                    job["location"],
                    ", ".join(job["skills"]),
                    job["link"],
                    job["salary"],
                    job["employment_type"],
                    job["posted_date"],
                    job["work_mode"],
                    job["job_description"],
                    job["scraped_timestamp"]

                ))

                if cursor.rowcount == 1:
                    inserted_jobs += 1

        print(f"Inserted {inserted_jobs} new jobs into {database_path}")
