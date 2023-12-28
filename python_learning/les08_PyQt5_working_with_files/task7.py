import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QPlainTextEdit,
    QPushButton,
    QLineEdit,
    QFrame,
    QStatusBar
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)
        self.statusbar = QStatusBar()
        self.line_edit = QLineEdit()
        self.txt_edit = QPlainTextEdit()
        self.txt_edit.viewport().setProperty('cursor', QCursor(Qt.IBeamCursor))
        grid.addWidget(self.statusbar, 9, 0, 1, 2)
        grid.addWidget(self.line_edit, 0, 0)
        grid.addWidget(self.txt_edit, 0, 1, 8, 1)
        for i, el in enumerate(
            (
                'Создать новый',
                'Сохранить файл',
                'Открыть фаил'
            )
        ):
            btn = QPushButton(el)
            grid.addWidget(btn, i + 1, 0)
            btn.clicked.connect(self.action)

    def action(self):
        btn_name = self.sender().text()
        print(btn_name)
        file_name = self.line_edit.text()
        ext = file_name.split('.')[1] if '.' in file_name else None
        if btn_name == 'Создать новый':
            self.txt_edit.clear()
            if not ext:
                self.statusbar.showMessage(
                    'Введите расширение !')
            elif file_name.split('.')[1] != 'txt':
                self.statusbar.showMessage(
                    'можно создавать только текстовые файлы !')
            else:
                if not is_file(file_name):
                    make_new_file(file_name)
                    self.statusbar.showMessage(f'Файл "{file_name}" создан')
                else:
                    self.statusbar.showMessage(
                        f'Файл уже существует !',
                        3000
                    )
        if btn_name == 'Сохранить файл':
            if is_file(file_name):
                with open(file_name, 'w', encoding='utf-8') as wfile:
                    txt_edited = self.txt_edit.toPlainText()
                    wfile.write(txt_edited)
            else:
                self.statusbar.showMessage(
                    'Сохранять в несозданный файл нельзя'
                )
        if btn_name == 'Открыть фаил':
            try:
                with open(file_name, 'r', encoding='utf-8') as rfile:
                    txt_in_file = rfile.read()
                    if txt_in_file:
                        self.txt_edit.setPlainText(txt_in_file)
                        self.statusbar.showMessage(f'Файл {file_name}')
                    else:
                        self.statusbar.showMessage('Файл пуст')
            except FileNotFoundError:
                self.statusbar.showMessage('Файл не найден')


def is_file(f_name):
    try:
        with open(f_name) as file:
            pass
    except:
        return False  # Файла нет
    else:
        return True  # Файл есть


def make_new_file(f_name: str):
    with open(f_name, 'w', encoding='utf-8') as new_f:
        pass


def save_File(f_name):
    pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
