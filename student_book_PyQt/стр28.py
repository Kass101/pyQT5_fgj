# QFontDialog
import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QSizePolicy, QLabel, QFontDialog, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()  # вертикальный блок
        btn = QPushButton('Dialog', self)  # создание кнопки
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # фиксированный размер кнопки
        btn.move(20, 20)  # расположение кнопки
        vbox.addWidget(btn)  # добавление кнопки в вертикальный бокс
        btn.clicked.connect(self.showDialog)  # при нажатие на кнопку вызывается функция showDialog
        self.lbl = QLabel('Knowledge only matters', self)  # создание надписи (Label)
        self.lbl.move(130, 20)  # расположение label
        vbox.addWidget(self.lbl)  # добавление label  в вертикальный бокс
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()  # высвечиваем диалог со шрифтами,
        # метод getFont возвращает имя шрифта и параметр ok
        if ok:  # если кликнули OK, шрифт метки б изменился
            self.lbl.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход