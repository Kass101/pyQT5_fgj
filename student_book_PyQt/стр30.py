# QFileDialog

import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор.
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()  # создание текстового блока
        self.setCentralWidget(self.textEdit)  # устанавливает виждет в качестве центрального виджета главного экрана
        self.statusBar()  # строка состояния

        openFile = QAction(QIcon('logo.png'), 'Open', self)  # добавляеи действие иконка + название
        openFile.setShortcut('Ctrl+Q')  # задаем горячие клавиши
        openFile.setStatusTip('Open new File')  # добавляет статус в строку состояния
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()  # создание меню
        fileMenu = menubar.addMenu('&File')  # создание меню и его название
        fileMenu.addAction(openFile)  # добавить действие открытие файла

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        f = open(fname, 'r')
        with f:
            data = f.read()
            self.textEdit.setText(data)
        # выбранное имя файла читается и содержащий файл устанавливается в виджет редактир текста


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход