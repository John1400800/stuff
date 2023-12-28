#  ПОПРОБУЙТЕ ВВЕСТИ ВО ВТОРОЕ ПОЛЕ СНАЧАЛА БУКВЫ А ПОТО ЦИФРЫ!
import sys
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QListWidget,
    QFormLayout,
    QGridLayout
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Записная книжка')
        self.setGeometry(300, 300, 400, 400)

        grid = QGridLayout()
        self.setLayout(grid)

        form = QFormLayout()
        grid.addLayout(form, 0, 0)

        volidator = QIntValidator(0, 10**9, self)
        self.inp1, self.inp2 = QLineEdit(), QLineEdit()
        self.inp2.setValidator(volidator)

        form.addRow(QLabel('Имя: '), self.inp1)
        form.addRow(QLabel('Номер: '), self.inp2)

        btn = QPushButton('Добавить')
        grid.addWidget(btn, 0, 1)

        self.lst_widget = QListWidget()
        grid.addWidget(self.lst_widget, 1, 0, 1, 2)

        btn.clicked.connect(self.add1)

    def add1(self):
        res = f'{self.inp1.text()} {self.inp2.text()}'
        if len(res.split()) >= 2:
            self.lst_widget.addItem(res)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
