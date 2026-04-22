import tkinter as tk
from tkinter import ttk, messagebox

from workloads.cpu_bound import generate_cpu_bound
from workloads.io_bound import generate_io_bound
from workloads.memory_bound import generate_memory_bound
from workloads.mixed import generate_mixed

from engine.runner import run_benchmark
from engine.normalizer import normalize_results
from analysis.decision import select_best
from analysis.insights import generate_insights

from utils.helpers import export_to_csv


WORKLOAD_MAP = {
    "CPU-bound": generate_cpu_bound,
    "IO-bound": generate_io_bound,
    "Memory-bound": generate_memory_bound,
    "Mixed": generate_mixed
}


def run_simulation():
    try:
        workload_type = workload_var.get()

        config = {
            "num_processes": int(entry_processes.get()),
            "burst_min": int(entry_burst_min.get()),
            "burst_max": int(entry_burst_max.get()),
            "pages_length": int(entry_pages.get()),
            "disk_requests": int(entry_disk.get()),
            "frames": int(entry_frames.get()),
            "seed": None
        }

        generator = WORKLOAD_MAP[workload_type]
        data = generator(**config)

        results = run_benchmark(data)
        results = normalize_results(results)

        best = select_best(results)
        insights = generate_insights(data["type"], best)

        output_text.config(state="normal")
        output_text.delete(1.0, tk.END)

        output_text.insert(tk.END, "🔹 BEST POLICIES\n\n", "heading")

        for b in best:
            output_text.insert(tk.END, str(b) + "\n", "result")

        output_text.insert(tk.END, "\n🔹 INSIGHTS\n\n", "heading")

        for item in insights:
            output_text.insert(tk.END, f"{item['policy']}\n", "subheading")
            for line in item["explanation"]:
                output_text.insert(tk.END, f"• {line}\n")
            output_text.insert(tk.END, "\n")

        output_text.config(state="disabled")

        export_to_csv(results)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- UI ---------------- #

root = tk.Tk()
root.title("OS Benchmark Framework")
root.geometry("800x700")
root.configure(bg="#f5f7fa")

# Title
tk.Label(root, text="OS Benchmark Framework",
         font=("Segoe UI", 20, "bold"),
         bg="#f5f7fa").pack(pady=10)

# Card Frame
card = tk.Frame(root, bg="white", bd=2, relief="groove")
card.pack(padx=20, pady=10, fill="x")

# Workload
tk.Label(card, text="Select Workload", font=("Segoe UI", 10, "bold"), bg="white").grid(row=0, column=0, pady=5)
workload_var = ttk.Combobox(card, values=list(WORKLOAD_MAP.keys()), state="readonly")
workload_var.current(0)
workload_var.grid(row=0, column=1, pady=5, padx=10)

# Input helper
def create_input(label, row):
    tk.Label(card, text=label, bg="white").grid(row=row, column=0, pady=5, sticky="w")
    entry = tk.Entry(card)
    entry.grid(row=row, column=1, pady=5, padx=10)
    return entry

entry_processes = create_input("Number of Processes", 1)
entry_burst_min = create_input("Min Burst Time", 2)
entry_burst_max = create_input("Max Burst Time", 3)
entry_pages = create_input("Page Reference Length", 4)
entry_disk = create_input("Disk Requests", 5)
entry_frames = create_input("Number of Frames", 6)

# Button
tk.Button(root,
          text="Run Simulation",
          command=run_simulation,
          font=("Segoe UI", 10, "bold"),
          bg="#2ecc71",
          fg="white",
          padx=20,
          pady=5).pack(pady=10)

# Output Box Frame
output_frame = tk.Frame(root)
output_frame.pack(fill="both", expand=True, padx=20, pady=10)

output_text = tk.Text(output_frame,
                      font=("Consolas", 10),
                      bg="#1e1e1e",
                      fg="white",
                      insertbackground="white")
output_text.pack(fill="both", expand=True)

# Text styling
output_text.tag_config("heading", font=("Segoe UI", 12, "bold"), foreground="#00d4ff")
output_text.tag_config("subheading", font=("Segoe UI", 10, "bold"), foreground="#00ffae")
output_text.tag_config("result", foreground="#ffd166")

output_text.config(state="disabled")

root.mainloop()