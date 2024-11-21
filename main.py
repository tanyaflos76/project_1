import sys
import sqlite3
from PyQt6 import uic, QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSignal, QObject

from dialog import MyDialog
from dialog_2 import MyDialog_2
from dialog_3 import MyDialog_3
from dialog_4 import MyDialog_4
from dialog_5 import MyDialog_5


class Communicate(QObject):
    sendVarToDialog = pyqtSignal(object, object)
    sendVarToDialog_2 = pyqtSignal(object, object, object, object, object)
    sendVarToDialog_3 = pyqtSignal()
    sendVarToDialog_4 = pyqtSignal()
    sendVarToDialog_5 = pyqtSignal()
    sendVar_2_ToDialog_5 = pyqtSignal(object)


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
        self.action_2.triggered.connect(self.replacements_act)
        self.action_3.triggered.connect(self.admin_act)

        # Нажажие радиокнопок
        self.floors.buttonClicked.connect(self.radio_buttons_click)

        # Отображение исходной картинки
        self.pixmap = QPixmap('school.jpg')
        self.image = self.for_picture
        self.image.move(200, 20)
        self.image.resize(700, 500)
        self.image.setPixmap(self.pixmap)

    def replacements_act(self):
        self.dialog_3 = MyDialog_3()

        self.c.sendVarToDialog_3.connect(self.dialog_3.getVarToDialog_3)
        self.c.sendVarToDialog_3.emit()
        self.dialog_3.show()

    def admin_act(self):
        self.dialog_5 = MyDialog_5()

        self.c.sendVarToDialog_5.connect(self.dialog_5.getVarToDialog_5)
        self.c.sendVarToDialog_5.emit()
        self.dialog_5.exec()

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

    def data_is_correct(self):
        data = self.classNumber.text()
        con = sqlite3.connect('info_about_classes.sqlite')
        cur = con.cursor()
        query = f'''select id_teacher from classrooms where num_class = "{data}"'''
        res = cur.execute(query).fetchall()
        con.close()
        if not res:
            return False
        return True

    def show_plan(self):
        self.dialog = MyDialog()

        file_name = str(self.find_file_name(self.number_floor))[2:-3]

        # Коммуникация с диалоговым окном
        self.c.sendVarToDialog.connect(self.dialog.getVarToDialog)
        self.c.sendVarToDialog.emit(file_name, self.number_floor)
        self.dialog.show()

    def show_the_class(self):
        self.dialog_2 = MyDialog_2()

        if self.data_is_correct():
            # Поиск нужной информации для выбранного кабинета
            number = self.classNumber.text()
            teacher = self.find_teacher(number)
            subject = [str(self.find_subject(i))[2:-2] for i in teacher]
            number_floor = self.find_num_floor(number)
            filename = self.find_filename_class(number)

            # Коммуникация с диалоговым окном вторым
            self.c.sendVarToDialog_2.connect(self.dialog_2.getVarToDialog_2)
            self.c.sendVarToDialog_2.emit(number, number_floor, teacher, subject, filename)
            self.dialog_2.show()
        else:
            self.statusBar().showMessage('Кабинет не найден.')
            self.classNumber.setText("")

    def find(self):
        self.classNumber.setVisible(True)
        self.label_2.setVisible(True)
        self.showClass.setVisible(True)

    def find_teacher(self, number):
        result = []
        con = sqlite3.connect('info_about_classes.sqlite')
        cur = con.cursor()
        query = f'''select name from teachers where id_teacher in
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

    def find_num_floor(self, number_class):
        con = sqlite3.connect('info_about_classes.sqlite')
        cur = con.cursor()
        query = f'''select id_floor from classrooms where num_class = "{number_class}"'''
        res = cur.execute(query).fetchall()
        res = str(res)[2:3]
        con.close()
        return res

    def find_filename_class(self, number_class):
        con = sqlite3.connect('info_about_classes.sqlite')
        cur = con.cursor()
        query = f'''select file_name from classrooms where num_class = "{number_class}"'''
        res = cur.execute(query).fetchall()
        res = str(res[0])[2:-3]
        con.close()
        return res


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
