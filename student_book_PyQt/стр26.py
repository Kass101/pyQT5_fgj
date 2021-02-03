# ДИАЛОГОВЫЕ ОКНА

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton("Dialog", self)  # создание кнопки
        self.btn.move(20, 20)  # расположение кнопки
        self.btn.clicked.connect(self.showDialod)  # при нажатии кнопки вызывается функция showDialod

        self.le = QLineEdit(self)  # создание линии тектса
        self.le.move(130, 22)   # расположение линии текста

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Input Dialog')
        self.show()

    def showDialod(self):
        text, ok = QInputDialog.getText(self, "InputDialog", "Enter your name:")
        # отображает диалог ввоода для получения текстовых значений.
        # Первое значение это заголовок диалога, вторая сообщение внутри диалога
        if ok:  # диалогвозвращ логю значение и введеный текст. Если OK то лог знач = true
            self.le.setText(str(text))  # текст который мы получили устанавл в виджет редактирования текста


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход