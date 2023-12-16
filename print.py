indent = "\t\t\t\t"


def print_gantt_chart(processes_sequence, timeline_sequence, head_text, file):
    n = len(processes_sequence)

    file.write(
        f"\n{indent}{' ' * int((n * 5 - len(head_text)) / 2)}{head_text}\n\n"
        f"{indent}|{' -- |' * n}\n"
        f"{indent}| {'| '.join(f'{p:<3}' for p in processes_sequence)}|\n"
        f"{indent}|{' -- |' * n}\n"
        f"{indent}{''.join(f'{e:<5}' for e in timeline_sequence)}\n\n")


def print_result(completed_processes, file):
    file.write(f"{indent}{'    '.join(f'{s:<4}' for s in ['P', 'WT', 'TRT', 'RT'])}\n")

    for process in sorted(completed_processes, key=lambda x: x.name):
        file.write(
            f"{indent}{process.name:<4}\t{process.waiting_time:<4}\t{process.turnaround_time:<4}\t{process.response_time}\n")

    length = len(completed_processes)
    avg_waiting_time = sum(p.waiting_time for p in completed_processes) / length
    avg_turnaround_time = sum(p.turnaround_time for p in completed_processes) / length
    avg_response_time = sum(p.response_time for p in completed_processes) / length

    file.write(f"{indent}Avg:\t{avg_waiting_time:<4}\t{avg_turnaround_time:<4}\t{avg_response_time:<4}\n")


def print_all(completed_processes, processes_sequence, timeline_sequence, head_text, file):
    print_gantt_chart(processes_sequence, timeline_sequence, head_text, file)
    print_result(completed_processes, file)

    file.write('-' * 80)
