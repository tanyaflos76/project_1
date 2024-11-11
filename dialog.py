import sys

from PyQt6 import uic, QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap


class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('dialog_form.ui', self)

    def getVarToDialog(self, filename, number_floor):
        # Отображаем в label номер этажа
        self.nameOfTheFloor.setText(f'{number_floor} этаж')
        # Отображаем саму картинку
        self.pixmap = QPixmap(filename)
        self.image = self.label
        if filename == 'floors_picture/1_floor' or 'floors_picture/2_floor':
            self.image.move(162, 40)
            self.image.resize(1060, 670)
        else:
            self.image.move(0, 0)
            self.image.resize(1000, 670)
        self.image.setPixmap(self.pixmap)


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
