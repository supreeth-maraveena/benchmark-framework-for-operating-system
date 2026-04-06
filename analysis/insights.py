def generate_insights(workload_type, best_results):
    insights = []

    for result in best_results:
        cpu = result.cpu_algo
        memory = result.memory_algo
        disk = result.disk_algo

        explanation = []

        # ---------------- CPU Insight ----------------
        if cpu == "SJF":
            explanation.append("SJF minimizes waiting time by executing shorter jobs first.")
        elif cpu == "FCFS":
            explanation.append("FCFS processes jobs in arrival order but may lead to higher waiting time.")
        elif cpu == "PRIORITY":
            explanation.append("Priority scheduling favors high-priority processes, improving responsiveness.")
        elif cpu == "RR":
            explanation.append("Round Robin ensures fairness by sharing CPU time among processes.")

        # ---------------- Memory Insight ----------------
        if memory == "LRU":
            explanation.append("LRU reduces page faults by exploiting locality of reference.")
        elif memory == "FIFO":
            explanation.append("FIFO is simple but may replace frequently used pages.")
        elif memory == "OPTIMAL":
            explanation.append("Optimal minimizes page faults by using future knowledge.")

        # ---------------- Disk Insight ----------------
        if disk == "SSTF":
            explanation.append("SSTF reduces seek time by selecting the closest request.")
        elif disk == "FCFS":
            explanation.append("Disk FCFS is simple but results in higher head movement.")
        elif disk == "SCAN":
            explanation.append("SCAN provides balanced performance by servicing requests in a direction.")

        # ---------------- Workload Insight ----------------
        if workload_type == "CPU-bound":
            explanation.append("CPU-bound workload benefits from efficient CPU scheduling.")
        elif workload_type == "IO-bound":
            explanation.append("I/O-bound workload benefits from optimized disk scheduling.")
        elif workload_type == "Memory-bound":
            explanation.append("Memory-bound workload benefits from efficient page replacement.")
        elif workload_type == "Mixed":
            explanation.append("Mixed workload requires balanced performance across CPU, memory, and disk.")

        insights.append({
            "policy": result.get_combination_name(),
            "explanation": explanation
        })

    return insights