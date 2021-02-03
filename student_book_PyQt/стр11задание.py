# ОКНО ДОЛЖНО ОТОБРАЖ В ПРАВОМ НИЖНЕМ, А ДИАЛОГОВОЕ В ЛЕВОМ ВЕРХНЕМ УГЛАХ
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox, QDesktopWidget)


class Example(QWidget):  # класс, который наследуетс из касса QWidget
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор
        self.initUI()

    def right(self):
        qr = self.frameGeometry()  # прямоугольник, точно определяющий форму главного окна
        cp = QDesktopWidget().availableGeometry().bottomRight()
        qr.moveBottomRight(cp)
        self.move(qr.topLeft())  # мы перемещаем верхнюю точку окна приложения в верхнюю левую точку прямоуг qr,
        # таким образом центризуя ее

    def left(self):
        qr = self.frameGeometry()  # прямоугольник, точно определяющий форму главного окна
        cp = QDesktopWidget().availableGeometry().topLeft()
        qr.moveTopLeft(cp)
        self.move(qr.topLeft())  # мы перемещаем верхнюю точку окна приложения в верхнюю левую точку прямоуг qr,
        # таким образом центризуя ее

    def initUI(self):  # создание Gui (компонеты граф интерфейса)
        self.setGeometry(300, 300, 300, 220)  # методы resize и move в одном
        self.setWindowTitle("Tooltips")  # заголовок окна
        self.right()
        self.show()

    def closeEvent(self, event):
        self.left()
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',\
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # Показываем сообщение с двумя кнопками Yes и No. Первая строка появляется в заголовке.
        # Вторая это текст сообщения, отображаемый с помощью диалогового окна.
        # Третий аргумент указывает комбинацию кнопок, появляющ в диалоге.
        # Последний - кнопка по умолчанию, которая первоначально имеет на себе указатель клавиатуры
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            self.right()
        # (18-21) Если мы закрываем QWidget, вызывается QCloseEvent. Чтобы изменить поведение виджета,
        # нам необходимо переопределить обработчик событий closeEvent()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()   # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход