import random
import csv

def generate_random_list(size, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(size)]


def export_to_csv(results, filename="results.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Combination", "WT", "PF", "ST", "Score"])

        for r in results:
            writer.writerow([
                r.get_combination_name(),
                r.avg_waiting_time,
                r.page_faults,
                r.seek_time,
                r.score
            ])