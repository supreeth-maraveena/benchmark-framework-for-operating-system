def lru_memory(memory_data):
    pages = memory_data["pages"]
    frames_capacity = memory_data["frames"]

    frames = []
    page_faults = 0

    for page in pages:
        if page in frames:
            # Move page to most recently used (end)
            frames.remove(page)
            frames.append(page)
        else:
            page_faults += 1

            if len(frames) < frames_capacity:
                frames.append(page)
            else:
                # Remove least recently used (front)
                frames.pop(0)
                frames.append(page)

    return {
        "page_faults": page_faults
    }