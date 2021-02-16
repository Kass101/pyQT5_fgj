# Система рисования PyQt5 способна обрабатывать векторную графику, изображения и шрифты.
# Рисование необходимо в приложениях, когда мы хотим изменить, улучшить существующий виджет, или мы создаём с нуля.
# Чтобы сделать рисунок, мы используем API рисования, предоставленное инструментарием PyQt5.
# Рисование делается в рамках метода paintEvent().Код рисования размещается между методами begin и end объекта QPainter.

# РИСОВАНИЕ ТЕКСТА

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'  # надпись \u041b\ - Л
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Draw text')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)  # начало
        self.drawText(event, qp)  # вызывается метод drawText, метод где происходит написание проги рисования
        qp.end()  # конец

    def drawText(self, event, qp):
        qp.setPen(QColor(168, 34, 3))  # определяем ручку и цвет текста
        qp.setFont(QFont('Decorative', 10))  # определяем шрифт и размер
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)  # 1 - хз, 2 - выравнивание по центру, 3 - сам текст


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
