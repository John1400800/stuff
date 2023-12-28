from email.mime import image
import sys
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLabel, QPushButton, QFileDialog
)
MATRIX_INDEX = {'R': 0, 'G': 5, 'B': 10}
MATRIX = [0, 0, 0, 0,
          0, 0, 0, 0,
          0, 0, 0, 0]


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PIL 2.0')
        self.name = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '')[0]
        grid = QGridLayout()
        self.setLayout(grid)
        self.angle = 0
        self.res = 'res.jpg'
        self.img = QLabel()
        self.img.setPixmap(QPixmap(self.name))
        self.init_img()
        grid.addWidget(self.img, 0, 1, 4, 3)
        for indx, btn_n in enumerate(('R', 'G', 'B', 'ALL')):
            btn = QPushButton(btn_n)
            grid.addWidget(btn, indx, 0)
            btn.clicked.connect(self.color_f)
        for indx, btn_n in enumerate(('⮮', '⮯')):
            btn = QPushButton(btn_n)
            grid.addWidget(btn, 4, indx * 2, 1, 2)
            btn.clicked.connect(self.rotate)

    def init_img(self):
        with Image.open(self.name) as im:
            im.save(self.res)

    def color_f(self):
        matrix = MATRIX[:]
        channel = self.sender().text()
        if channel == 'ALL':
            for i in MATRIX_INDEX.values():
                matrix[i] = 1
        else:
            matrix[MATRIX_INDEX[channel]] = 1

        with Image.open(self.name) as im:
            im = im.convert('RGB', matrix)
            im.save(self.res)
            self.img.setPixmap(QPixmap(self.res))

    def rotate(self):
        rot = self.sender().text()
        angle = 90 if rot == '⮮' else -90
        with Image.open(self.name) as im, Image.open(self.res) as col:
            im = im.rotate(self.angle + angle)
            im.save(self.name, quality=100)
            col = col.rotate(self.angle + angle)
            col.save(self.res, quality=100)
            self.img.setPixmap(QPixmap(self.res))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
