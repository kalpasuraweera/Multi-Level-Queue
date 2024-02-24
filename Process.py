# Process Class
class Process:
    def __init__(self, burst_time):
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.remaining_time = burst_time
        self.completed = False
    
    def process_completed(self):
        self.completed = True