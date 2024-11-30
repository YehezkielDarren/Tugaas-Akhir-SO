from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QWidget, QHeaderView, QSizePolicy, QTableWidget, QTableWidgetItem
from qfluentwidgets import TableWidget, PushButton, LineEdit, PrimaryPushSettingCard, FluentIcon as FIF


class preemptiveCardManager:
    def __init__(self):
        self.cards = {}

    def preemptiveCards(self, parent):
        vBoxLayout = QVBoxLayout()
        vBoxLayout.setContentsMargins(0, 0, 0, 0)

        # Title
        processTitle = QLabel('Preemptive Scheduling')
        processTitle.setObjectName('processTitle')
        processTitle.setStyleSheet('font-weight: bold;')
        processTitle.setContentsMargins(0, 0, 0, 0)
        vBoxLayout.addWidget(processTitle)

        # Table
        tableWidget = TableWidget(parent)
        tableWidget.setObjectName('processTable')
        tableWidget.setRowCount(10)
        tableWidget.setColumnCount(3)
        tableWidget.setHorizontalHeaderLabels(
            ['Process', 'Arrival Time', 'Burst Time'])
        tableWidget.horizontalHeader().setStretchLastSection(True)
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableWidget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)

        for row in range(tableWidget.rowCount()):
            item = QTableWidgetItem()
            item.setFlags(~Qt.ItemFlag.ItemIsEditable)
            tableWidget.setItem(row, 0, item)

        vBoxLayout.addWidget(tableWidget)

        # Buttons
        startButton = PushButton('Start', parent)
        startButton.setObjectName('startProcess')
        startButton.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Fixed)
        vBoxLayout.addWidget(startButton)

        cardWidget = QWidget()
        cardWidget.setLayout(vBoxLayout)

        self.cards['preemptive'] = cardWidget
        return cardWidget

    def resultPreemptiveCards(self, parent):
        vBoxLayout = QVBoxLayout()
        vBoxLayout.setContentsMargins(0, 0, 0, 0)

        # Gantt Chart
        ganttChart = PrimaryPushSettingCard(
            'Gantt Chart',
            FIF.VIEW,
            'View Gantt Chart',
            f'Visual representation of the scheduling algorithm',
            parent
        )
        ganttChart.setObjectName('ganttChart')
        vBoxLayout.addWidget(ganttChart)

        # Average Waiting Time
        hBoxLayout = QHBoxLayout()
        hBoxLayout.setContentsMargins(0, 0, 0, 0)
        resultTitle = QLabel('Average Waiting Time')
        resultTitle.setObjectName('resultAWT')
        resultTitle.setStyleSheet('font-weight: bold;')
        hBoxLayout.addWidget(resultTitle)

        resultValue = LineEdit(parent)
        resultValue.setObjectName('resultAWTValue')
        resultValue.setReadOnly(True)
        hBoxLayout.addWidget(resultValue)
        vBoxLayout.addLayout(hBoxLayout)

        # Average Turn-Around Time
        hBoxLayout = QHBoxLayout()
        hBoxLayout.setContentsMargins(0, 0, 0, 0)
        resultTitles = QLabel('Average Turn-Around Time')
        resultTitles.setObjectName('resultATAT')
        resultTitles.setStyleSheet('font-weight: bold;')
        hBoxLayout.addWidget(resultTitles)

        resultValues = LineEdit(parent)
        resultValues.setObjectName('resultATATValue')
        resultValues.setReadOnly(True)
        hBoxLayout.addWidget(resultValues)
        vBoxLayout.addLayout(hBoxLayout)

        # Table
        tableWidget = TableWidget(parent)
        tableWidget.setObjectName('resultTable')
        tableWidget.setColumnCount(4)
        tableWidget.setHorizontalHeaderLabels(
            ['Process', 'Burst Time', 'Waiting Time', 'Turn-Around Time'])
        tableWidget.horizontalHeader().setStretchLastSection(True)
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        vBoxLayout.addWidget(tableWidget)

        cardWidget = QWidget()
        cardWidget.setLayout(vBoxLayout)

        self.cards['resultPreemptive'] = cardWidget
        return cardWidget

    def getCard(self, cardName):
        return self.cards.get(cardName)
