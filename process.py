class Process:
    def __init__(self, name, burst_time, arrival_time):
        self.name = name
        self.arrival_time = int(arrival_time)
        self.burst_time = int(burst_time)
        self.remaining_time = int(burst_time)
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = -1
