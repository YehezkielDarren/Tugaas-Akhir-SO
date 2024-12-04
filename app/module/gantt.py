import matplotlib.pyplot as plt
import heapq


class GanttChart:
    def __init__(self, processes):
        self.processes = sorted(processes, key=lambda x: x[1])

    def render(self):
        plt.clf()

        current_time = 0
        completed = 0
        n = len(self.processes)
        heap = []
        timeline = []
        labels = []

        remaining_time = {proc[0]: proc[2] for proc in self.processes}

        # Menyimpan daftar proses (arrival_time, burst_time) yang belum selesai
        i = 0
        while completed < n:
            # Tambahkan semua proses yang tiba ke heap berdasarkan sisa waktu eksekusi
            while i < n and self.processes[i][1] <= current_time:
                process_name, arrival_time, burst_time, _, _, _ = self.processes[i]
                heapq.heappush(
                    heap, (remaining_time[process_name], arrival_time, process_name))
                i += 1

            if not heap:
                # Jika tidak ada proses yang siap, idle hingga proses berikutnya datang
                if i < n:
                    timeline.append(
                        (current_time, self.processes[i][1], "Idle"))
                    current_time = self.processes[i][1]
                continue

            # Ambil proses dengan waktu sisa terkecil
            remaining_burst, arrival_time, process_name = heapq.heappop(heap)

            # Proses berjalan satu satuan waktu
            start_time = current_time
            current_time += 1
            remaining_time[process_name] -= 1

            # Update timeline dan label
            if timeline and timeline[-1][2] == process_name:
                timeline[-1] = (timeline[-1][0], current_time, process_name)
            else:
                timeline.append((start_time, current_time, process_name))

            # Jika proses selesai
            if remaining_time[process_name] == 0:
                completed += 1
            else:
                # Masukkan kembali proses ke heap dengan waktu sisa yang diperbarui
                heapq.heappush(heap, (remaining_time[process_name], arrival_time, process_name))

        # Plot konfigurasi
        fig, ax = plt.subplots(figsize=(10, 5), facecolor='none')

        for start, end, label in timeline:
            color = "lightgray" if label == "Idle" else "skyblue"
            ax.barh(0, end - start, left=start, height=0.5,
                    align='center', color=color, edgecolor="black")
            ax.text((start + end) / 2, 0, label, ha='center',
                    va='center', color="black", fontsize=12)

        ax.set_yticks([])
        time_ticks = sorted(
            set([start for start, _, _ in timeline] + [end for _, end, _ in timeline]))
        ax.set_xticks(time_ticks)

        ax.set_xlim(0, max(end for _, end, _ in timeline))
        ax.grid(axis='x', linestyle='--', alpha=0.7)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_linewidth(0.5)

        plt.title('Gantt Chart')
        plt.xlabel('Time')
        return fig

# Kalau mau debug
# if __name__ == '__main__':
#     processes = [[1, 0, 6], [2, 1, 8], [3, 2, 7], [4, 3, 3]]
#     gantt = GanttChart(processes)
#     fig = gantt.render()
#     plt.show()