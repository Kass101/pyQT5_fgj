# Кнопка переключателя - это QPushButton в особом режиме, имеет 2 состояния нажатое и нет


import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор.
        self.initUI()

    def initUI(self):
        self.col = QColor(0, 0, 0)  # начальное значение цвета, черный

        redb = QPushButton("Red", self)  # создание кнопки с названием Red
        redb.setCheckable(True)  # делаем кнопку проверяемой, путем вызова сигнала setCheckable
        redb.move(10, 10)  # расположение кнопки

        redb.clicked[bool].connect(self.setColor)  # мы привязывем сигнал к нашему польззовательскому методу.
        # Мы используем значение clicked, который работает с логическим значением

        greenb = QPushButton("Green", self)
        greenb.setCheckable(True)
        greenb.move(10, 60)
        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton("Blue", self)
        blueb.setCheckable(True)
        blueb.move(10, 110)
        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget {background-color: %s }" % self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):

        source = self.sender()  # мы получаем кнопку, которая была переключена

        if pressed:
            f = 255
        else:
            f = 0

        if source.text() == "Red":
            self.col.setRed(f)
        elif source.text() == "Green":
            self.col.setGreen(f)
        else:
            self.col.setBlue(f)

        self.square.setStyleSheet("QWidget {background-color: %s }" % self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход