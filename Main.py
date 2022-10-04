import Process
import RoundRobin
import FCFS
import SPN
import SRT
import HRRN
import Feedback

with open('processes.txt') as f:
    n = int(f.readline())
    p = f.readlines()

temp = [[0, 0] for i in range(0, n)]
for i in range(n):
    temp[i][0], temp[i][1] = map(float, p[i].split(" - "))

print("Enter the id of desired scheduling algorithm")
print("FCFS:1\nRR:2\nSPN:3\nSRT:4\nHRRN:5\nFeedback queue:6")
n = int(input("(Enter the id): "))
if n == 1:
    finished_processes = FCFS.fcfs(temp)
elif n == 2:
    finished_processes = RoundRobin.roundrobin(temp)
elif n == 3:
    finished_processes = SPN.spn(temp)
elif n == 4:
    finished_processes = SRT.srt(temp)
elif n == 5:
    finished_processes = HRRN.hrrn(temp)
elif n == 6:
    finished_processes = Feedback.Feedback(temp)
# Printing information
avg_finish = 0.0
avg_ta = 0.0
avg_wait = 0.0
for p in finished_processes:
    p.printInformation()
    avg_finish += p.finish_time
    avg_ta += p.turnaround()
    avg_wait += p.turnaround() - p.ser_time
print("\nAvarage finish time: " + str(round(avg_finish / n, 3)))
print("Avarage turnaround time: " + str(round(avg_ta / n, 3)))
print("Avarage waiting time: " + str(round(avg_wait / n, 3)))
