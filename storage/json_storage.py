import json
import os

from config import OUTPUT_DIR


class JSONStorage:

    def save(self, jobs, filename):

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        filepath = os.path.join(OUTPUT_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as file:

            json.dump(
                jobs,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"Saved {len(jobs)} jobs to {filepath}")