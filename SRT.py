from Process import Process


def srt(temp):
    n = len(temp)
    processes = []
    finished_processes = []
    elapsed_time = 0.0
    temp = [[x[0], x[1], temp.index(x) + 1] for x in sorted(temp, key=lambda x: x[0])]
    i = 0
    # Appending processes that arrived at 0 to ready queue
    while i < n and temp[i][0] <= elapsed_time:
        processes.append(Process(temp[i][0], temp[i][1], temp[i][2]))
        print(processes)
        i += 1
    while i < n or len(processes) > 0:
        while len(processes) == 0:
            print("Status: Idle, Time: " + str(elapsed_time))
            elapsed_time += 1
            while i < n and temp[i][0] <= elapsed_time:
                processes.append(Process(temp[i][0], temp[i][1], temp[i][2]))
                i += 1
        processes.sort(key=lambda x: (x.rem_time, x.arr_time))
        p = processes.pop(0)
        print("Status: Running, Process id:" + str(p.id) + " , Time: " + str(elapsed_time))
        for _ in range(int(p.rem_time)):
            p.rem_time -= 1
            elapsed_time += 1
            min_time = p.rem_time
            while i < n and temp[i][0] <= elapsed_time:
                processes.append(Process(temp[i][0], temp[i][1], temp[i][2]))
                min_time = min(min_time, temp[i][1])
                i += 1
            if min_time < p.rem_time:
                if p.rem_time > 0:
                    processes.append(p)
                break
        if p.rem_time == 0:
            finished_processes.append(p)
            p.finish_time = elapsed_time
    print("Status: All processes completed, Time: " + str(elapsed_time))
    finished_processes.sort(key=lambda x: x.id)
    return finished_processes
