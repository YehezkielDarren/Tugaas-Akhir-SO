from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QWidget, QHeaderView, QSizePolicy
from qfluentwidgets import TableWidget, PushButton


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
            ['Process', 'Burst Time', 'Arrival Time'])
        tableWidget.horizontalHeader().setStretchLastSection(True)
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableWidget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
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

    def getCard(self, cardName):
        return self.cards.get(cardName)
