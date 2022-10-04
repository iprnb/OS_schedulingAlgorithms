import queue
from Process import Process

def Feedback(temp):
    def updateQueue(currentq, nextq, times):
        nonlocal i
        nonlocal elapsed_time
        while i < n and temp[i][0] <= elapsed_time:
            currentq.put(Process(temp[i][0], temp[i][1], temp[i][2]))
            i += 1
        p = currentq.get()
        print("Status: Running, Process id:" + str(p.id) + " , Time: " + str(elapsed_time))
        for x in range(int(p.updateRemainingTime(times))):

            elapsed_time += 1
            while i < n and temp[i][0] <= elapsed_time:
                q1.put(Process(temp[i][0], temp[i][1], temp[i][2]))
                i += 1
        if p.rem_time == 0:
            p.finish_time = elapsed_time
            finished_processes.append(p)
        else:
            if nextq is not None:
                nextq.put(p)
            else:
                currentq.put(p)
    n = len(temp)
    q1, q2, q3 = queue.SimpleQueue(), queue.SimpleQueue(), queue.SimpleQueue()
    t1, t2, t3 = 1, 4, 8
    i = 0 in globals()
    finished_processes = []
    elapsed_time = 0.0 in globals()

    temp = [[x[0], x[1], temp.index(x) + 1] for x in sorted(temp, key=lambda x: x[0])]

    while i < n and temp[i][0] <= elapsed_time:
        q1.put(Process(temp[i][0], temp[i][1], temp[i][2]))
        i += 1
    while i < n or not (q1.empty() and q2.empty() and q3.empty()):
        while q1.empty() and q2.empty() and q3.empty():
            print("Status: Idle, Time: " + str(elapsed_time))
            elapsed_time += 1
            while i < n and temp[i][0] <= elapsed_time:
                q1.put(Process(temp[i][0], temp[i][1], temp[i][2]))
                i += 1
        if not q1.empty():
            updateQueue(q1, q2, t1)
        elif not q2.empty():
            updateQueue(q2, q3, t2)
        elif not q3.empty():
            updateQueue(q3, None, t3)

    print("Status: All processes completed, Time: " + str(elapsed_time))
    finished_processes.sort(key=lambda x: x.id)
    return finished_processes
