import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QTableWidget, QTableWidgetItem,
    QAbstractItemView, QGridLayout
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 900, 11, 25]

        self.table = QTableWidget()
        grid.addWidget(self.table, 0, 0)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(
            QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(
            QAbstractItemView.SelectRows)
        self.table.setSortingEnabled(True)
        
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        for i, elem in enumerate(lst):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, elem)
            self.table.setItem(i, 0, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
