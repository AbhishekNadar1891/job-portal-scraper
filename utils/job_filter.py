class JobFilter:

    def filter_by_location(self, jobs, location):

        filtered_jobs = []

        for job in jobs:

            if location.lower() in job["location"].lower():
                filtered_jobs.append(job)

        return filtered_jobs