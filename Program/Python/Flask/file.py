import csv

def save_to_file(file_name, jobs):
    file = open(f"{file_name}_jobs.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(jobs_db[0].keys())

    for job in jobs_db:
        writer.writerow(job.values())

    file.close()
