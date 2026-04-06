def fcfs_disk(disk_data):
    queue = disk_data["queue"]
    head = disk_data["head"]

    current_position = head
    total_seek_time = 0

    for request in queue:
        # Calculate movement
        movement = abs(current_position - request)
        total_seek_time += movement

        # Move head
        current_position = request

    return {
        "seek_time": total_seek_time
    }