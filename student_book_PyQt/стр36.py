# QSlider

import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)  # здесь мы создаем горизотальный slider
        sld.setFocusPolicy(Qt.NoFocus)  # ?
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)  # мы привязываем сигнал valueChanged
        # к определенному пользователем методу changeValue

        self.label = QLabel(self)  # создание  виджета QLabel
        self.label.setPixmap(QPixmap('стикеры.png'))  # устанавливаем начальное изображение
        self.label.setGeometry(150, 45, 680, 360)  # установка размеров и положения лейбла картинок
        self.setGeometry(300, 300, 1000, 450)  # установка размеров и положения окна
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):
        if value == 0:  # мы устанавливаем изображение стикеры.png на метку если ползунок равен 0
            self.label.setPixmap(QPixmap('стикеры.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('слайд1.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('слайд2.png'))
        else:
            self.label.setPixmap(QPixmap('слайд3.png'))
    # основываясь на значении ползунка, мы устанавливаем изображение на метку.

if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход
