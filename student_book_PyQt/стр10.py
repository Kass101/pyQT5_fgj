# ЦЕНТРИРОВАНИЕ ОКОН
import sys
from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QApplication)


class Example(QWidget):  # класс, который наследуетс из касса QWidget
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор
        self.initUI()

    def initUI(self):
        self.resize(250, 150)  # размеры окна (ширина, высота)
        self.center()  # вызов метода (функции) center()
        self.setWindowTitle("Center")  # заголовок
        self.show()  # отображение виджета на экране

    def center(self):
        qr = self.frameGeometry()  # прямоугольник, точно определяющий форму главного окна
        cp = QDesktopWidget().availableGeometry().center()  # выяснение расширения монитора,
        # из этого расширения получаем центральную точку
        qr.moveCenter(cp)  # устанавливаем центр прямоугольника в центр экрана, размер прямоугольника не изменяется
        self.move(qr.topLeft())  # мы перемещаем верхнюю точку окна приложения в верхнюю левую точку прямоуг qr,
        # таким образом центризуя ее


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()   # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход
