# БЛОЧНЫЙ МАКЕТ
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор.
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')  # создание кнопки Ok
        cancelButton = QPushButton('Cancel')  # создание кнопки Cancel
        hbox = QHBoxLayout()  # создание горизонтального блока
        hbox.addStretch(1)  # длбавление показателя растяжения.
        # Растяжение добавляет растянутое свободное пространство перед кнопками
        hbox.addWidget(okButton)  # добавление кнопки в горизонтальный блок
        hbox.addWidget(cancelButton)  # добавление кнопки в горизонтальный блок
        vbox = QVBoxLayout()  # создание вертикального блока
        vbox.addStretch(1)  # добавление показателя растяжения.
        vbox.addLayout(hbox)  # объединетие блоков горизонтального и вертикального

        self.setLayout(vbox)  # устанавливаем главный макет окна

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttoons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход
