def sstf_disk(disk_data):
    queue = disk_data["queue"][:]
    head = disk_data["head"]

    current_position = head
    total_seek_time = 0

    # Copy queue so original isn't modified
    remaining = queue[:]

    while remaining:
        # Find closest request
        closest = remaining[0]
        min_distance = abs(current_position - closest)

        for req in remaining:
            distance = abs(current_position - req)
            if distance < min_distance:
                min_distance = distance
                closest = req

        # Move head
        total_seek_time += min_distance
        current_position = closest

        # Remove serviced request
        remaining.remove(closest)

    return {
        "seek_time": total_seek_time
    }