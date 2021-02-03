# QColorDialog
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QFrame, QColorDialog, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)  # первоначальный цвет фона
        self.btn = QPushButton('Dialog', self)  # создание кнопки
        self.btn.move(20, 20)  # размеры кнопки
        self.btn.clicked.connect(self.showDialog)  # при нажатии вызов функции showDialog
        self.frm = QFrame(self)  # окошко где отображается цвет
        self.frm.setStyleSheet("QWidget { background-color: %s}" % col.name())  # перевод первоначального цвета фона
        # в другой формат (#000000)
        # self.frm.setStyleSheet("QWidget { background-color: #000}") можно задать начальный цвет так
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Color Dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()  # это строка высветит QColorDialog (где выбирать цвет)
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s}" % col.name())  # выбор цвета
        # мы проверяем явл цвет валидным, если нажимаем кнопку Cancel, возвращ невалидный цвет,
        # елси цвет валиден, мы меняем цвет фона используя табл css

if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход
