# ВСПЛЫВАЮЩИЕ ОКНА
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton)
from PyQt5.QtGui import QFont


class Example(QWidget):  # класс, который наследуетс из касса QWidget
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор
        self.initUI()

    def initUI(self):  # создание Gui (компонеты граф интерфейса)
        QToolTip.setFont(QFont("SansSerif", 10))  # шрифт для показа всплывающих подсказок

        self.setToolTip("This is a <b>QWidget</b> widget")  # создание подсказки

        btn = QPushButton('Button', self)  # создание виджета кнопки
        btn.setToolTip("This is a <b>QPushButton</b> widget")  # установление всплывающей плдсказки
        btn.resize(btn.sizeHint())  # 18-19 меняем размер у кнопки, перемещаем ее в окно.
        # sizeHint() дает рекаменд размер окна
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 220)  # методы resize и move в одном
        self.setWindowTitle("Tooltips")  # заголовок окна
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()   # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход