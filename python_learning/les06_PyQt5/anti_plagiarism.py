from random import seed
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QDoubleSpinBox,
    QTextEdit,
    QPushButton,
    QStatusBar,
    QFormLayout,
    QGridLayout
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Антиплагиат')
        
        grid = QGridLayout()
        self.setLayout(grid)

        form = QFormLayout()
        grid.addLayout(form, 0, 0, 1, 2)

        self.spnbx = QDoubleSpinBox()
        form.addRow(QLabel('Порог срабатывания(%)   '), self.spnbx)
        
        self.txtedit1 = QTextEdit()
        self.txtedit2 = QTextEdit()

        grid.addWidget(QLabel('Текст 1'), 1, 0)
        grid.addWidget(QLabel('Текст 2'), 1, 1)

        grid.addWidget(self.txtedit1, 2, 0)
        grid.addWidget(self.txtedit2, 2, 1)

        btn = QPushButton('Сравнить')
        grid.addWidget(btn, 3, 0, 1, 2)

        self.statusbar = QStatusBar()
        grid.addWidget(self.statusbar, 4, 0, 1, 2)

        self.statusbar.showMessage('Message Show')

        btn.clicked.connect(self.txt_eq)

    def txt_eq(self):
        txt1 = self.txtedit1.toPlainText()
        txt2 = self.txtedit2.toPlainText()
        
        len_small_txt = min(map(len, (txt1, txt2)))
        cnt = 0
        for i in range(len_small_txt):
            if txt1[i] == txt2[i]:
                cnt += 1

        if len_small_txt > 0:
            percent = round(((cnt / len_small_txt) * 100), 2)
            self.statusbar.showMessage(f'Текст похож на: {percent} %')

            if percent > float('.'.join(self.spnbx.text().split(','))):
                self.statusbar.setStyleSheet('background-color:red;')
            else:
                self.statusbar.setStyleSheet('background-color:green;')
        else:
            self.statusbar.showMessage('Введите текст')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())