def fcfs_cpu(cpu_data):
    burst_time = cpu_data["burst_time"]
    arrival_time = cpu_data["arrival_time"]

    n = len(burst_time)

    waiting_time = [0] * n
    completion_time = [0] * n
    turnaround_time = [0] * n

    # First process
    completion_time[0] = arrival_time[0] + burst_time[0]
    turnaround_time[0] = completion_time[0] - arrival_time[0]
    waiting_time[0] = 0

    # Remaining processes
    for i in range(1, n):
        if completion_time[i - 1] < arrival_time[i]:
            # CPU is idle
            completion_time[i] = arrival_time[i] + burst_time[i]
        else:
            completion_time[i] = completion_time[i - 1] + burst_time[i]

        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    return {
        "waiting_times": waiting_time
    }