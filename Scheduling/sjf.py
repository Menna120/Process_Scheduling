def SJF(processes):
    current_time = 0
    completed_processes = []
    processes_sequence = []
    timeline_sequence = []

    processes.sort(key=lambda y: (y.arrival_time, y.burst_time))

    while processes:
        available_processes = [p for p in processes if p.arrival_time <= current_time]

        if not available_processes:
            current_time = processes[0].arrival_time
            continue

        current_process = min(available_processes, key=lambda x: x.burst_time)
        if current_process.response_time == -1:
            current_process.response_time = current_time - current_process.arrival_time

        processes_sequence.append(current_process.name)
        timeline_sequence.append(current_time)

        current_time += current_process.burst_time
        current_process.turnaround_time = current_time - current_process.arrival_time
        current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
        completed_processes.append(current_process)
        processes.remove(current_process)

    timeline_sequence.append(current_time)

    return completed_processes, processes_sequence, timeline_sequence
