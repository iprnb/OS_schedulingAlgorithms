import queue
from Process import Process


def fcfs(temp):
    n = len(temp)
    processes = queue.SimpleQueue()
    finished_processes = []
    elapsed_time = 0.0
    temp = [[x[0], x[1], temp.index(x) + 1] for x in sorted(temp, key=lambda x: x[0])]
    i = 0
    # Appending processes that arrived at 0 to ready queue
    while i < n and temp[i][0] <= elapsed_time:
        processes.put(Process(temp[i][0], temp[i][1], temp[i][2]))
        i += 1
    while i < n or not processes.empty():
        if processes.empty():
            while processes.empty():
                print("Status: Idle, Time: " + str(elapsed_time))
                elapsed_time += 1
                while i < n and temp[i][0] <= elapsed_time:
                    processes.put(Process(temp[i][0], temp[i][1], temp[i][2]))
                    i += 1
        p = processes.get()
        print("Status: Running, Process id:" + str(p.id) + " , Time: " + str(elapsed_time))
        for x in range(int(p.updateRemainingTime(p.rem_time))):
            while i < n and temp[i][0] <= elapsed_time:
                processes.put(Process(temp[i][0], temp[i][1], temp[i][2]))
                i += 1
            elapsed_time += 1
        while i < n and temp[i][0] <= elapsed_time:
            processes.put(Process(temp[i][0], temp[i][1], temp[i][2]))
            i += 1
        p.finish_time = elapsed_time
        finished_processes.append(p)
    print("Status: All processes completed, Time: " + str(elapsed_time))
    finished_processes.sort(key=lambda x: x.id)
    return finished_processes
