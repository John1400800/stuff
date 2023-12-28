import sys

from PIL import Image

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QGridLayout, QHBoxLayout, QMainWindow, QWidget,
    QPushButton, QLabel, QFormLayout, QFileDialog
)

MATRIX_INDEX = {'R': 0, 'G': 5, 'B': 10}
MATRIX = [0, 0, 0, 0,
          0, 0, 0, 0,
          0, 0, 0, 0]


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PIL 2.0')
        widget = QWidget()
        layout = QGridLayout()
        child_layout = QHBoxLayout()
        layout.addLayout(child_layout, 4, 0, 1, 2)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.name = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '')[0]
        self.res = 'res1.jpg'
        self.image = QLabel()
        self.image.setPixmap(QPixmap(self.name))
        self.init_image()
        layout.addWidget(self.image, 0, 1, 4, 1)
        for i, text in enumerate(('R', 'G', 'B', 'ALL')):
            btn = QPushButton(text)
            btn.clicked.connect(self.leave_channels)
            layout.addWidget(btn, i, 0)

        for i, (text, d) in enumerate((('Против часовой стрелке', +1),
                                       ('По часовой стрелке', -1))):
            btn = QPushButton(text)
            btn.clicked.connect(self.rotate(d))
            child_layout.addWidget(btn)

    def init_image(self):
        with Image.open(self.name) as im:
            im.save(self.res)

    def leave_channels(self):
        matrix = MATRIX[:]
        channel = self.sender().text()  # type: ignore
        if channel == 'ALL':
            for i in MATRIX_INDEX.values():
                matrix[i] = 1
        else:
            matrix[MATRIX_INDEX[channel]] = 1

        with Image.open(self.name) as im:
            im = im.convert('RGB', matrix)  # type: ignore
            im.save(self.res)
            self.image.setPixmap(QPixmap(self.res))

    def rotate(self, direction):
        def inner():
            with (Image.open(self.res) as im,
                  Image.open(self.name) as ref):
                im = im.rotate(180 - 90 * direction)
                im.save(self.res, quality=100)
                ref = ref.rotate(180 - 90 * direction)
                ref.save(self.name, quality=100)
                self.image.setPixmap(QPixmap(self.res))
        return inner


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
