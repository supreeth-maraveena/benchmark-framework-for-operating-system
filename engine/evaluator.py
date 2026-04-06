def evaluate_cpu(cpu_output):
    """
    cpu_output should contain:
    {
        "waiting_times": [..]
    }
    """
    wt_list = cpu_output["waiting_times"]
    avg_wt = sum(wt_list) / len(wt_list)
    return avg_wt


def evaluate_memory(memory_output):
    """
    memory_output should contain:
    {
        "page_faults": int
    }
    """
    return memory_output["page_faults"]


def evaluate_disk(disk_output):
    """
    disk_output should contain:
    {
        "seek_time": int
    }
    """
    return disk_output["seek_time"]