
from Process import Process
from Queue import Queue

#time quantum for each queue
TIME_QUANTUM = 20

# main function for the program
if __name__ == "__main__":
    print("### Enter Process with Burst Time and Priority ###")
    print("""Priority Values:
        0. Round Robin (RR) - Highest Priority
        1. Shortest Job First (SJF)
        2. Shortest Job First (SJF)
        3. First-In-First-Out (FIFO) - Lowest Priority""")

    #create 4 queues for each scheduling algorithm
    queues = [Queue(0), Queue(1), Queue(2), Queue(3)]

    print("Enter the number of processes: ")
    num_processes = int(input())
    for i in range(num_processes):
        print(f"Enter the burst time for process {i+1}: ")
        burst_time = int(input())
        print(f"Enter the priority for process {i+1}: ")
        priority = int(input())
        if(priority > 3 or priority < 0):
            print("Invalid priority value. Priority value should be between 0 and 3.")
            continue
        queues[priority].enqueue(Process(burst_time))
    
    #run the scheduling algorithms until all queues are empty
    while not all(queue.is_empty() for queue in queues):
        for queue in queues:
            #increase waiting time of processes in other queues
            for other_queue in queues:
                if other_queue != queue:
                    other_queue.increase_waiting_time(TIME_QUANTUM)
            queue.run(TIME_QUANTUM)
    
    #Show Waiting Time and Turnaround Time for each process
    print("\n### Waiting Time and Turnaround Time for each Process ###")
    for queue in queues:
        for process in queue.completedPrecesses:
            print(f"Process with burst time {process.burst_time} and priority {queue.priority} has waiting time {process.waiting_time} and turnaround time {process.turnaround_time}.")
    
    #write to csv file
    with open('data.csv', 'a') as file:
        if file.tell() == 0:
            file.write("Priority, Burst Time, Priority, Waiting Time, Turnaround Time\n")
        else:
            file.write("\n")
        for queue in queues:
            for process in queue.completedPrecesses:
                file.write(f"{queue.priority}, {process.burst_time}, {queue.priority}, {process.waiting_time}, {process.turnaround_time}\n")
