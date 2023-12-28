import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QRadioButton,
    QPushButton,
    QLabel,
    QGridLayout,
    QButtonGroup
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Текстовый флаг')
        self.setGeometry(200, 200, 700, 300)

        grid = QGridLayout()
        self.setLayout(grid)

        grp1 = QButtonGroup(self)
        grp2 = QButtonGroup(self)
        grp3 = QButtonGroup(self)
        self.btn_grps = [grp1, grp2, grp3]

        for i1, head in enumerate((
                'Цвет№1\n',
                'Цвет№2\n',
                'Цвет№3\n')):
            name = QLabel(head)
            name.setFont(QFont('Arial', 18))
            name.setStyleSheet("font-weight: bold")
            name.setAlignment(Qt.AlignBottom)
            grid.addWidget(name, 0, i1)

            for i2, r in enumerate(('Синий', 'Красный', 'Зелёный', 'Жёлтый')):
                btn = QRadioButton(r)
                btn.toggle() if i2 == 0 else 0
                self.btn_grps[i1].addButton(btn)
                grid.addWidget(btn, i2 + 1, i1)

            self.lbl_res = QLabel()
            self.lbl_res.setAlignment(Qt.AlignLeft)
            self.lbl_res.setFont(QFont('Arial', 11))
            self.lbl_res.setStyleSheet("font-weight: bold")
            grid.addWidget(self.lbl_res, 6, 0, 6, 3)
            btn_res = QPushButton('Cделать флаг')
            grid.addWidget(btn_res, 5, 2)
            btn_res.clicked.connect(self.make_flag)
    
    def make_flag(self):
        self.lbl_res.setText(
            'Цвета: '
            f'{self.btn_grps[0].checkedButton().text()}, '
            f'{self.btn_grps[1].checkedButton().text()}и '
            f'{self.btn_grps[2].checkedButton().text()}'
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
    