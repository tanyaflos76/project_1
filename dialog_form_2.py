# Form implementation generated from reading ui file 'dialog_form_2.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(911, 544)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(340, 10, 561, 511))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        self.label_7.setGeometry(QtCore.QRect(80, 110, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 200, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.floor = QtWidgets.QLineEdit(parent=Dialog)
        self.floor.setGeometry(QtCore.QRect(130, 110, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.floor.setFont(font)
        self.floor.setObjectName("floor")
        self.numberClass = QtWidgets.QLineEdit(parent=Dialog)
        self.numberClass.setGeometry(QtCore.QRect(130, 80, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.numberClass.setFont(font)
        self.numberClass.setObjectName("numberClass")
        self.teacher = QtWidgets.QLineEdit(parent=Dialog)
        self.teacher.setGeometry(QtCore.QRect(130, 170, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.teacher.setFont(font)
        self.teacher.setObjectName("teacher")
        self.subject = QtWidgets.QLineEdit(parent=Dialog)
        self.subject.setGeometry(QtCore.QRect(130, 200, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.subject.setFont(font)
        self.subject.setObjectName("subject")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 260, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(parent=Dialog)
        self.label_8.setGeometry(QtCore.QRect(60, 290, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.teacher_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.teacher_2.setGeometry(QtCore.QRect(130, 260, 201, 21))
        self.teacher_2.setObjectName("teacher_2")
        self.subject_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.subject_2.setGeometry(QtCore.QRect(130, 290, 201, 21))
        self.subject_2.setObjectName("subject_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Поиск кабинета"))
        self.label.setText(_translate("Dialog", "Дополнительная информация о кабинете:"))
        self.label_2.setText(_translate("Dialog", "Преподаватель:"))
        self.label_3.setText(_translate("Dialog", "Номер кабинета:"))
        self.label_7.setText(_translate("Dialog", "Этаж:"))
        self.label_5.setText(_translate("Dialog", "Предмет:"))
        self.label_4.setText(_translate("Dialog", "Преподаватель:"))
        self.label_8.setText(_translate("Dialog", "Предмет:"))
