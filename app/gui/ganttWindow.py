from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout
from PySide6.QtGui import QIcon
from qfluentwidgets import FluentBackgroundTheme
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

from app.module.resource import getResource
from app.module.gantt import GanttChart


class GanttWindow(QDialog):
    def __init__(self, gantt_data):
        super().__init__()
        self.__init_layout(gantt_data)
        self.__setup()

    def __init_layout(self, gantt_data):
        self.layout = QVBoxLayout()
        self.gantt_chart = GanttChart(gantt_data)
        self.figure = self.gantt_chart.render()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

    def __setup(self):
        self.setWindowTitle('Gantt Chart')
        self.setAcceptDrops(True)

        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        background_theme = FluentBackgroundTheme.DEFAULT_BLUE
        color1, color2 = background_theme

        self.setStyleSheet(f"""
            QDialog {{
                background-color: {color2.name()};
            }}
        """)