import sqlite3
import os

from config import OUTPUT_DIR


class SQLiteStorage:

    def save(self, jobs, database_name):

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        database_path = os.path.join(OUTPUT_DIR, database_name)

        connection = sqlite3.connect(database_path)

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobs (

                title TEXT,
                company TEXT,
                experience TEXT,
                location TEXT,
                skills TEXT,
                link TEXT,
                scraped_timestamp TEXT
            )
        """)

        for job in jobs:

            cursor.execute("""
                INSERT INTO jobs
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (

                job["title"],
                job["company"],
                job["experience"],
                job["location"],
                ", ".join(job["skills"]),
                job["link"],
                job["scraped_timestamp"]

            ))

        connection.commit()

        connection.close()

        print(f"Saved {len(jobs)} jobs to {database_path}")