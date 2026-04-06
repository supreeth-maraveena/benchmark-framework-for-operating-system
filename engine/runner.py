from models.result import Result

# CPU algorithms
from algorithms.cpu.fcfs import fcfs_cpu
from algorithms.cpu.sjf import sjf_cpu
from algorithms.cpu.priority import priority_cpu
from algorithms.cpu.round_robin import round_robin_cpu

# Memory algorithms
from algorithms.memory.fifo import fifo_memory
from algorithms.memory.lru import lru_memory
from algorithms.memory.optimal import optimal_memory

# Disk algorithms
from algorithms.disk.fcfs import fcfs_disk
from algorithms.disk.sstf import sstf_disk
from algorithms.disk.scan import scan_disk

# Evaluator
from engine.evaluator import evaluate_cpu, evaluate_memory, evaluate_disk


def run_benchmark(workload):
    results = []

    # Algorithm mappings
    cpu_algos = {
        "FCFS": fcfs_cpu,
        "SJF": sjf_cpu,
        "PRIORITY": priority_cpu,
        "RR": round_robin_cpu
    }

    memory_algos = {
        "FIFO": fifo_memory,
        "LRU": lru_memory,
        "OPTIMAL": optimal_memory
    }

    disk_algos = {
        "FCFS": fcfs_disk,
        "SSTF": sstf_disk,
        "SCAN": scan_disk
    }

    cpu_data = workload["cpu"]
    memory_data = workload["memory"]
    disk_data = workload["disk"]

    # Iterate through combinations
    for cpu_name, cpu_func in cpu_algos.items():
        for mem_name, mem_func in memory_algos.items():
            for disk_name, disk_func in disk_algos.items():

                # Run algorithms
                if cpu_name == "RR":
                    cpu_output = cpu_func(cpu_data, quantum=4)
                else:
                    cpu_output = cpu_func(cpu_data)

                memory_output = mem_func(memory_data)
                disk_output = disk_func(disk_data)

                # Evaluate metrics
                avg_wt = evaluate_cpu(cpu_output)
                pf = evaluate_memory(memory_output)
                st = evaluate_disk(disk_output)

                # Store result
                result = Result(cpu_name, mem_name, disk_name)
                result.set_metrics(avg_wt, pf, st)

                results.append(result)

    return results