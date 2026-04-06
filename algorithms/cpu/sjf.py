def sjf_cpu(cpu_data):
    burst_time = cpu_data["burst_time"]
    arrival_time = cpu_data["arrival_time"]

    n = len(burst_time)

    # Track completed processes
    completed = [False] * n
    waiting_time = [0] * n
    completion_time = [0] * n
    turnaround_time = [0] * n

    current_time = 0
    completed_count = 0

    while completed_count < n:
        idx = -1
        min_bt = float('inf')

        # Find process with minimum burst time among arrived ones
        for i in range(n):
            if (arrival_time[i] <= current_time) and (not completed[i]):
                if burst_time[i] < min_bt:
                    min_bt = burst_time[i]
                    idx = i

        if idx == -1:
            # No process has arrived yet → move time forward
            current_time += 1
            continue

        # Execute selected process
        current_time += burst_time[idx]
        completion_time[idx] = current_time

        turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
        waiting_time[idx] = turnaround_time[idx] - burst_time[idx]

        completed[idx] = True
        completed_count += 1

    return {
        "waiting_times": waiting_time
    }