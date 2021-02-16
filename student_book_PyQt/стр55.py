# QBrush – это элементарный графический объект.
# Он используется для рисования фона графических форм, таких как прямоугольники, эллипсы или многоугольники.
# Кисть может быть трёх разных типов: предопределённая кисть, градиент, образец текстуры.

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('Brushes')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()  # Конструктор QPainter
        qp.begin(self)  # начало
        self.drawBrushes(qp)  # вызов метода drawBrushes, где происходит рисование
        qp.end()  # конец

    def drawBrushes(self, qp):
        brush = QBrush(Qt.SolidPattern)  # создание объекта и определ параметра (сплошная заливка)
        qp.setBrush(brush)
        qp.drawRect(10, 15, 90, 60)

        brush.setStyle(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

        brush.setStyle(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)

        brush.setStyle(Qt.Dense3Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(Qt.DiagCrossPattern)
        col = QColor(250, 2, 26)  # задаем фон
        qp.setBrush(col)  # задаем фон
        qp.drawRect(10, 105, 90, 60)  # задаем фон
        qp.setBrush(brush)  # рисуем узор поверх
        qp.drawRect(10, 105, 90, 60)  # рисуем узор поверх

        brush.setStyle(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)

        brush.setStyle(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        brush.setStyle(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush.setStyle(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)

        brush.setStyle(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())