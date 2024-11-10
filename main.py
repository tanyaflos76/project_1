import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap


class Navigation(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('template.ui', self)
        self.ClassNumber.setVisible(False)
        self.label_2.setVisible(False)
        self.showClass.setVisible(False)
        self.findClass.clicked.connect(self.find)

        self.pixmap = QPixmap('school.jpg')
        self.image = self.for_picture
        self.image.move(200, 35)
        self.image.resize(700, 500)
        self.image.setPixmap(self.pixmap)

    def find(self):
        self.ClassNumber.setVisible(True)
        self.label_2.setVisible(True)
        self.showClass.setVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Navigation()
    ex.show()
    sys.exit(app.exec())
