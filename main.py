import sys
from PyQt6 import uic, QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap

from dialog import MyDialog


class Navigation(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('template.ui', self)
        self.classNumber.setVisible(False)
        self.label_2.setVisible(False)
        self.showClass.setVisible(False)
        self.findClass.clicked.connect(self.find)
        self.showClass.clicked.connect(self.show_number)
        self.showPicture.clicked.connect(self.show_plan)

        self.pixmap = QPixmap('school.jpg')
        self.image = self.for_picture
        self.image.move(200, 35)
        self.image.resize(700, 500)
        self.image.setPixmap(self.pixmap)

    def show_plan(self):
        self.dialog = MyDialog()
        self.dialog.show()

    def find(self):
        self.classNumber.setVisible(True)
        self.label_2.setVisible(True)
        self.showClass.setVisible(True)

    def show_number(self):
        number = int(self.classNumber.text())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    ex = Navigation()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
