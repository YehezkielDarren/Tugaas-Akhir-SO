from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QWidget
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from qfluentwidgets import (
    FluentBackgroundTheme,
    InfoBar,
    CardWidget,
    SubtitleLabel,
    BodyLabel,
    PushButton
)
from app.module.resource import getResource


class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.team_members = [
            {
                "name": "Bernadus Xaverius H.",
                "role": "Developer",
                "quotes": "Nama juga hidup kadang diatas kadang digidaw"
            },
            {
                "name": "Yehezkiel Darren P. W.",
                "role": "Developer",
                "quotes": "Selamat menempuh hidup baru Ivan :D"
            },
            {
                "name": "Benedictus Karol Wojtyfa P. S.",
                "role": "Developer",
                "quotes": "Aku gaya\nkarol 2k24"
            }
        ]
        self.__init_layout()
        self.__setup()

    def __init_layout(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        title = SubtitleLabel("Meet Our Team", self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(title)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(20)
        grid_layout.setContentsMargins(10, 10, 10, 10)

        for i in range(2):
            card = self._create_member_card(self.team_members[i])
            grid_layout.addWidget(card, 0, i)

        card = self._create_member_card(self.team_members[2])
        grid_layout.addWidget(card, 1, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        self.layout.addLayout(grid_layout)

        button_layout = QHBoxLayout()
        close_button = PushButton('Close', self)
        close_button.clicked.connect(self.close)
        close_button.setFixedWidth(100)
        button_layout.addWidget(
            close_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.layout.addLayout(button_layout)
        self.layout.addStretch()

    def _create_member_card(self, member):
        card = CardWidget(self)
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(10)

        name_label = SubtitleLabel(member["name"], self)
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setWordWrap(True)
        card_layout.addWidget(name_label)

        role_label = BodyLabel(member["role"], self)
        role_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(role_label)

        quotes_label = BodyLabel(f'"{member["quotes"]}"', self)
        quotes_font = quotes_label.font()
        quotes_font.setItalic(True)
        quotes_label.setFont(quotes_font)
        quotes_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        quotes_label.setWordWrap(True)
        card_layout.addWidget(quotes_label)

        return card

    def __setup(self):
        self.setWindowTitle('About Us')
        self.setAcceptDrops(True)

        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        self.setStyleSheet(f"""
            QDialog {{
                background-color: #202831;
                color: #fff;
                border-radius: 8px;
                padding: 20px;
            }}

            CardWidget {{
                background-color: #2B333C;
                border-radius: 8px;
                padding: 15px;
                min-width: 270px;
                max-width: 300px;
            }}

            SubtitleLabel {{
                font-size: 14px;
                padding: 2px;
                margin: 5px;
            }}

            BodyLabel {{
                padding: 2px;
                margin-right: 5px;
                margin-left: 5px;
            }}

            PushButton {{
                padding: 5px 15px;
                background-color: #2B2D31;
                border-radius: 4px;
                color: white;
            }}

            PushButton:hover {{
                background-color: #3B3D41;
            }}
        """)
