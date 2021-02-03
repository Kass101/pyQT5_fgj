# ОБЗОРНЫЙ ПРИМЕР
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QApplication, QLabel, QLineEdit, QTextEdit)


class Example(QWidget):
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор.
        self.initUI()

    def initUI(self):
        title = QLabel('Title')  # добавление надписи
        author = QLabel('Author')  # добавление надписи
        review = QLabel('Review')  # добавление надписи
        titleEdit = QLineEdit()  # добавление строки (линии) в которую можно вводить текст
        authorEdit = QLineEdit()  # добавление строки в которую можно вводить текст
        reviewEdit = QTextEdit()  # добавление блока с текстом в котором много строк и в который можно вводить текст
        grid = QGridLayout()  # создание экемпляра QGridLayout()
        grid.setSpacing(10)  # добавление отступов между блоками
        grid.addWidget(title, 1, 0)  # добавляем блок в онкно, и назначаем позицию
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)  # добавляем блок в онкно, и назначаем позицию с какой по какую

        self.setLayout(grid)




        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход
