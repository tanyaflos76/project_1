import sys
import sqlite3

from PyQt6 import uic, QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6.QtCore import pyqtSignal, QObject

from dialog_5 import MyDialog_5


class Communicate(QObject):
    sendVarToDialog_5 = pyqtSignal()


class MyDialog_4(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('dialog_form_4.ui', self)
        self.c = Communicate()
        self.addButton.clicked.connect(self.add)

    def getVarToDialog_4(self):
        self.dialog_5 = MyDialog_5()
        self.c.sendVarToDialog_5.connect(self.dialog_5.getVarToDialog_5)
        self.c.sendVarToDialog_5.emit()
        self.dialog_5.exec()

    def add(self):
        con = sqlite3.connect('info_about_classes.sqlite')
        date = self.date.text()
        num_lesson = self.lesson.text()
        students = self.students_class.text()
        subject = self.subject.text()
        teacher = self.teacher.text()
        num_class = self.num_class.text()
        cur = con.cursor()
        query1 = f'''select id_teacher from teachers where name = "{teacher}"'''
        res1 = cur.execute(query1)
        for i in res1:
            id_teach = str(i)[1:-2]
        query2 = f'''INSERT INTO replacements(number_lesson, subject, where_class, who_replaces, pupils_class, date)
        VALUES({num_lesson}, '{subject}', '{num_class}', {id_teach}, '{students}', '{date}')'''
        res2 = cur.execute(query2)
        con.commit()
        con.close()
        self.date.setText('')
        self.lesson.setText('')
        self.students_class.setText('')
        self.subject.setText('')
        self.teacher.setText('')
        self.num_class.setText('')


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
