import random
from utils.helpers import generate_random_list

def generate_cpu_bound(num_processes=5, burst_min=20, burst_max=40,
                       pages_length=20, disk_requests=6,
                       frames=3, seed=None):

    if seed is not None:
        random.seed(seed)

    burst_time = generate_random_list(num_processes, burst_min, burst_max)
    arrival_time = list(range(num_processes))
    priority = generate_random_list(num_processes, 1, 5)

    pages = generate_random_list(pages_length, 1, 10)
    disk_queue = generate_random_list(disk_requests, 0, 199)

    return {
        "type": "CPU-bound",
        "cpu": {
            "burst_time": burst_time,
            "arrival_time": arrival_time,
            "priority": priority
        },
        "memory": {
            "pages": pages,
            "frames": frames
        },
        "disk": {
            "queue": disk_queue,
            "head": random.randint(0, 199)
        }
    }