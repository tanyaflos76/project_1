import sys

from PyQt6 import uic, QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap, QIcon
from dialog_form_2 import Ui_Dialog


class MyDialog_2(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('favicon.ico'))
        self.numberClass.setEnabled(False)
        self.teacher.setEnabled(False)
        self.floor.setEnabled(False)
        self.subject.setEnabled(False)
        self.teacher_2.setVisible(False)
        self.subject_2.setVisible(False)
        self.label_4.setVisible(False)
        self.label_8.setVisible(False)

    def getVarToDialog_2(self, number, number_floor, teacher, subject, filename):
        # Работа с информацией
        self.numberClass.setText(number)
        self.floor.setText(number_floor)
        if len(teacher) > 1:
            self.teacher_2.setVisible(True)
            self.subject_2.setVisible(True)
            self.label_4.setVisible(True)
            self.label_8.setVisible(True)
            self.subject_2.setEnabled(False)
            self.teacher_2.setEnabled(False)
            self.teacher_2.setText(teacher[1])
            self.subject_2.setText(subject[1])
        self.teacher.setText(teacher[0])
        self.subject.setText(subject[0])

        # Добавление картинки с выделенным кабинетом
        self.pixmap = QPixmap(filename)
        self.image = self.label_6
        self.image.move(335, 40)
        self.image.resize(560, 474)
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
