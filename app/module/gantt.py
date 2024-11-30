import matplotlib.pyplot as plt


class GanttChart:
    def __init__(self, data):
        self.data = sorted(data, key=lambda x: x[2])

    def render(self):
        plt.clf()
        timeline = []
        labels = []

        current_time = 0
        for process in self.data:
            process_name, burst_time, completion_time, waiting_time, turnaround_time = process

            if current_time < completion_time:
                timeline.append((current_time, completion_time))
                labels.append("Idle")
                current_time = completion_time

            start_time = current_time
            end_time = start_time + burst_time
            timeline.append((start_time, end_time))
            labels.append(process_name)
            current_time = end_time

        fig, ax = plt.subplots(figsize=(6, 4), facecolor='none')

        for i, (start, end) in enumerate(timeline):
            color = "lightgray" if labels[i] == "Idle" else "skyblue"
            ax.barh(0, end - start, left=start, height=0.5,
                    align='center', color=color, edgecolor="black")
            ax.text(start + (end - start) / 2, 0,
                    labels[i], ha='center', va='center', color="black", fontsize=12)

        ax.set_yticks([])
        
        # Menentukan ticks hanya pada start dan end times dari proses dan idle
        time_ticks = sorted(set([start for start, _ in timeline] + [end for _, end in timeline]))
        ax.set_xticks(time_ticks)
        
        ax.set_xlim(0, max(t[1] for t in timeline))
        ax.grid(axis='x', linestyle='--', alpha=0.7)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_linewidth(0.5)
        ax.spines['bottom'].set_linewidth(0.5)

        plt.title('Gantt Chart')
        return fig
