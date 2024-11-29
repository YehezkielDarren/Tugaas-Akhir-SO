class SJF_Preemptive:
    def __init__(self, process):
        self.process = process
        self.length = len(process)

    def findWaitingTime(self, processes, n, wt):
        rt = [0] * n
        for i in range(n):
            rt[i] = processes[i][1]

        complete = 0
        t = 0
        minm = float('inf')
        short = -1
        check = False

        while complete != n:
            for j in range(n):
                if (processes[j][2] <= t and rt[j] < minm and rt[j] > 0):
                    minm = rt[j]
                    short = j
                    check = True

            if not check:
                t += 1
                continue

            rt[short] -= 1
            minm = rt[short]
            if minm == 0:
                minm = float('inf')

            if rt[short] == 0:
                complete += 1
                check = False
                fint = t + 1
                wt[short] = fint - processes[short][1] - processes[short][2]
                if wt[short] < 0:
                    wt[short] = 0

            t += 1

    def findTurnAroundTime(self, processes, n, wt, tat):
        for i in range(n):
            tat[i] = processes[i][1] + wt[i]

    def findavgTime(self, processes, n):
        wt = [0] * n
        tat = [0] * n
        result = []
        self.findWaitingTime(processes, n, wt)
        self.findTurnAroundTime(processes, n, wt, tat)

        total_wt = 0
        total_tat = 0
        for i in range(n):
            total_wt += wt[i]
            total_tat += tat[i]
            result.append([processes[i][0], processes[i][1], wt[i], tat[i]])

        return result, total_wt / n, total_tat / n
