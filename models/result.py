class Result:
    def __init__(self, cpu_algo, memory_algo, disk_algo):
        # Policy combination
        self.cpu_algo = cpu_algo
        self.memory_algo = memory_algo
        self.disk_algo = disk_algo

        # Metrics
        self.avg_waiting_time = 0
        self.page_faults = 0
        self.seek_time = 0

        # Final score (after normalization)
        self.score = 0

    def set_metrics(self, wt, pf, st):
        self.avg_waiting_time = wt
        self.page_faults = pf
        self.seek_time = st

    def set_score(self, score):
        self.score = score

    def get_combination_name(self):
        return f"{self.cpu_algo} + {self.memory_algo} + {self.disk_algo}"

    def to_dict(self):
        return {
            "combination": self.get_combination_name(),
            "WT": self.avg_waiting_time,
            "PF": self.page_faults,
            "ST": self.seek_time,
            "Score": self.score
        }

    def __repr__(self):
        return (
            f"{self.get_combination_name()} | "
            f"WT: {self.avg_waiting_time}, "
            f"PF: {self.page_faults}, "
            f"ST: {self.seek_time}, "
            f"Score: {self.score}"
        )