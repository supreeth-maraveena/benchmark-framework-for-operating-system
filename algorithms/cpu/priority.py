def priority_cpu(cpu_data):
    burst_time = cpu_data["burst_time"]
    arrival_time = cpu_data["arrival_time"]
    priority = cpu_data["priority"]

    n = len(burst_time)

    completed = [False] * n
    waiting_time = [0] * n
    completion_time = [0] * n
    turnaround_time = [0] * n

    current_time = 0
    completed_count = 0

    while completed_count < n:
        idx = -1
        best_pr = float('inf')  # lower is better

        # pick highest priority among arrived
        for i in range(n):
            if (arrival_time[i] <= current_time) and (not completed[i]):
                if priority[i] < best_pr:
                    best_pr = priority[i]
                    idx = i
                elif priority[i] == best_pr:
                    # tie-break: earlier arrival
                    if idx == -1 or arrival_time[i] < arrival_time[idx]:
                        idx = i

        if idx == -1:
            # CPU idle
            current_time += 1
            continue

        # execute selected process
        current_time += burst_time[idx]
        completion_time[idx] = current_time

        turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
        waiting_time[idx] = turnaround_time[idx] - burst_time[idx]

        completed[idx] = True
        completed_count += 1

    return {
        "waiting_times": waiting_time
    }