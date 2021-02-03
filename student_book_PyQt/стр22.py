# СИГНАЛЫ И СЛОТЫ
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QPushButton)

class Example(QWidget):
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор.
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber()  # дисплей с циферками
        sdl = QSlider(Qt.Horizontal, self)  # ползунок
        vbox = QVBoxLayout()  # вертикальный блок
        vbox.addWidget(lcd)  # добавление дисплея в вертикальный блок
        vbox.addWidget(sdl)
        self.setLayout(vbox)

        sdl.valueChanged.connect(lcd.display)  #

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Sidnals & Slots')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход