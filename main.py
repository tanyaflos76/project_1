import sys
import sqlite3
from PyQt6 import uic, QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSignal, QObject

from dialog import MyDialog
from dialog_2 import MyDialog_2


class Communicate(QObject):
    sendVarToDialog = pyqtSignal(object, object)
    sendVarToDialog_2 = pyqtSignal(object, object)


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
        self.showClass.clicked.connect(self.show_the_class)
        self.c = Communicate()

        # Нажажие радиокнопок
        self.floors.buttonClicked.connect(self.radio_buttons_click)

        # Отображение исходной картинки
        self.pixmap = QPixmap('school.jpg')
        self.image = self.for_picture
        self.image.move(200, 35)
        self.image.resize(700, 500)
        self.image.setPixmap(self.pixmap)

    # Сохраняем номер этажа, выбранного пользователем
    def radio_buttons_click(self, button):
        floor = button.text()
        number_floor = int(floor[0])
        self.number_floor = number_floor

    # Найдем имя файла с картинкой нужного этажа
    def find_file_name(self, name):
        con = sqlite3.connect('info_about_classes.sqlite')
        cur = con.cursor()
        query = f'''select file_name from floors where id_floor = {name}'''
        res = cur.execute(query).fetchone()
        con.close()
        return res

    def show_plan(self):
        self.dialog = MyDialog()

        file_name = str(self.find_file_name(self.number_floor))[2:-3]

        # Коммуникация с диалоговым окном
        self.c.sendVarToDialog.connect(self.dialog.getVarToDialog)
        self.c.sendVarToDialog.emit(file_name, self.number_floor)
        self.dialog.show()

    def show_the_class(self):
        self.dialog_2 = MyDialog_2()
        # Коммуникация с диалоговым окном вторым
        # self.c.sendVarToDialog_2.connect(self.dialog.getVarToDialog_2)
        # self.c.sendVarToDialog_2.emit()
        self.dialog_2.show()

    def find(self):
        self.classNumber.setVisible(True)
        self.label_2.setVisible(True)
        self.showClass.setVisible(True)

    def show_number(self):
        # number = int(self.classNumber.text())
        ...


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
