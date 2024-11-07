import io
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtWidgets

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MWindow</class>
 <widget class="QMainWindow" name="MWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>775</width>
    <height>488</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Навигация</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QRadioButton" name="floor1">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>70</y>
      <width>83</width>
      <height>18</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>1 этаж</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">floors</string>
    </attribute>
   </widget>
   <widget class="QRadioButton" name="floor2">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>110</y>
      <width>83</width>
      <height>18</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>2 этаж</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">floors</string>
    </attribute>
   </widget>
   <widget class="QRadioButton" name="floor3">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>150</y>
      <width>83</width>
      <height>18</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>3 этаж</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">floors</string>
    </attribute>
   </widget>
   <widget class="QRadioButton" name="floor4">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>190</y>
      <width>101</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>4 этаж </string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">floors</string>
    </attribute>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>30</y>
      <width>131</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>11</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Выберите этаж</string>
    </property>
   </widget>
   <widget class="QPushButton" name="showPicture">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>240</y>
      <width>141</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Показать план этажа</string>
    </property>
   </widget>
   <widget class="QLabel" name="for_picture">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>20</y>
      <width>511</width>
      <height>401</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="findClass">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>300</y>
      <width>141</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Найти кабинет</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="ClassNumber">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>350</y>
      <width>141</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>775</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="floors"/>
 </buttongroups>
</ui>"""


class Navigation(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)


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
