from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QMetaObject
from PySide6.QtGui import QFontDatabase, QFont, QIcon

from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import (NavigationItemPosition,
                            MSFluentWindow, FluentBackgroundTheme)
from qfluentwidgets.common.style_sheet import styleSheetManager

from app.module.resource import getResource

from app.gui.preemptivewindow import PreemptiveInterface
from app.gui.settingwindow import SettingInterface


class MainWindow(MSFluentWindow):
    def __init__(self):
        super().__init__()

        self.preemptiveInterface = PreemptiveInterface(self)
        self.settingInterface = SettingInterface(self)

        self.__navigation()
        self.__setup()

    def __navigation(self):
        self.addSubInterface(
            self.preemptiveInterface, FIF.ASTERISK,
            'SJF P',
            selectedIcon=FIF.ASTERISK
        )
        self.addSubInterface(
            self.settingInterface, FIF.SETTING,
            'Settings',
            selectedIcon=FIF.SETTING
        )

    def __setup(self):
        self.setWindowTitle('Sistem Operasi')
        self.resize(800, 600)
        self.setAcceptDrops(True)

        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

        self.setCustomBackgroundColor(*FluentBackgroundTheme.DEFAULT_BLUE)