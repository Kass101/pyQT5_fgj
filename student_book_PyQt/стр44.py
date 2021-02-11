# QComboBox - виджет позволяющий пользователю выбирать из списка вариантов

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QApplication)


class Example(QWidget):
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор.
        self.initUI()

    def initUI(self):
        self.lbl = QLabel("Ubuntu", self)  # создание лейбла
        combo = QComboBox(self)  # созданиеи виджета
        combo.addItems(["Ubuntu", "Mandriva", "Fedora", "Arch", "Gentoo"])  # список вариантов
        combo.move(50, 50)  # расположение блока со списком
        self.lbl.move(50, 150)  # расположенеи лейбла
        combo.activated[str].connect(self.onActivated)  # после ввыбора пункта вызывается метод (функция) onActivated
        self.setGeometry(300, 300, 300, 200)  # методы move и resize в одном
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)  # устанавливаем выбранный текст в лебл
        self.lbl.adjustSize()  # вызываем метод adjustSize(), чтобы приспосабливать размер метки к длине текста


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта при
    # ложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход

