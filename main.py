from config.settings import DEFAULT_CONFIG

from workloads.cpu_bound import generate_cpu_bound
from workloads.io_bound import generate_io_bound
from workloads.memory_bound import generate_memory_bound
from workloads.mixed import generate_mixed

from engine.runner import run_benchmark
from engine.normalizer import normalize_results
from analysis.decision import select_best
from analysis.insights import generate_insights

from utils.helpers import export_to_csv


def get_user_config(workload_type):
    print("\nChoose Mode:")
    print("1. Default (quick run)")
    print("2. Custom input")

    mode = int(input("Enter choice: "))

    if mode == 1:
        return DEFAULT_CONFIG

    print("\n🔹 Recommended Parameter Guidelines:")

    if workload_type == "CPU-bound":
        print("- High burst time")
        print("- Low disk requests")
        print("- Moderate page references")

    elif workload_type == "IO-bound":
        print("- Low burst time")
        print("- High disk requests")
        print("- Moderate memory usage")

    elif workload_type == "Memory-bound":
        print("- High page reference length")
        print("- Limited frames (to induce page faults)")
        print("- Moderate CPU usage")

    elif workload_type == "Mixed":
        print("- Balanced values across CPU, memory, and disk")

    print("\nEnter your custom values:\n")

    config = {}
    config["num_processes"] = int(input("Number of processes: "))
    config["burst_min"] = int(input("Min burst time: "))
    config["burst_max"] = int(input("Max burst time: "))
    config["pages_length"] = int(input("Page reference length: "))
    config["disk_requests"] = int(input("Disk requests: "))
    config["frames"] = int(input("Number of frames: "))
    config["seed"] = None

    return config


def choose_workload():
    print("\nChoose Workload:")
    print("1. CPU-bound")
    print("2. IO-bound")
    print("3. Memory-bound")
    print("4. Mixed")

    choice = int(input("Enter choice (1-4): "))

    if choice == 1:
        return generate_cpu_bound, "CPU-bound"
    elif choice == 2:
        return generate_io_bound, "IO-bound"
    elif choice == 3:
        return generate_memory_bound, "Memory-bound"
    elif choice == 4:
        return generate_mixed, "Mixed"
    else:
        print("Invalid choice")
        exit()


def print_generated_data(data):
    print("\n🔹 Generated Workload Data")

    print("\nCPU:")
    print("Burst Time:", data["cpu"]["burst_time"])
    print("Arrival Time:", data["cpu"]["arrival_time"])
    print("Priority:", data["cpu"]["priority"])

    print("\nMemory:")
    print("Pages:", data["memory"]["pages"])
    print("Frames:", data["memory"]["frames"])

    print("\nDisk:")
    print("Queue:", data["disk"]["queue"])
    print("Head:", data["disk"]["head"])


def main():
    # Step 1: Workload
    generator, workload_type = choose_workload()

    # Step 2: Config
    config = get_user_config(workload_type)

    # Generate workload
    data = generator(**config)

    # Print generated values
    print_generated_data(data)

    # Run benchmark
    results = run_benchmark(data)
    results = normalize_results(results)

    # Decision + insights
    best = select_best(results)
    insights = generate_insights(data["type"], best)

    print("\nBest Policies:")
    for b in best:
        print(b)

    print("\nInsights:")
    for item in insights:
        print(f"\nPolicy: {item['policy']}")
        for line in item["explanation"]:
            print("-", line)

    # Export CSV for R
    export_to_csv(results)

    print("\n📁 Results exported to results.csv")
    print(" Open plots.R in RStudio to visualize the results")


if __name__ == "__main__":
    main()