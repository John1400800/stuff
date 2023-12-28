import sys
from random import randrange
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QFormLayout,
    QPushButton,
    QLabel,
    QFrame
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(
            "random char (создайте фаил с именем: 'your_file.txt')")
        self.setFixedSize(600, 0)
        f_layaut = QFormLayout()
        self.setLayout(f_layaut)
        self.btn = QPushButton('Получить')
        self.lbl = QLabel()
        self.lbl.setFrameShape(QFrame.Box)
        f_layaut.addRow(self.btn, self.lbl)
        self.btn.clicked.connect(self.random_char)

    def random_char(self):
        with open('your_file.txt', 'r', encoding='utf-8') as f:
            if f.readline():
                f.seek(0)
                line = next(f)
                for n, al in enumerate(f, 2):
                    if randrange(n):
                        continue
                    line = al
                self.lbl.setText(line.rstrip())
            else:
                self.lbl.setText('фаил пуст')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
