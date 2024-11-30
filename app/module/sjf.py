class SJF_Preemptive:
    def __init__(self, processes):
        self.processes = processes
        self.n = len(processes)

    def findWaitingTime(self, wt):
        rt = [self.processes[i][2] for i in range(self.n)]
        complete = 0
        t = 0
        min_rt = float('inf')
        shortest = -1
        check = False

        while complete != self.n:
            for i in range(self.n):
                if self.processes[i][1] <= t and rt[i] < min_rt and rt[i] > 0:
                    min_rt = rt[i]
                    shortest = i
                    check = True

            if not check:
                t += 1
                continue

            rt[shortest] -= 1
            min_rt = rt[shortest] if rt[shortest] > 0 else float('inf')

            if rt[shortest] == 0:
                complete += 1
                check = False
                finish_time = t + 1
                wt[shortest] = finish_time - self.processes[shortest][2] - \
                    self.processes[shortest][1]
                if wt[shortest] < 0:
                    wt[shortest] = 0

            t += 1

    def findTurnAroundTime(self, wt, tat):
        for i in range(self.n):
            tat[i] = self.processes[i][2] + wt[i]

    def findAverageTime(self):
        wt = [0] * self.n
        tat = [0] * self.n
        result = []

        self.findWaitingTime(wt)
        self.findTurnAroundTime(wt, tat)

        total_wt = sum(wt)
        total_tat = sum(tat)

        for i in range(self.n):
            result.append(
                [self.processes[i][0], self.processes[i][2], wt[i], tat[i]])

        avg_wt = total_wt / self.n
        avg_tat = total_tat / self.n

        return result, avg_wt, avg_tat
