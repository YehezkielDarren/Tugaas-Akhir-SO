import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


import matplotlib.pyplot as plt


class GanttChart:
    def __init__(self, data):
        self.data = sorted(data, key=lambda x: x[2])

    def render(self):
        current_time = 0
        timeline = []
        labels = []

        for process in self.data:
            process_name, burst_time, arrival_time = process
            if current_time < arrival_time:
                timeline.append((current_time, arrival_time))
                labels.append("Idle")
                current_time = arrival_time

            start_time = current_time
            end_time = current_time + burst_time
            timeline.append((start_time, end_time))
            labels.append(process_name)
            current_time = end_time

        fig, ax = plt.subplots(figsize=(8, 6), facecolor='none')

        for i, (start, end) in enumerate(timeline):
            color = "lightgray" if labels[i] == "Idle" else "skyblue"
            ax.barh(0, end - start, left=start, height=0.5,
                    align='center', color=color, edgecolor="black")
            ax.text(start + (end - start) / 2, 0, labels[i],
                    ha='center', va='center', color="black", fontsize=12)

        ax.set_yticks([])
        ax.set_xticks(range(0, max(t[1] for t in timeline) + 1, 1))
        ax.set_xlim(0, max(t[1] for t in timeline))
        ax.grid(axis='x', linestyle='--', alpha=0.7)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_linewidth(0.5)
        ax.spines['bottom'].set_linewidth(0.5)

        return fig


class GanttChartWidget(QWidget):
    def __init__(self, gantt_data):
        super().__init__()
        self.setWindowTitle("Gantt Chart in Qt")

        # Set up layout
        layout = QVBoxLayout()

        # Create Gantt chart and canvas
        gantt_chart = GanttChart(gantt_data)
        figure = gantt_chart.render()

        canvas = FigureCanvas(figure)

        # Add canvas to the layout
        layout.addWidget(canvas)

        # Set the layout for the widget
        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)

    gantt_data = [
        ("P1", 3, 0),
        ("P2", 4, 1),
        ("P3", 2, 3),
        ("P4", 5, 10)
    ]

    window = GanttChartWidget(gantt_data)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
