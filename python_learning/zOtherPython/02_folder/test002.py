import sys
# from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QStatusBar
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Оплата премиум подписки')

        grid = QGridLayout()
        self.setLayout(grid)

        lbl = QLabel('Введите номер карты: ')
        grid.addWidget(lbl, 0, 0)

        self.ln_edit = QLineEdit()
        self.ln_edit.setInputMask('9999999999999999')
        # volidator = QIntValidator(0, 999999999, self)
        # self.ln_edit.setValidator(volidator)
        grid.addWidget(self.ln_edit, 1, 0, 1, 3)

        btn = QPushButton('Оплать')
        grid.addWidget(btn, 2, 1, 1, 1)

        btn.clicked.connect(self.pay)

        self.sts_bar = QStatusBar()
        grid.addWidget(self.sts_bar, 3, 0, 1, 3)

    def pay(self):
        print(self.ln_edit.text())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
