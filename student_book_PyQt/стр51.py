# РИСОВАНИЕ ТОЧЕК

import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 280, 170)  # положение и размр окна
        self.setWindowTitle('Points')  # название
        self.show()


    def paintEvent(self, e):
        qp = QPainter()  # Конструктор QPainter
        qp.begin(self)  # начало
        self.drawPoints(qp)  # вызов метода drawPoints, где происходит рисование
        qp.end()  # конец


    def drawPoints(self, qp):
        qp.setPen(Qt.red)  # устанавливаем объект ручку и его цветовой параметр красного цвета
        # p.setPen(QColor(5, 152, 0))  # еще один способ задать цвет
        size = self.size()
        for i in range(1000):
            x = random.randint(1, size.width()-1)  # рандомное определение координаты x
            y = random.randint(1, size.height()-1)  # рандомное определение координаты y
            qp.drawPoint(x, y)  # рисование точки, на заданных координатах


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())