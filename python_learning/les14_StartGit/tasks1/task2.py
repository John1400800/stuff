import sys
from random import randint, choice
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.paint_f = 0
        uic.loadUi('UI.ui', self)

        self.tpl1 = tuple(range(200, 501, 50))

        self.pushButton.clicked.connect(self.paint)
        self.painter = QPainter()

    def paint(self):
        self.paint_f = 1
        self.update()
        # self.paintEvent()
        # print(self.sender().text())

    def paintEvent(self, e):
        super().paintEvent(e)
        if self.paint_f:
            self.painter.begin(self)
            self.painter.setPen(QPen(Qt.black, 2, Qt.DashLine))
            color = QColor(*[randint(0, 255) for _ in range(3)])
            self.painter.setBrush(QBrush(color, Qt.SolidPattern))
            width = choice(self.tpl1)
            self.painter.drawEllipse(
                randint(0, 600 - width),
                randint(0, 520 - width),
                width, width)
            self.painter.end()
            self.paint_f = 0


app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec())
