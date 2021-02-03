# СТРОКА СОСТОЯНИЯ
# Зачем вообще нужна строка состояния?
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("Ready")  # чтобы получить строку состояния  мы вызываем метод statusBar().
        # Первый вызов метода создает строку состояния, последующие возвращают объект строки состояния.
        # showMessage - отображает сообщение в строке состояния
        self.setGeometry(300, 300, 250, 150) # методы resize и move в одном
        self.setWindowTitle("statusBar")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
