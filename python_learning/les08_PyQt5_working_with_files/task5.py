import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QStatusBar,
    QSpinBox,
    QDoubleSpinBox,
    QLabel,
    QPushButton,
    QLineEdit
)


class EmptyFile(Exception):
    pass


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350, 200)
        vlayout = QVBoxLayout()
        self.setLayout(vlayout)
        hlayout = QHBoxLayout()
        hlayout.addWidget(QLabel('File name:'), 0)
        self.file_name = QLineEdit()
        hlayout.addWidget(self.file_name, 1)
        self.btn = QPushButton('Calculate')
        self.btn.clicked.connect(self.calculate)
        hlayout.addWidget(self.btn)
        vlayout.addLayout(hlayout, 0)
        flayout1 = QFormLayout()
        self.max_val = QSpinBox()
        self.max_val.setReadOnly(True)
        self.max_val.setMaximum(999999999)
        flayout1.addRow(QLabel('Max value:'), self.max_val)
        vlayout.addLayout(flayout1, 1)
        flayout2 = QFormLayout()
        self.min_val = QSpinBox()
        self.min_val.setReadOnly(True)
        self.min_val.setMaximum(999999999)
        flayout2.addRow(QLabel('Min value:'), self.min_val)
        vlayout.addLayout(flayout2, 2)
        flayout3 = QFormLayout()
        self.mid_val = QDoubleSpinBox()
        self.mid_val.setReadOnly(True)
        self.mid_val.setMaximum(999999999)
        flayout3.addRow(QLabel('Average value:'), self.mid_val)
        vlayout.addLayout(flayout3, 3)
        self.statusbar = QStatusBar()
        # self.statusbar.showMessage('Message')
        vlayout.addWidget(self.statusbar, 4)

    def calculate(self):
        file_name = self.file_name.text()
        if '.' in file_name and (ext := file_name.split('.')[1]) != 'txt':
            # Написать на statusbar invalid data format
            self.statusbar.showMessage(f'''nonexistent file: '{ext}' ''')
            return None
        try:
            calculate(file_name, self.max_val, self.min_val, self.mid_val)
        except FileNotFoundError:
            self.statusbar.showMessage(f'''file: '{file_name}' not found''')
        except EmptyFile:
            self.statusbar.showMessage('Empty file')
        except ValueError:
            self.statusbar.showMessage('invalid data format')


def calculate(f_name: str, max_val, min_val, mid_val):
    with (open(f_name, 'r', encoding='utf-8') as inpf,
          open('output.txt', 'w', encoding='utf-8') as outf):
        if inpf.readline():  # Если файл не пустой:
            inpf.seek(0)
            lst_num = []
            # Записываем все цифры из файла в список
            for line in inpf:
                lst_num.extend(map(int, line.split()))
            max_v = max(lst_num)
            min_v = min(lst_num)
            middl_v = sum(lst_num) / len(lst_num)
            max_val.setValue(max_v)
            min_val.setValue(max_v)
            mid_val.setValue(middl_v)
            outf.write(f'{max_v}\n')
            outf.write(f'{min_v}\n')
            outf.write(f'{middl_v}')
        else:  # Фаил пустой!
            raise EmptyFile


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
