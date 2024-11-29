from PySide6.QtCore import Qt, QEasingCurve
from PySide6.QtWidgets import QWidget
from qfluentwidgets import (
    ScrollArea, Theme, setTheme, isDarkTheme, ExpandLayout, FlowLayout)

from app.module.resource import getResource
from app.module.config import cfg


class BaseInterface(ScrollArea):
    def __init__(self, parent=None, objectName='', layoutType=None, layoutFunction=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget()
        self.scrollWidget.setObjectName('scrollWidget')

        if layoutType == 'expand':
            self.layout = ExpandLayout(self.scrollWidget)
        elif layoutType == 'flow':
            self.layout = FlowLayout(self.scrollWidget, needAni=True)
            self.layout.setAnimation(250, QEasingCurve.OutQuad)
            self.layout.setContentsMargins(30, 0, 30, 0)
            self.layout.setVerticalSpacing(20)
            self.layout.setHorizontalSpacing(10)
        else:
            raise ValueError(f'Unknown layoutType: {layoutType}')

        self.setObjectName(objectName)
        self.__initWidget(layoutFunction)
        self.__setQss()

        self.__connectSignalToSlot()

    def __initWidget(self, layoutFunction):
        self.resize(700, 600)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 40, 0, 40)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

        if layoutFunction:
            layoutFunction()

    def __setQss(self):
        theme = 'dark' if isDarkTheme() else 'light'
        with open(getResource(f'app/resource/qss/{theme}/setting_interface.qss'), 'r', encoding='UTF-8') as f:
            self.setStyleSheet(f.read())

    def __onThemeChanged(self, theme: Theme):
        setTheme(theme, lazy=True)
        self.__setQss()

    def __connectSignalToSlot(self):
        cfg.themeChanged.connect(self.__onThemeChanged)
