# ПАНЕЛЬ ИНСТРУМЕНТОВ
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):  # __init__() - Конструктор класса в языке Python
        super().__init__()  # метод super() возвращает объект родителя из класса Example и мы вызыв его конструктор
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('logo.png'), 'Exit', self)  # QAction - абстракция действий, выполняемых из меню,
        # панелью инструментов или горячих клавиш
        # задаем exitAction название действия и иконку рядом
        exitAction.setShortcut('Ctrl+Q')  # определяем горячую клавишу
        exitAction.triggered.connect(qApp.quit)  # когда выбирают действие срабатывает инициирующий сигнал.
        # Сигнал присоединяется к методу quit() виджета QApplication. Это завершает приложение
        self.toolbar = self.addToolBar("Exit")  # создаем панель инструментов и подключам объект действия к ней
        self.toolbar.addAction(exitAction)  # добавление в панель инструментов строки (действия)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('ToolBar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    ex = Example()  # вызов класса Example
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход