# ИКОНКА ПРИЛОЖЕНИЯ
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget  # импрорт необходимых модулей
from PyQt5.QtGui import QIcon


class Example(QWidget):  # класс, который наследуетс из касса QWidget
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор
        self.initUI()

    def initUI(self):  # создание Gui (компонеты граф интерфейса)
        self.setGeometry(300, 300, 300, 220)  # методы resize и move в одном)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("logo.png"))  # иконка приложения
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()   # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход