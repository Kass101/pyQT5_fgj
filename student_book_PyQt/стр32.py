# QCheckBox

import sys
from PyQt5.QtWidgets import (QWidget, QCheckBox, QApplication)
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор.
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self)  # конструктор QCheckBox
        cb.move(20, 20)  # расположенеи чекбокса
        cb.toggle()  # мы устанавливаем галочку (показывает что кнопка уже выбрана)
        cb.stateChanged.connect(self.changeTitle)
        # мы связываем пользователя, определяющего метод changeTitle, с сигналом stateChange.
        # метод changeTitle будет переключать заголовок кна

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')
    # переменная state - состояние виджета. Если виджет помечен галочкой, то иы устанавливаем заголовок окнаю


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход
