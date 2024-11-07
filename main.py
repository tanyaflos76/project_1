import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class Navigation(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('template.ui', self)
        self.ClassNumber.setVisible(False)
        self.label_2.setVisible(False)
        self.showClass.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Navigation()
    ex.show()
    sys.exit(app.exec())
