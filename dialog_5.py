import sys

from PyQt6 import uic, QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6.QtCore import pyqtSignal, QObject
from dialog_4 import MyDialog_4


class Communicate(QObject):
    sendVarFromDialog_5 = pyqtSignal()
    sendVarToDialog_4 = pyqtSignal()
    # sendVar_2_FromDialog_5 = pyqtSignal(object)


class MyDialog_5(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('dialog_form_5.ui', self)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.ok_button.clicked.connect(self.ok)
        self.cancel_button.clicked.connect(self.cancel)
        self.c = Communicate()
        self.cor_password = 'hello_world!'

    def ok(self):
        passw = self.password.text()
        if passw == self.cor_password:
            self.close()
            self.dialog_4 = MyDialog_4()
            self.c.sendVarToDialog_4.connect(self.dialog_4.getVarToDialog_4)
            self.c.sendVarToDialog_4.emit()
            self.dialog_4.show()
        else:
            self.password.setText("")
            self.label_2.setText('Неверный пароль. Попробуйте ещё раз.')

    def cancel(self):
        self.close()

    def getVarToDialog_5(self):
        ...


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
