from prettytable import PrettyTable

indent = "\t\t\t\t"

def print_gantt_chart(processes_sequence, timeline_sequence, head_text, file):
    n = len(processes_sequence)
    head_padding = ' ' * int((n * 5 - len(head_text)) / 2)
    gantt_chart = f"\n{indent}{head_padding}{head_text}\n\n"
    gantt_chart += f"{indent}|{' -- |' * n}\n"
    gantt_chart += f"{indent}| {'| '.join(f'{p:<3}' for p in processes_sequence)}|\n"
    gantt_chart += f"{indent}|{' -- |' * n}\n"
    gantt_chart += f"{indent}{''.join(f'{e:<5}' for e in timeline_sequence)}\n\n"
    file.write(gantt_chart)

def print_result(completed_processes, file):
    result = PrettyTable()
    result.field_names = ['P', 'WT', 'TRT', 'RT']
    for process in sorted(completed_processes, key=lambda x: x.name):
        result.add_row([process.name, process.waiting_time, process.turnaround_time, process.response_time])

    length = len(completed_processes)
    avg_waiting_time = sum(p.waiting_time for p in completed_processes) / length
    avg_turnaround_time = sum(p.turnaround_time for p in completed_processes) / length
    avg_response_time = sum(p.response_time for p in completed_processes) / length

    result.add_row(['------' for _ in range(len(result.field_names))])
    result.add_row(['AVG', avg_waiting_time, avg_turnaround_time, avg_response_time])

    file.write('\n'.join([indent + line for line in str(result).split('\n')]) + '\n\n')

def print_all(completed_processes, processes_sequence, timeline_sequence, head_text, file):
    print_gantt_chart(processes_sequence, timeline_sequence, head_text, file)
    print_result(completed_processes, file)
    file.write('-' * 80)