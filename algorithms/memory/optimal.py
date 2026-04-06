def optimal_memory(memory_data):
    pages = memory_data["pages"]
    frames_capacity = memory_data["frames"]

    frames = []
    page_faults = 0

    for i in range(len(pages)):
        page = pages[i]

        if page not in frames:
            page_faults += 1

            if len(frames) < frames_capacity:
                frames.append(page)
            else:
                # Find page to replace
                farthest_index = -1
                page_to_replace = -1

                for f in frames:
                    if f not in pages[i + 1:]:
                        # Not used again → best to replace
                        page_to_replace = f
                        break
                    else:
                        next_use = pages[i + 1:].index(f)
                        if next_use > farthest_index:
                            farthest_index = next_use
                            page_to_replace = f

                # Replace selected page
                frames[frames.index(page_to_replace)] = page

    return {
        "page_faults": page_faults
    }