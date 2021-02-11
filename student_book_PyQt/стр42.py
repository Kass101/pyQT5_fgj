# QSplitter

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame, QSplitter, QApplication)
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор.
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)  # создание горизонтального блока
        topleft = QFrame(self)  # QFrame является базовым классом для виджетов способных иметь рамку
        topleft.setFrameShape(QFrame.StyledPanel)  # setFrameShape - содержит значение формы рамки из стиля рамки
        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)
        splitter1 = QSplitter(Qt.Horizontal)  # создаем виджет QSplitter
        splitter1.addWidget(topleft)  # добавляем фрэйм в сплитер1
        splitter1.addWidget(topright)  # добавляем фрэйм в сплитер1
        splitter2 = QSplitter(Qt.Vertical)  # создаем еще один QSplitter2
        splitter2.addWidget(splitter1)  # добавляем в сплитер1 в сплитер2
        splitter2.addWidget(bottom)  # добавляем в сплитер2 еще один фрэйм
        hbox.addWidget(splitter2)  # добавляем сплитер2, где все блоки в горизонтальный блок
        self.setLayout(hbox)  # устанавливает в главный макет горизотнальный блок
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта при
    # ложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход
