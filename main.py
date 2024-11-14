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
    sendVarToDialog_2 = pyqtSignal(object, object, object, object, object)


class Navigation(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('template.ui', self)
        self.classNumber.setVisible(False)
        self.label_2.setVisible(False)
        self.showClass.setVisible(False)
        self.findClass.clicked.connect(self.find)
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
        # self.c.sendVarToDialog_2.connect(self.dialog_2.getVarToDialog_2)
        # self.c.sendVarToDialog_2.emit()
        number = self.classNumber.text()
        teacher = self.find_teacher(number)
        subject = [self.find_subject(i) for i in teacher]
        classes = [self.find_classes(i) for i in teacher]
        print(number, teacher, subject, classes)
        self.dialog_2.show()

    def find(self):
        self.classNumber.setVisible(True)
        self.label_2.setVisible(True)
        self.showClass.setVisible(True)

    def find_teacher(self, number):
        result = []
        con = sqlite3.connect('info_about_classes.sqlite')
        cur = con.cursor()
        query = f'''select name from teachers where id_teacher =
(select id_teacher from classrooms where num_class = '{number}')'''
        res = cur.execute(query).fetchall()
        con.close()
        for i in res:
            teacher = str(i)[2:-3]
            result.append(teacher)
        return result

    def find_subject(self, teacher):
        result = []
        con = sqlite3.connect('info_about_classes.sqlite')
        cur = con.cursor()
        query = f'''select subject from teachers where name = "{teacher}"'''
        res = cur.execute(query).fetchall()
        con.close()
        for i in res:
            subject = str(i)[2:-3]
            result.append(subject)
        return result

    def find_classes(self, teacher):
        result = []
        con = sqlite3.connect('info_about_classes.sqlite')
        cur = con.cursor()
        query = f'''select whom_teaches from teachers where name = "{teacher}"'''
        res = cur.execute(query).fetchall()
        con.close()
        for i in res:
            classes = str(i).replace('\\n', '')[2:-3]
            result.append(classes)
        return result


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
