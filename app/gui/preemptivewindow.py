from app.gui.base.interface import BaseInterface
from app.resource.concat.preemptive import preemptiveSetting
from app.module.sjf import SJF_Preemptive

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QTableWidget, QTableWidgetItem
from qfluentwidgets import Flyout, InfoBarIcon


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
            # TODO: Implement UI for SJF Preemptive

            sjf = SJF_Preemptive(table_data)
            akhir, AWT, ATA = sjf.findavgTime(sjf.process, sjf.length)
            print(akhir, AWT, ATA)
