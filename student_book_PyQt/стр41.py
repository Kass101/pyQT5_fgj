# QLineEdit

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QApplication)
from PyQt5.QtCore import QBasicTimer

class Example(QWidget):
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор.
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)  # виджет лейбл
        qle = QLineEdit(self)  # виджет редактирования текста
        qle.move(60, 100)  # расположение редактир тектса
        self.lbl.move(60, 40)  # расположение редактир лейбла
        qle.textChanged[str].connect(self.onChanged)  # если текст в виджете меняется вызывается метод onChanged
        self.setGeometry(300, 300, 280, 170)  # установка размеров и положения окна
        self.setWindowTitle('QLineEdit')  # название
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)  # устанавливаем напечатаный текст в лебл
        self.lbl.adjustSize()  # вызываем метод adjustSize(), чтобы приспосабливать размер метки к длине текста


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход