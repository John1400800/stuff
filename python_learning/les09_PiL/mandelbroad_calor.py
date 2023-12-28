import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint


class Mand(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def paintEvent(self, event):
        self.qp.begin(self)
        self.mand_bw()
        # Пока mand_bw не закончиться
        # мы не вызываем окончание рисование !
        self.qp.end()

    def mand_bw(self):
        # Комплексное после и его размеры
        xa, ya, xb, yb = [-2.0, -1.0, 1.0, 1.0]
        # Размеры окна
        img_x, img_y = self.width(), self.height()
        for y in range(img_y):
            #  найдём комплексную ординату точки
            zy = y * (yb - ya) / img_y + ya
            for x in range(img_x):
                #  найдём комплексную абсцису точки
                zx = x * (xb - xa) / img_x + xa
                # Зададим начальные параметры последовательности
                c, z = zx + zy * 1j, 0
                for cnt in range(self.max_iteration):
                    if abs(z) > 2.0:
                        break
                    z = z * z + c

                # Параметры пера / цвета
                pen = QPen(QColor(*self.palette[cnt]), 1)
                self.qp.setPen(pen)
                self.qp.drawPoint(QPoint(x, y))

    def initUI(self):
        self.setGeometry(300, 300, 600, 400)  # 600, 400
        self.setWindowTitle('black and white mandelbrot')
        self.qp = QPainter(self)
        self.max_iteration = 255
        # Создание палитры
        self.palette = [
            (
                int(255 * math.sin(i / 30.0 + 0.5) ** 2),
                int(255 * math.sin(i / 30.0 + 1.0) ** 2),
                int(255 * math.sin(i / 30.0 + 1.7) ** 2)
            ) for i in range(self.max_iteration - 1)
        ]
        self.palette.append((0, 0, 0))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mand = Mand()
    mand.show()
    sys.exit(app.exec())
