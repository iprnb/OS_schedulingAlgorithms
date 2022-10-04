class Process:
    def __init__(self, arr_time, rem_time, pid):
        self.arr_time = arr_time
        self.ser_time = rem_time
        self.rem_time = rem_time
        self.id = pid
        self.finish_time = 0
        self.last_run = 0

    def updateRemainingTime(self, x):
        if x < self.rem_time:
            self.rem_time -= x
            return x
        else:
            rt = self.rem_time
            self.rem_time = 0
            return rt

    def turnaround(self):
        return self.finish_time - self.arr_time

    def responseRatio(self, t):
        return ((t - self.arr_time) + self.ser_time) / self.ser_time

    def printInformation(self):
        print("\nProcess id: " + str(self.id))
        print(".\tFinish time: " + str(self.finish_time))
        print(".\tTurnaround  time: " + str(self.turnaround()))
        print(".\tWaiting time: " + str(self.turnaround() - self.ser_time))

