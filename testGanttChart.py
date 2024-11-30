import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from app.module.gantt import GanttChart


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

    gantt_data = [['P1', 3, 3, 0, 3], ['P2', 2, 5, 2, 4]]

    window = GanttChartWidget(gantt_data)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
