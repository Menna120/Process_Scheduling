import subprocess
from Scheduling.fcfs import FCFS
from Scheduling.sjf import SJF
from process import Process
from Scheduling.srjf import SRJF
from print import *


def compute(func, lines, file, name):
    processes = [Process(*line.split()) for line in lines if line]
    completed_processes, process_sequence, timeline_sequence = func(processes)
    output(completed_processes, process_sequence, timeline_sequence, f"{name} Chart", file)


def main():
    lines = open("example.txt", "r").read().splitlines()
    file = open("solution.txt", "w")

    compute(FCFS, lines, file, "FCFS")
    compute(SJF, lines, file, "SJF")
    compute(SRJF, lines, file, "SRJF")

    subprocess.Popen(["notepad.exe", "solution.txt"], shell=True)


if __name__ == "__main__":
    main()
