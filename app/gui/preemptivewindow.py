from app.gui.base.interface import BaseInterface
from app.resource.concat.preemptive import preemptiveSetting
from app.module.sjf import SJF_Preemptive

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QVBoxLayout
from qfluentwidgets import Flyout, InfoBarIcon

from app.module.gantt import GanttChart

class PreemptiveInterface(BaseInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent, objectName='preemptiveWindow',
                         layoutType='expand', layoutFunction=self.__initLayout)

    def __initLayout(self):
        groups = preemptiveSetting(self.scrollWidget)

        self.layout.setSpacing(28)
        self.layout.setContentsMargins(60, 10, 60, 0)

        for group in groups.values():
            self.layout.addWidget(group)

            start_button = group.findChild(QPushButton, 'startProcess')
            tableWidget = group.findChild(QTableWidget, 'processTable')
            if start_button:
                start_button.clicked.connect(self.on_startButton_click)
            if tableWidget:
                tableWidget.itemChanged.connect(self.on_table_item_changed)

    def on_table_item_changed(self, item):
        if item.column() in [1, 2]:
            row = item.row()
            table_widget = self.findChild(QTableWidget, 'processTable')

            process_name = QTableWidgetItem(f'P{row + 1}')
            process_name.setFlags(~Qt.ItemFlag.ItemIsEditable)
            table_widget.setItem(row, 0, process_name)

    def on_startButton_click(self):
        table_widget = self.findChild(QTableWidget, 'processTable')
        table_data = []

        for row in range(table_widget.rowCount()):
            row_data = []
            row_is_empty = False

            for col in range(table_widget.columnCount()):
                item = table_widget.item(row, col)
                cell_text = item.text() if item else ""
                if col == 1 or col == 2:
                    try:
                        cell_text = int(cell_text) if cell_text else 0
                    except ValueError:
                        cell_text = 0
                if not cell_text:
                    row_is_empty = True

                row_data.append(cell_text)

            if not row_is_empty:
                table_data.append(row_data)

        if (len(table_data) < 1):
            start_button = self.sender()
            Flyout.create(
                icon=InfoBarIcon.ERROR,
                title='Warning',
                content='Minimum 1 process required!',
                target=start_button,
                parent=self,
                isClosable=True
            )
        else:
            sjf = SJF_Preemptive(table_data)
            akhir, AWT, ATA = sjf.findavgTime(sjf.process, sjf.length)

            # Gantt Chart

            result_value_awt = self.findChild(QLineEdit, 'resultAWTValue')
            if result_value_awt:
                result_value_awt.setText(str(f"{AWT:.2f} ms"))

            result_value_atat = self.findChild(QLineEdit, 'resultATATValue')
            if result_value_atat:
                result_value_atat.setText(str(f"{ATA:.2f} ms"))

            result_table_widget = self.findChild(QTableWidget, 'resultTable')
            if result_table_widget:
                result_table_widget.setRowCount(len(akhir))

                for row, (process, burst, waiting, turnaround) in enumerate(akhir):
                    process_n = QTableWidgetItem(process)
                    process_n.setFlags(~Qt.ItemFlag.ItemIsEditable)
                    result_table_widget.setItem(row, 0, process_n)

                    burst_n = QTableWidgetItem(str(burst))
                    burst_n.setFlags(~Qt.ItemFlag.ItemIsEditable)
                    result_table_widget.setItem(row, 1, burst_n)

                    waiting_n = QTableWidgetItem(str(waiting))
                    waiting_n.setFlags(~Qt.ItemFlag.ItemIsEditable)
                    result_table_widget.setItem(row, 2, waiting_n)

                    turnaround_n = QTableWidgetItem(str(turnaround))
                    turnaround_n.setFlags(~Qt.ItemFlag.ItemIsEditable)
                    result_table_widget.setItem(row, 3, turnaround_n)
