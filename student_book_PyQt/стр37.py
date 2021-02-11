# QProgressBar

import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar, QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer

class Example(QWidget):
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор.
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)  # это конструктор QProgressBar
        self.pbar.setGeometry(30, 40, 200, 25)  # установка размеров и положения QProgressBar
        self.btn = QPushButton('Start', self)  # создание кнопки
        self.btn.move(40, 80)  # расположение кнопки
        self.btn.clicked.connect(self.doAction)  # добавление действия на кнопку
        self.timer = QBasicTimer()  # создание объекта таймера
        self.step = 0  # переменная
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход