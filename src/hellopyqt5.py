# # FileName : PyQtDemo.py
# # Author   : Adil
# # DateTime : 2018/2/1 11:07
# # SoftWare : PyCharm
#
#
# from PyQt5 import QtWidgets, QtGui
# import sys
#
# app = QtWidgets.QApplication(sys.argv)
# window = QtWidgets.QWidget();
# window.show()
# sys.exit(app.exec_())



#!/usr/bin/python3
# coding = utf-8

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#
#     w = QWidget()
#     w.resize(250, 150)
#     w.move(300, 300)
#     w.setWindowTitle('学点编程吧出品')
#     w.show()
#
#     sys.exit(app.exec_())



# FileName : main.py
# Author   : Adil
# DateTime : 2018/2/1 12:00
# SoftWare : PyCharm

import sys
import hellodesigner
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = hellodesigner.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())