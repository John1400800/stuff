import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPlainTextEdit,
    QPushButton,
    QGridLayout,
    QFrame
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 200, 440, 340)
        grid = QGridLayout()
        self.setLayout(grid)
        self.btn = QPushButton('Загрузить сьроки')
        self.btn.clicked.connect(self.write)
        self.plain_text = QPlainTextEdit()
        self.plain_text.setFrameShape(QFrame.Box)
        self.plain_text.setFont(QFont('Arial', 9, italic=True))
        # btn.setFont(QFont('Arial', 18))
        grid.addWidget(self.btn, 0, 0, 1, 2)
        grid.addWidget(self.plain_text, 1, 0, 1, 3)

    def write(self):
        with open('lines.txt', 'r', encoding='utf-8') as inp:
            if inp.readline():
                inp.seek(0)
                lst_even, lst_odd = [], []
                for i, line in enumerate(inp):
                    if i % 2:
                        lst_even.append(line.strip())
                    else:
                        lst_odd.append(line.strip())
                res = ''.join(
                    [f'{i}\n' if i != lst_odd[-1] else i
                     for i in lst_even + lst_odd]
                )
            else:
                res = 'Фаил пуст'

        self.plain_text.setPlainText(res)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook == except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
