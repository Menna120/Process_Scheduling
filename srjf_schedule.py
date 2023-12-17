def SRJF(processes):
    current_time = 0
    completed_processes = []
    processes_sequence = []
    timeline_sequence = []

    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))

    while processes:
        available_processes = [p for p in processes if p.arrival_time <= current_time]

        if not available_processes:
            current_time += 1
            continue

        current_process = min(available_processes, key=lambda x: x.remaining_time)
        if current_process.response_time == -1:
            current_process.response_time = current_time - current_process.arrival_time

        if not processes_sequence or processes_sequence[-1] != current_process.name:
            processes_sequence.append(current_process.name)
            timeline_sequence.append(current_time)

        current_process.remaining_time -= 1
        current_time += 1

        if current_process.remaining_time == 0:
            current_process.turnaround_time = current_time - current_process.start_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed_processes.append(current_process)
            processes.remove(current_process)

    timeline_sequence.append(current_time)

    return completed_processes, processes_sequence, timeline_sequence