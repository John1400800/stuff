import sys
import random
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QGridLayout)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Form')
        # self.setGeometry(300, 300, 500, 500)
        grid = QGridLayout()
        self.setLayout(grid)

        n = int(input())
        mass = [random.choices(' #', k=n) for i in range(n)]

        if mass:
            for row in range(n):
                for col in range(n):
                    icon = QLineEdit(mass[row][col])
                    icon.setEnabled(False)
                    grid.addWidget(icon, row, col)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
