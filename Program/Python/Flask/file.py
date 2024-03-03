import csv

def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(jobs[0].keys())

    for job in jobs:
        writer.writerow(job.values())

    file.close()

# old version
# def save_to_file(file_name, jobs):
#     file = open(f"{file_name}.csv", "w")
#     file.write("Position,Company,Location,URL\n")

#     for job in jobs:
#         file.write(f"{job['position']},{job['compony']},{job['location']},{job['link']}\n")
#         file.close()
