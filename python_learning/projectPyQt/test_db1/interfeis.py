import os
import sys
from aditional_func import *
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QVBoxLayout, QFormLayout, QLineEdit,
    QSpinBox, QGridLayout, QComboBox,
    QLabel, QTableWidget, QStatusBar,
    QTableWidgetItem, QAbstractItemView,
    QButtonGroup, QRadioButton,
    QHeaderView
)


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('second window')
        self.setMinimumSize(700, 500)
        # можно сделать оформление
        style = """"""
        self.setStyleSheet(style)

        # подключение к базе данных
        self.db_conn = sqlite3.connect(DB_PATH)
        self.cur = self.db_conn.cursor()
        cities = {
            tpl[0]: tpl[1]
            for tpl in self.cur.execute(SQL_GET_CITIES).fetchall()}
        # основная сетка
        grid = QGridLayout()
        self.setLayout(grid)

        # размещение всего на сетке
        grid.addWidget(QLabel('name:'), 0, 0, 1, 3)
        grid.addWidget(QLabel('surname:'), 1, 0, 1, 3)
        self.line_edit_name = QLineEdit()
        self.line_edit_surname = QLineEdit()
        grid.addWidget(self.line_edit_name, 0, 3, 1, 3)
        grid.addWidget(self.line_edit_surname, 1, 3, 1, 3)
        grid.addWidget(QLabel('visa'), 0, 7, 1, 2)
        self.combo_box_visa = QComboBox()
        visa_codes = cities.values()
        for cod in visa_codes:
            self.combo_box_visa.addItem(cod)
        grid.addWidget(self.combo_box_visa, 0, 9, 1, 3)
        self.btn_add = QPushButton('снять номер')
        self.btn_add.clicked.connect(self.add_people)
        grid.addWidget(self.btn_add, 0, 12, 1, 3)

        grid.addWidget(QLabel('$:'), 1, 9, 1, 2)
        self.edit_many = QSpinBox()
        self.edit_many.setMinimum(0)
        self.edit_many.setMaximum(20000)
        grid.addWidget(self.edit_many, 1, 11, 1, 4)

        self.lbl_err = QLabel('запись')
        self.lbl_err.setAlignment(Qt.AlignCenter)
        grid.addWidget(self.lbl_err, 2, 0, 1, 6)
        self.btn_group = QButtonGroup()
        self.btn_free = QRadioButton('свободные')
        self.btn_busy = QRadioButton('занятые')
        self.btn_free.toggle()
        self.btn_free.clicked.connect(self.change_city)
        self.btn_busy.clicked.connect(self.change_city)
        self.btn_group.addButton(self.btn_free)
        self.btn_group.addButton(self.btn_busy)
        grid.addWidget(self.btn_free, 2, 6, 1, 4)
        grid.addWidget(self.btn_busy, 2, 11, 1, 4)

        self.table_cities = QTableWidget()
        self.table_hotels = QTableWidget()
        grid.addWidget(self.table_cities, 3, 0, 7, 6)
        grid.addWidget(self.table_hotels, 3, 6, 7, 9)

        # размеры таблицы table_hotels
        self.table_hotels.setColumnCount(2)
        self.table_hotels.setHorizontalHeaderItem(
            0, QTableWidgetItem('название'))
        self.table_hotels.setHorizontalHeaderItem(
            1, QTableWidgetItem('цена'))
        # ...
        # не редактируются
        self.table_hotels.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        # ?
        self.table_hotels.setDragEnabled(False)
        self.table_hotels.setDragDropOverwriteMode(False)
        # уберает выделение
        self.table_hotels.setSelectionMode(
            QAbstractItemView.SingleSelection)
        self.table_hotels.setSelectionBehavior(
            QAbstractItemView.SelectRows)
        # растягивает заголовки
        self.table_hotels.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.Stretch)
        self.table_hotels.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)
        # сортировка
        # self.table_hotels.setSortingEnabled(True)

        # размеры таблицы table_cities
        self.table_cities.setColumnCount(1)
        self.table_cities.setRowCount(0)
        self.table_cities.setHorizontalHeaderItem(
            0, QTableWidgetItem('города'))
        # ...
        # не редактируются
        self.table_cities.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        # ?
        self.table_cities.setDragEnabled(False)
        self.table_cities.setDragDropOverwriteMode(False)
        # уберает выделение
        self.table_cities.setSelectionMode(
            QAbstractItemView.SingleSelection)
        # растягивает заголовки
        self.table_cities.horizontalHeader().setStretchLastSection(True)

        cyties_names = cities.keys()
        for i, row in enumerate(cyties_names):
            self.table_cities.setRowCount(
                self.table_cities.rowCount() + 1)
            self.table_cities.setItem(
                i, 0, QTableWidgetItem(str(row)))

        self.table_cities.cellClicked.connect(self.change_city)
        # self.btn_group.buttonToggled.connect(self.foo)

    def change_city(self):
        # если город выбран
        if (selected_city := self.table_cities.selectedItems()):
            selected_city = selected_city[0].text()
            self.selected_city = selected_city

            # кнопка free_hotels
            if self.btn_free.isChecked():
                hotels_data = self.cur.execute(
                    SQL_GET_FREE_HOTELS,
                    (selected_city,)).fetchall()
            # кнопка busy hotels
            else:
                hotels_data = self.cur.execute(
                    SQL_GET_BUSY_HOTELS,
                    (selected_city,)).fetchall()

            self.insert_hotels(hotels_data, selected_city)

    def insert_hotels(self, lst_rows: list[tuple], selected_city: str):
        self.table_hotels.setSortingEnabled(False)

        self.table_hotels.setRowCount(0)

        kooficent = 1
        self.selected_visa = self.cur.execute(
            SQL_GET_VISA, (selected_city,)).fetchall()[0][0]
        if self.selected_visa == self.combo_box_visa.currentText():
            kooficent = 0.8

        for i, row in enumerate(lst_rows):
            self.table_hotels.setRowCount(
                self.table_hotels.rowCount() + 1)
            for j, col in enumerate(row):
                item = QTableWidgetItem()
                if j == 0:
                    item.setText(col)
                    self.table_hotels.setItem(i, j, item)
                    # i, j, QTableWidgetItem(str(col)))
                elif j == 1:
                    item.setData(Qt.DisplayRole, int(col * kooficent))
                    self.table_hotels.setItem(i, j, item)
                    # i, j, QTableWidgetItem(str(int(col * kooficent))))

        self.table_hotels.setSortingEnabled(True)

    def add_people(self):
        #  запись в свободные отели
        if self.btn_free.isChecked():
            # вписанны фамилия и имя
            if (self.line_edit_name.text().replace(' ', '') and
                    self.line_edit_surname.text().replace(' ', '')):
                # выбран отель
                if len(data_hotel := self.table_hotels.selectedItems()) != 0:
                    data_hotel = [int(el.text()) if el.text().isdigit()
                                  else el.text()
                                  for el in data_hotel]
                    # хватает ли денег:
                    if self.edit_many.value() >= data_hotel[1]:
                        # получение ид отеля
                        id_hotel = self.cur.execute(
                            SQL_GET_HOTEL_ID,
                            (data_hotel[0], self.selected_city)
                        ).fetchone()[0]

                        # добавления в этот отель одного гостя:
                        self.cur.execute(SQL_UPDATE_ONE_GUEST, (id_hotel,))
                        self.db_conn.commit()
                        full_name_people = (self.line_edit_name.text()
                                            + ' '
                                            + self.line_edit_surname.text())

                        # добавление в таблицу с людьми человека
                        self.cur.execute(SQL_INSERT_MAN, (full_name_people,
                                                          self.selected_visa,
                                                          id_hotel))
                        self.db_conn.commit()

                        # print(full_name_people,
                        #       self.selected_visa,
                        #       id_hotel, sep='\n')

                        self.change_city()
                        self.edit_many.clear()
                        self.line_edit_name.clear()
                        self.line_edit_surname.clear()
                        # self.combo_box_visa.clear()
                    else:
                        self.lbl_err.setText('нехватает денег')
                else:
                    self.lbl_err.setText('выберите отель')
            else:
                self.lbl_err.setText('заполните имя фамилию')
        else:
            self.lbl_err.setText('записаться в занятый отель нельзя')
                

    def closeEvent(self, event) -> None:
        self.db_conn.close()
        os.remove(DB_PATH)


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('First form')
        self.setFixedSize(300, 0)
        vertical_layout = QVBoxLayout()
        self.setLayout(vertical_layout)
        self.lbl_error = QLabel()
        vertical_layout.addWidget(self.lbl_error)

        form_layout = QFormLayout()
        vertical_layout.addLayout(form_layout)

        create_btn = QPushButton('сгенерировать базу данных')
        vertical_layout.addWidget(create_btn)
        create_btn.clicked.connect(self.create_table)

        self.spin_bx1 = QSpinBox()
        self.spin_bx1.setMinimum(1)
        self.spin_bx1.setMaximum(20)
        form_layout.addRow('кол. городов', self.spin_bx1)
        self.spin_bx2 = QSpinBox()
        # self.spin_bx2.setMinimum(1)
        self.spin_bx2.setMaximum(20)
        form_layout.addRow(
            'мин. кол. отелей\nв каждом из городов', self.spin_bx2)
        self.spin_bx3 = QSpinBox()
        self.spin_bx3.setMinimum(1)
        self.spin_bx3.setMaximum(20)
        form_layout.addRow(
            'макс. кол. отелей\nв каждом из городов', self.spin_bx3)
        self.spin_bx4 = QSpinBox()
        self.spin_bx4.setMinimum(1)
        self.spin_bx4.setMaximum(20)
        form_layout.addRow(
            'мин. кол. мест\nв каждом из отелей', self.spin_bx4)
        self.spin_bx5 = QSpinBox()
        self.spin_bx5.setMinimum(1)
        self.spin_bx5.setMaximum(20)
        form_layout.addRow(
            'макс. кол. мест\nв каждом из отелей', self.spin_bx5)
        self.spin_bx6 = QSpinBox()
        self.spin_bx6.setMinimum(1000)
        self.spin_bx6.setMaximum(12000)
        form_layout.addRow('средняя цена по отелям', self.spin_bx6)

    def create_table(self):
        num_of_cities = self.spin_bx1.value()
        average_price = self.spin_bx6.value()
        num_hotels_in_city = self.spin_bx2.value(), self.spin_bx3.value()
        num_seats_in_hotels = self.spin_bx4.value(), self.spin_bx5.value()

        try:
            incert_sql_queries = sql_insert_queries(
                make_data_dct(),
                num_of_cities,
                average_price,
                num_hotels_in_city,
                num_seats_in_hotels)
        except MinimumMoreMaximum:
            # print('минимум больше максимума')
            self.lbl_error.setText('минимум больше максимума')
        except IncorectMinimum:
            # print(
            #     'в отелях должно быть как минимум одно место')
            self.lbl_error.setText(
                'в отелях должно быть как минимум одно место')
        except ImpossibleNumCities:
            # print('нельзя сгенерировать столько городов')
            self.lbl_error.setText(
                'нельзя сгенерировать столько городов')
        else:
            self.lbl_error.setText('Генерация')
            # создание и заполнение базы данных
            db_conn = sqlite3.connect(DB_PATH)
            cur = db_conn.cursor()
            cur.executescript(SQL_CREATE_DB)
            db_conn.commit()
            for sql_query in incert_sql_queries:
                cur.execute(sql_query)
                db_conn.commit()
            db_conn.close()

            self.window2 = Window2()
            self.window2.show()
            self.close()

    def closeEvent(self, event) -> None:
        os.remove(DB_PATH)


def exception_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    window = StartWindow()
    window.show()
    sys.exit(app.exec())
