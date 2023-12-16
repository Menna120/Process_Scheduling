from process import Process
from srjf_schedule import SRJF
from print import *


def main():
    lines = open("example.txt", "r").read().splitlines()
    processes = [Process(*line.split()) for line in lines if line]

    completed_processes, process_sequence, timeline_sequence = SRJF(processes)

    file = open("solution.txt", "w")
    print_all(completed_processes, process_sequence, timeline_sequence, "SRJF Chart", file)


if __name__ == "__main__":
    main()
