from PyQt5.QtGui import QGuiApplication
from PyQt5 import QtQml
if __name__ == '__main__':
    path = 'helloqml.qml'
    app = QGuiApplication([])
    engine = QtQml.QQmlApplicationEngine()
    engine.load(path)
    app.exec_()