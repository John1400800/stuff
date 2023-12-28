import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QRadioButton,
    QGridLayout,
    QSizePolicy,
    QButtonGroup,
    QLabel
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Крестики-нолики')
        self.setGeometry(300, 300, 400, 400)
        grid = QGridLayout()
        self.setLayout(grid)

        self.lbl = QLabel()

        self.btn_grup = QButtonGroup(self)

        self.rbtn1 = QRadioButton('X')
        self.rbtn2 = QRadioButton('O')

        self.btn_grup.addButton(self.rbtn1)
        self.btn_grup.addButton(self.rbtn2)

        self.rbtn1.toggle()
        grid.addWidget(self.rbtn1, 0, 0)
        grid.addWidget(self.rbtn2, 0, 1)
        grid.addWidget(self.lbl, 4, 0)

        self.tpl = (QPushButton(' '), QPushButton(' '), QPushButton(' '),
                    QPushButton(' '), QPushButton(' '), QPushButton(' '),
                    QPushButton(' '), QPushButton(' '), QPushButton(' '))

        for i, btn in enumerate(self.tpl):
            grid.addWidget(btn, i // 3 + 1, i % 3)
            sizepolicy = QSizePolicy(
                QSizePolicy.Minimum,
                QSizePolicy.Minimum)

            btn.setSizePolicy(sizepolicy)
            btn.setFont(QFont('Arial', 60))
            btn.setStyleSheet("font-weight: bold; border: 1px solid red; border-radius: 20px; margin: 10px;")
            btn.clicked.connect(self.logic)

        self.cntf = 1

    def logic(self):
        btn = self.sender()
        btn.setEnabled(False)

        if self.cntf:
            self.f = self.btn_grup.checkedButton().text()
            self.cntf = 0

        btn.setText(self.f)

        self.f = ('X' if self.f == 'O' else 'O')
        self.rbtn1.setEnabled(False)
        self.rbtn2.setEnabled(False)

        for i in range(1, 4):
            n = [i.text() for i in self.tpl[3 * (i - 1):3 * i]]
            if len(set(n)) == 1 and len(n) == 3 and ''.join(set(n)) != ' ':
                self.lbl.setText('Выйграл: ' + ''.join(set(n)))
                self.end()

        for i in range(3):
            n = (self.tpl[0 + i], self.tpl[3 + i], self.tpl[6 + i])
            n = [i.text() for i in n]
            if len(set(n)) == 1 and len(n) == 3 and ''.join(set(n)) != ' ':
                self.lbl.setText('Выйграл: ' + ''.join(set(n)))
                self.end()
        # 0, 4, 8; 2, 4, 6

        n = [i.text() for i in (self.tpl[0], self.tpl[4], self.tpl[8])]
        if len(set(n)) == 1 and len(n) == 3 and ''.join(set(n)) != ' ':
            self.lbl.setText('Выйграл: ' + ''.join(set(n)))
            self.end()

        n = [i.text() for i in (self.tpl[2], self.tpl[4], self.tpl[6])]
        if len(set(n)) == 1 and len(n) == 3 and ''.join(set(n)) != ' ':
            self.lbl.setText('Выйграл: ' + ''.join(set(n)))
            self.end()

        n = [i.text() for i in self.tpl]
        if len(n) == 9 and ' ' not in n:
            self.lbl.setText('Ничья')
            self.end()

    def end(self):
        for i in self.tpl:
            # i.setText(' ')
            i.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
