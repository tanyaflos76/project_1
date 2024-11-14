import sys

from PyQt6 import uic, QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap


class MyDialog_2(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('dialog_form_2.ui', self)
        self.numberClass.setEnabled(False)
        self.teacher.setEnabled(False)
        self.floor.setEnabled(False)
        self.subject.setEnabled(False)
        self.teacher_2.setVisible(False)
        self.subject_2.setVisible(False)
        self.label_4.setVisible(False)
        self.label_8.setVisible(False)

    def getVarToDialog_2(self, number, number_floor, teacher, subject):
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
