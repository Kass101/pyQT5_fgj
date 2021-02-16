# QPen (ручка) – это элементарный графический объект.
# Используется, чтобы рисовать линии, кривые и контуры прямоугольников, эллипсов, многоугольников и других фигур.

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Pen styles')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()  # Конструктор QPainter
        qp.begin(self)  # начало
        self.drawLines(qp)  # вызов метода drawLines, где происходит рисование
        qp.end()  # конец

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)  # создание объекта, цвет - черный, жирность - 2px,
        # Qt.SolidLine – это один из стилей (жирная линия)
        qp.setPen(pen)  # создание объекта, и установка параметров ручки
        qp.drawLine(20, 40, 250, 40)  # рисование линии

        pen.setStyle(Qt.DashLine)  # стиль пунктир
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)  # стиль пунктир точка
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)  # стиль пунктир мелкий
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)  # стиль пунктир точка точка
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        # определяем пользовательский стиль ручки.
        # Мы устанавливаем стиль ручки Qt.CustomDashLine и вызываем метод setDashPattern().
        # Список чисел определяет стиль. Может быть даже несколько чисел.
        # Нечётные числа определяют сплошную линию, чётные числа – промежутки.
        # Чем больше число, тем больше промежуток или штрих.
        # Наш образец – штрих в 1 пиксель, промежуток в 4 пикселя, штрих в 5 пикселей, промежуток в 4 пикселя
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())