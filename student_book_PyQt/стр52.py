# Цвет – это объект, представляющий собой комбинацию красного, зелёного и синего (RGB)
# Мы можем определить цвет разными способами десятичные или шестнадцатеричные значения RGB
# Мы также можем использовать значения RGBA, которые обозначают красный, зелёный, синий и альфа-канал
# Значение альфа 255 определяет полную непрозрачность, 0 – полная прозрачность, т.е. цвет невидим.

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 100)  # расположение и размеры окна
        self.setWindowTitle('Colours')  # название
        self.show()

    def paintEvent(self, e):
        qp = QPainter()  # Конструктор QPainter
        qp.begin(self)  # начало
        self.drawRectangles(qp)  # вызов метода drawRectangles, где происходит рисование
        qp.end()  # конец

    def drawRectangles(self, qp):
        col = QColor(0, 0, 0)  # определение цвета для col, начальный черный
        col.setNamedColor('#d4d4d4')  # задаем другой цвет для переменной col в 16ричной с/c
        qp.setPen(col)  # определяем цвет которыйм рисуем (обводки будущих прямоугольников)

        qp.setBrush(QColor(200, 0, 0))  # определяем кисть, ее цвет, и рисуем окрашеный прямоугольник
        qp.drawRect(10, 15, 90, 60)  # рисуем прямоугольник по координатам (1 и 2 - одна точка, 3-4 вторая)

        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(130, 15, 90, 60)

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 90, 60)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())