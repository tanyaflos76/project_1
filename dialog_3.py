import sys

from PyQt6 import uic, QtCore, QtWidgets
import datetime as dt
import sqlite3
from dialog_form_3 import Ui_Dialog
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView


class MyDialog_3(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('info_about_classes.sqlite')
        self.current_date = dt.datetime.now().date().strftime("%d.%m.%Y")
        self.setWindowIcon(QIcon('favicon.ico'))

    def getVarToDialog_3(self):
        cur = self.con.cursor()
        query = f'''select pupils_class, number_lesson, subject, (select name from teachers where id_teacher = who_replaces), where_class from replacements where date = "{self.current_date}"'''
        titles = ['Класс', '№ урока', 'Предмет', 'Учитель', 'Кабинет']
        res = cur.execute(query).fetchall()
        if res:
            self.tableWidget.setRowCount(len(res))
            self.tableWidget.setColumnCount(len(res[0]))
            self.tableWidget.setHorizontalHeaderLabels(titles)
            self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

            for i, row in enumerate(res):
                for j, item in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))
        self.label_date.setText(self.label_date.text() + ' ' + self.current_date)


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
