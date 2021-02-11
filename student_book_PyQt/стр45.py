# ПРОСТОЕ ПЕРЕТАСКИВАНИЕ

import sys
from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication)

class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)
        button = Button("Button", self)
        button.move(190, 65)
        self.setWindowTitle('Simple drag & drop')
        self.setGeometry(300, 300, 300, 150)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта при
    # ложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход
