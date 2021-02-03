# СРАБАТЫВАНИЕ СИГНАЛОВ
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    closeApp = pyqtSignal()  # сигнал создается с pyqtSignal как атрибут класса внешного класса Communicate


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()  # Что такое Communicate()?
        self.c.closeApp.connect(self.close)  # пользовательский сигнал closeApp
        # присоединяется к слоту close класса QMainWindow
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):  # событие происходящее при клике мыши?
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# Когда мы кликаем на окне курсором мыши, срабатывает сигнал closeApp, и приложение закрывается
