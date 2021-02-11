# QCalendarWidget, QLabel

import sys
from PyQt5.QtWidgets import (QWidget, QCalendarWidget, QLabel, QApplication)
from PyQt5.QtCore import QDate


class Example(QWidget):
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор.
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)  # создание виджета QCalendarWidget
        cal.setGridVisible(True)  #
        cal.move(20, 20)  # расположение календаря
        cal.clicked[QDate].connect(self.showDate)  # когда выбирается дата срабатывает сигнал clicked[QDate],
        # и мы присоединем этот сигнал к определленому пользовательскому методу showDate

        self.lbl = QLabel(self)  # создание лейбла
        date = cal.selectedDate()  # возвращаем выбранную дату путем вызова метода selectedDat (начальная дата)
        self.lbl.setText(date.toString())  # превращаем объект даты в строку и устанавливаем в лейбл (начальная дата)
        self.lbl.move(130, 260)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()


    def showDate(self, date):
        self.lbl.setText(date.toString())  # превращаем объект даты в строку и устанавливаем в лейбл (выбранная дата)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход