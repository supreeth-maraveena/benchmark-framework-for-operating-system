def fifo_memory(memory_data):
    pages = memory_data["pages"]
    frames_capacity = memory_data["frames"]

    frames = []
    page_faults = 0

    for page in pages:
        # Check if page already in frames (HIT)
        if page not in frames:
            page_faults += 1

            # If space available, just add
            if len(frames) < frames_capacity:
                frames.append(page)
            else:
                # Remove oldest page (FIFO)
                frames.pop(0)
                frames.append(page)

    return {
        "page_faults": page_faults
    }