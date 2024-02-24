# Queue Class
class Queue:
    def __init__(self,priority):
        self.queue = []
        self.completedPrecesses = []
        self.priority = priority
    
    def enqueue(self, process):
        self.queue.append(process)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def increase_waiting_time(self, time):
        for process in self.queue:
            process.waiting_time += time
    
    def run(self, time_quantum):
        if self.priority == 0:
            #each process will get time_quantum/len(queue) time
            for process in self.queue:
                #increase every other process's waiting time by time_quantum/len(queue)
                for p in self.queue:
                    if p != process:
                        p.waiting_time += time_quantum/len(self.queue)
                #run the process for time_quantum/len(queue) time
                process.remaining_time -= time_quantum/len(self.queue)
                #if the process is completed, calculate turnaround time
                if process.remaining_time <= 0:
                    process.turnaround_time = process.waiting_time + process.burst_time
                    process.process_completed()
                    self.completedPrecesses.append(process)
                    self.queue.remove(process)
                    print(f"Process with burst time {process.burst_time} and priority {self.priority} has completed.")
                else:
                    print(f"Process with burst time {process.burst_time} and priority {self.priority} has {process.remaining_time} remaining time.")
        elif self.priority == 1 or self.priority == 2:
            #sort the queue by burst time
            self.queue.sort(key=lambda x: x.burst_time)
            #run the process with the shortest burst time and limit run time to time_quantum
            remaining_time = time_quantum
            for process in self.queue:
                if process.remaining_time <= remaining_time:
                    process.turnaround_time = process.waiting_time + process.burst_time
                    process.process_completed()
                    self.completedPrecesses.append(process)
                    self.queue.remove(process)
                    print(f"Process with burst time {process.burst_time} and priority {self.priority} has completed.")
                else:
                    process.remaining_time -= remaining_time
                    print(f"Process with burst time {process.burst_time} and priority {self.priority} has {process.remaining_time} remaining time.")
                remaining_time -= process.remaining_time
                if remaining_time <= 0:
                    break
        elif self.priority == 3:
            #run the process in the order they were added and limit run time to time_quantum
            remaining_time = time_quantum
            for process in self.queue:
                if process.remaining_time <= remaining_time:
                    process.turnaround_time = process.waiting_time + process.burst_time
                    process.process_completed()
                    self.completedPrecesses.append(process)
                    self.queue.remove(process)
                    print(f"Process with burst time {process.burst_time} and priority {self.priority} has completed.")
                else:
                    process.remaining_time -= remaining_time
                    print(f"Process with burst time {process.burst_time} and priority {self.priority} has {process.remaining_time} remaining time.")
                remaining_time -= process.remaining_time
                if remaining_time <= 0:
                    break