import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QListWidget,
    QLineEdit,
    QPushButton,
    QLabel,
    QTimeEdit,
    QCalendarWidget)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Мини планеровщик')
        self.setGeometry(200, 200, 700, 400)
        grid = QGridLayout()
        self.setLayout(grid)

        self.time_edit = QTimeEdit()
        self.calendar = QCalendarWidget()
        self.line_edit = QLineEdit()
        btn = QPushButton('Добавить событие')
        self.lst_widget = QListWidget()

        grid.addWidget(self.time_edit, 0, 0)
        grid.addWidget(self.calendar, 1, 0)
        grid.addWidget(self.line_edit, 2, 0)
        grid.addWidget(btn, 3, 0)
        grid.addWidget(self.lst_widget, 0, 1, 3, 1)

        btn.clicked.connect(self.add_event)

    def add_event(self):
        str1 = '-'.join(map(str, self.calendar.selectedDate().getDate()))
        str2 = self.time_edit.text()
        str3 = (f' - {self.line_edit.text()}' if self.line_edit.text() else '')
        res = f'{str1} {str2}{str3}'
        if str3:
            self.lst_widget.addItem(res)
        print(res)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
