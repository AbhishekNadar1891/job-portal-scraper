import sqlite3
import os

from config import OUTPUT_DIR


class SQLiteStorage:

    def save(self, jobs, database_name):

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        database_path = os.path.join(OUTPUT_DIR, database_name)

        connection = sqlite3.connect(database_path)

        cursor = connection.cursor()

        inserted_jobs = 0

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobs (

                title TEXT,
                company TEXT,
                experience TEXT,
                location TEXT,
                skills TEXT,
                link TEXT UNIQUE,
                salary TEXT,
                posted_date TEXT,
                work_mode TEXT,
                job_description TEXT,
                scraped_timestamp TEXT
            )
        """)

        for job in jobs:

            cursor.execute("""
                INSERT OR IGNORE INTO jobs
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (

                job["title"],
                job["company"],
                job["experience"],
                job["location"],
                ", ".join(job["skills"]),
                job["link"],
                job["salary"],
                job["posted_date"],
                job["work_mode"],
                job["job_description"],
                job["scraped_timestamp"]

            ))

            if cursor.rowcount == 1:
                inserted_jobs += 1

        connection.commit()

        connection.close()

        print(f"Inserted {inserted_jobs} new jobs into {database_path}")