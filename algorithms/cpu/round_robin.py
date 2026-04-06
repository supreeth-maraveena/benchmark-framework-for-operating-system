def round_robin_cpu(cpu_data, quantum=4):
    burst_time = cpu_data["burst_time"]
    arrival_time = cpu_data["arrival_time"]

    n = len(burst_time)

    remaining_bt = burst_time[:]
    waiting_time = [0] * n
    completion_time = [0] * n

    current_time = 0
    queue = []
    visited = [False] * n

    # Add processes that arrive at time 0
    for i in range(n):
        if arrival_time[i] <= current_time:
            queue.append(i)
            visited[i] = True

    while queue:
        i = queue.pop(0)

        # Execute process for quantum or remaining time
        if remaining_bt[i] > quantum:
            current_time += quantum
            remaining_bt[i] -= quantum
        else:
            current_time += remaining_bt[i]
            remaining_bt[i] = 0
            completion_time[i] = current_time

        # Add newly arrived processes to queue
        for j in range(n):
            if (arrival_time[j] <= current_time) and (not visited[j]):
                queue.append(j)
                visited[j] = True

        # If process not finished, re-add to queue
        if remaining_bt[i] > 0:
            queue.append(i)

        # If queue empty but processes remain, jump time forward
        if not queue:
            for j in range(n):
                if not visited[j]:
                    current_time = arrival_time[j]
                    queue.append(j)
                    visited[j] = True
                    break

    # Calculate waiting time
    for i in range(n):
        turnaround_time = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time - burst_time[i]

    return {
        "waiting_times": waiting_time
    }