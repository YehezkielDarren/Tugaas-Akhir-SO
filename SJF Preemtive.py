import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

class SFJPreemtive:

    def __init__(self, processes):
        self.processes = processes
        self.length = len(processes)

    def findWaitingTime(self, processes, n, wt):
        rt = [0] * n

        for i in range(n):
            rt[i] = processes[i][2]
        t = 0
        minm = 999999999
        short = 0
        check = False
        complete = 0

        while (complete != n):
            for j in range(n):
                if ((processes[j][1] <= t) and
                        (rt[j] < minm) and rt[j] > 0):
                    minm = rt[j]
                    short = j
                    check = True
            if (check == False):
                t += 1
                continue

            rt[short] -= 1
            minm = rt[short]
            if (minm == 0):
                minm = 999999999

            if (rt[short] == 0):
                complete += 1
                check = False
                fint = t + 1
                wt[short] = (fint - processes[short][1])

                if (wt[short] < 0):
                    wt[short] = 0

            t += 1

    def findTurnAroundTime(self, processes, n, wt, tat):
        for i in range(n):
            tat[i] = wt[i] - processes[i][2]

    def findavgTime(self, processes, n):
        wt = [0] * n
        tat = [0] * n
        akhir = list()

        self.findWaitingTime(processes, n, wt)
        self.findTurnAroundTime(processes, n, wt, tat)

        total_wt = 0
        total_tat = 0
        for i in range(n):
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]
            akhir.append([processes[i][0], processes[i][2], tat[i], wt[i]])

        AWT = total_wt / n
        ATAT = total_tat / n
        return akhir, AWT, ATAT

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

class CustomInputDialog(simpledialog.Dialog):
    def __init__(self, parent, title, prompt):
        self.prompt = prompt
        super().__init__(parent, title=title)

    def body(self, parent):
        tk.Label(parent, text=self.prompt).grid(row=0, column=0)
        self.entry = tk.Entry(parent, width=30)
        self.entry.grid(row=0, column=1)
        return self.entry

    def apply(self):
        self.result = self.entry.get()

class ProgramSJFPreemtive:

    def __init__(self, root):
        self.root = root
        self.root.title("Program Penghitung SJF Preemtive")
        self.processes = []
        self.create_widgets()

    def create_widgets(self):
        self.jumlahproses = tk.IntVar(value=3)
        ttk.Label(self.root, text="Silahkan Masukan Jumlah Proses:").grid(row=1, column=0, padx=5, pady=10, sticky=tk.W)
        ttk.Spinbox(self.root, from_=1, to=10, textvariable=self.jumlahproses).grid(row=1, column=1, padx=5, pady=15, sticky=tk.W)

        ttk.Button(self.root, text="MULAI", command=self.run_simulation).grid(row=1, column=1, columnspan=2, padx=200, pady=10)

        self.result_text = tk.Text(self.root, height=30, width=60)
        font = self.result_text.cget("font")
        font_family, _, _ = font.partition(" ")
        new_font = (font_family, 12)
        self.result_text.configure(font=new_font)
        self.result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        result_str = "\nArrival Time => Waktu kedatangan proses\n\nBurst Time => Waktu yang dibutuhkan untuk menyelesaikan proses\n\n"
        self.result_text.insert(tk.END, result_str)

    def run_simulation(self):
        self.processes = []
        num_processes = self.jumlahproses.get()
        jalan = True

        for i in range(num_processes):
            arrival_time = (CustomInputDialog(root,title=(f"Arrival Time Proses {i + 1}"),prompt="Masukan Arrival Time :").result)
            try:
                arrival_time = int(arrival_time)
                burst_time = (CustomInputDialog(root,title=(f"Burst Time Proses {i + 1}"),prompt="Masukan Burst Time :").result)
                try:
                    burst_time = int(burst_time)
                    self.processes.append([i + 1, arrival_time, burst_time])
                except:
                    jalan = False
                    break
            except:
                jalan = False
                break
        if jalan:
            sfj = SFJPreemtive(self.processes)
            akhir, AWT, ATA = sfj.findavgTime(self.processes, num_processes)

            result_str = "\nHASIL PERHITUNGAN\n\n"
            result_str += "Processes\t     Burst Time\t  Waiting Time\t   Turn-Around Time\n\n"
            for i in akhir:
                result_str += f"    P{i[0]}\t\t{i[1]}\t  {i[2]}\t\t{i[3]}\n"
            result_str += "\n"
            result_str += f"\nAverage Waiting Time: {AWT:.2f}"
            result_str += f"\nAverage Turn Around Time: {ATA:.2f}"

            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result_str)
            self.result_text.config(state=tk.DISABLED)
        else:
            result_str = "\nPROGRAM TELAH DIHENTIKAN ATAU TERJADI KESALAHAN INPUT\n\n"
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result_str)
            self.result_text.config(state=tk.DISABLED)


root = tk.Tk()
center_window(root, 565, 615)
app = ProgramSJFPreemtive(root)
root.mainloop()
