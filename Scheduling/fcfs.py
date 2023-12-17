def FCFS(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Sort the processes based on arrival time
    timeline_sequence = []

    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        timeline_sequence.append(current_time)
        process.waiting_time = current_time - process.arrival_time
        process.response_time = process.waiting_time
        current_time += process.burst_time
        process.turnaround_time = process.waiting_time + process.burst_time

    timeline_sequence.append(current_time)
    process_sequence = [p.name for p in processes]

    return processes, process_sequence, timeline_sequence
