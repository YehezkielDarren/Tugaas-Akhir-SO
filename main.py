import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from app.core import MyMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

    window = MyMainWindow()
    window.show()

    app.exec()
