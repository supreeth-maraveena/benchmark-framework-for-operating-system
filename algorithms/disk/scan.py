def scan_disk(disk_data, disk_size=200, direction="right"):
    queue = disk_data["queue"]
    head = disk_data["head"]

    requests = sorted(queue)

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    total_seek_time = 0
    current_position = head

    if direction == "right":
        # Move right first
        for req in right:
            total_seek_time += abs(current_position - req)
            current_position = req

        # Go to end of disk
        total_seek_time += abs(current_position - (disk_size - 1))
        current_position = disk_size - 1

        # Reverse direction → move left
        for req in reversed(left):
            total_seek_time += abs(current_position - req)
            current_position = req

    else:
        # Move left first
        for req in reversed(left):
            total_seek_time += abs(current_position - req)
            current_position = req

        # Go to start of disk
        total_seek_time += abs(current_position - 0)
        current_position = 0

        # Reverse direction → move right
        for req in right:
            total_seek_time += abs(current_position - req)
            current_position = req

    return {
        "seek_time": total_seek_time
    }