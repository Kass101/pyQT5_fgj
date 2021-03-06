import sys
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QApplication, QPushButton, QGridLayout)


class Example(QWidget):
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор.
        self.initUI()

    def initUI(self):
        grid = QGridLayout()  # создание экемпляра QGridLayout()
        self.setLayout(grid)  # назначаем экземпляр QGridLayout() как макет окна приложения

        names = ['lcd', '', '', '', 'Cls', 'Bcb', "don't push", 'Close','7', '8', '9', '/', '4', '5', '6',
                 '*', '1', '2', '3', '-', '0', '.', '=', '+']  # список названий кнопочек
        positions = [(i, j) for i in range(6) for j in range(4)]  # список позиций
        for position, name in zip(positions, names):  # функция для перебирания 2ух списков одновременно
            if name == '':
                continue
            elif name == 'lcd':
                lcd = QLCDNumber()  # дисплей с циферками
                grid.addWidget(lcd, *position, 1, 0)
                continue
            button = QPushButton(name)  # добавляем кнопку с именем
            grid.addWidget(button, *position)  # ?

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Buttoons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход