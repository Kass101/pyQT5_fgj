# Перетаскивание виджета кнопки

import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):  # место, где начинается операция перетаскивания
        if e.buttons() != Qt.RightButton:
            return  # если нажата не правая кнопка, то ничего не происходит (левая кнопка резервируется для нажатия)
        mimeData = QMimeData()  # Возвращает MIME-данные, заключенные в объекте перетаскивания.
        drag = QDrag(self)  # метод Drag 'n' Drop
        drag.setMimeData(mimeData)  # Устанавливает в качестве данных, которые должны быть переданы,MIME-данные data.
        # Объект drag становится владельцем данных.
        drag.setHotSpot(e.pos() - self.rect().topLeft())  # Возвращает позицию горячей точки относительно
        # левого-верхнего угла указателя мыши.
        # dropAction = drag.exec_(Qt.MoveAction)  # почему когда нет этой строки не работает перетаскивание?
        drag.exec_(Qt.MoveAction)  # вероятно данная строчка завершает перемещения, показывает что действие завершено
    def mousePressEvent(self, e):
        QPushButton.mousePressEvent(self, e)
        if e.button() == Qt.LeftButton:  # если нажата левая кнопка то пишется print  в консоли
            print('press')


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)  #
        self.button = Button('Button', self)  # создание кнопки,
        # при помощи класса Button скорее всего задаются действия кнопки при нажатии ???
        self.button.move(100, 65)  # расположение кнопки
        self.setWindowTitle('Click or Move')  # название окна
        self.setGeometry(300, 300, 280, 150)  # расположение и размеры окна

    def dragEnterEvent(self, e):
        e.accept()
    # а вот без этого перетаскивание не работает, но выводит press

    def dropEvent(self, e):
        #  здесь кодирутся то что произойдет после того,как мы опустим кнопку мышии завершим операцию перетаскивания
        position = e.pos()  # узнаем текущее положение указателя мыши
        self.button.move(position)  # перемщение кнопки
        # e.setDropAction(Qt.MoveAction)  # мы указываем тип действия перетаскивания, в нашем случае перемещение
        # e.accept()  # и без этих строчек работает, зачем они?


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта при
    # ложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    ex.show()
    app.exec_()