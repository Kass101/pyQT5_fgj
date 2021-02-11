# QPixmap - виджет для работы с изображениями. Оптимизировван для показа изображений на экране

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор.
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)  # создание горизонтального блока
        pixmap = QPixmap("слайд1.png")  # создание объекта QPixmap
        lbl = QLabel(self)  # создания лейбла
        lbl.setPixmap(pixmap)  # добавление QPixmap в лейбл
        hbox.addWidget(lbl)  # добавляем лейбл в горизонтальный блок
        self.setLayout(hbox)  # объединение с окном
        self.move(300, 200)  # обозначение положения
        self.setWindowTitle('Red Rock')  # название
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход