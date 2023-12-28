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
    QHeaderView, QFileDialog,
    QFrame
)


class FormPeopleData(QWidget):
    def __init__(self, data_hotel,
                 dct_cities: dict,
                 id_hotel, outer_window,
                 selected_city,
                 cursor: sqlite3.Cursor,
                 db_connection: sqlite3.Connection):
        super().__init__()
        style = """
        QLable {
            font-size: 30px;
        }"""
        self.setStyleSheet(style)

        self.setWindowTitle(f'запись человека в {data_hotel[0]}')
        self.setMinimumSize(200, 300)

        self.data_hotel = data_hotel
        self.dct_cities = dct_cities
        self.id_hotel = id_hotel
        self.outer_window = outer_window
        self.selected_city = selected_city
        self.cur = cursor
        self.db_conn = db_connection

        grid = QGridLayout()
        self.setLayout(grid)

        self.lbl_err = QLabel('')
        grid.addWidget(self.lbl_err, 0, 0, 1, 3)

        form = QFormLayout()
        grid.addLayout(form, 1, 0, 4, 3)

        self.lbl_name = QLineEdit()
        form.addRow('имя: ', self.lbl_name)
        self.lbl_sur_name = QLineEdit()
        form.addRow('фамилия: ', self.lbl_sur_name)
        self.city = QComboBox()
        for i in dct_cities.values():
            self.city.addItem(i)
        form.addRow('город проживания: ', self.city)
        self.days = QSpinBox()
        form.addRow('дни аренды: ', self.days)
        self.lbl_many = QLabel()
        self.lbl_many.setFrameShape(QFrame.Box)
        form.addRow('цена аренды: ', self.lbl_many)

        self.btn_close = QPushButton('отмена')
        self.btn_close.clicked.connect(self.close)
        grid.addWidget(self.btn_close, 4, 0)

        self.btn_add = QPushButton('запись')
        self.btn_add.clicked.connect(self.add_people)
        grid.addWidget(self.btn_add, 4, 2)

        self.days.valueChanged.connect(self.summ_print)

    def add_people(self):
        if ((name := self.lbl_name.text()) != 0 and
            (surname := self.lbl_sur_name.text()) != 0 and
                self.days.value() != 0):
            # запись
            full_name = ' '.join((name, surname))
            cod = self.cur.execute(
                SQL_GET_VISA, (self.city.currentText(),)).fetchone()[0]
            self.cur.execute(SQL_INSERT_MAN, (full_name, cod, self.id_hotel))
            self.db_conn.commit()
            self.cur.execute(SQL_UPDATE_ONE_GUEST, (self.id_hotel,))
            self.db_conn.commit()
            self.close()
        else:
            self.lbl_err.setText('заолните все поля')

    def summ_print(self):
        kooficent = 1
        if self.selected_city == self.city.currentText():
            kooficent = 0.6

        res = int((int(self.data_hotel[1]) * self.days.value()) * kooficent)

        self.lbl_many.setText(str(res))

    def closeEvent(self, event):
        self.outer_window.setEnabled(True)
        self.outer_window.change_city()


class TablePeoplesInHotels(QTableWidget):
    def __init__(
            self, name_hotel, people: list,
            dct_cities, id_hotel, outer_window,
            cursor: sqlite3.Cursor,
            db_connection: sqlite3.Connection):
        super().__init__()

        self.outer_window = outer_window
        self.people = people
        self.dct_cities = dct_cities
        self.hotel_id = id_hotel
        self.cur = cursor
        self.db_conn = db_connection

        self.setWindowTitle(f'люди в {name_hotel}')
        self.setMinimumSize(374, 500)

        grid = QGridLayout()
        self.setLayout(grid)

        self.btn_delete = QPushButton('выселить')
        grid.addWidget(self.btn_delete, 0, 0, Qt.AlignBottom)

        self.setColumnCount(2)
        self.setHorizontalHeaderItem(0, QTableWidgetItem('имя'))
        self.setHorizontalHeaderItem(1, QTableWidgetItem('город'))
        # ...
        # не редактируются
        self.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        # ?
        self.setDragEnabled(False)
        self.setDragDropOverwriteMode(False)
        # уберает выделение
        self.setSelectionMode(
            QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(
            QAbstractItemView.SelectRows)
        # растягивает заголовки
        self.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)

        self.insert_table()

        self.btn_delete.clicked.connect(self.delete)

    def delete(self):
        # выбран пункт таблицы и таблица не пуста
        if len((select := [i.text() for i in self.selectedItems()])) != 0:
            # удаление из  визуальной таблицы
            for i, v in enumerate(self.people):
                if v[0] == select[0]:
                    self.people.pop(i)
                    break

            # удаление из отеля в базе данных
            self.cur.execute(SQL_DELETE_ONE_GUEST,
                             (self.hotel_id,))
            self.db_conn.commit()
            self.cur.execute(SQL_CLEAR_HOTEL_ID,
                             (self.hotel_id, select[0]))
            self.db_conn.commit()

            # в конце обнавляем визуальную таблицу
            self.insert_table()

    def insert_table(self):
        self.setRowCount(0)
        for i, row in enumerate(self.people):
            self.setRowCount(self.rowCount() + 1)
            self.setItem(i, 0, QTableWidgetItem(row[0]))
            self.setItem(i, 1, QTableWidgetItem(self.dct_cities[row[1]]))

    def closeEvent(self, event):
        self.outer_window.setEnabled(True)
        self.outer_window.change_city()


class Window2(QWidget):
    def __init__(self, db_name):
        super().__init__()
        DB_PATH = db_name
        self.setWindowTitle('second window')
        self.setMinimumSize(700, 500)

        # подключение к базе данных
        self.db_conn = sqlite3.connect(DB_PATH)
        self.cur = self.db_conn.cursor()
        self.cities = {
            tpl[1]: tpl[0]
            for tpl in self.cur.execute(SQL_GET_CITIES).fetchall()}

        # основная сетка
        grid = QGridLayout()
        self.setLayout(grid)
        self.btn_add = QPushButton('Запись')
        self.btn_review = QPushButton('выселение')
        # self.btn_add.clicked.connect()
        self.btn_add.clicked.connect(self.add)
        self.btn_review.clicked.connect(self.review)

        self.btn_add.setEnabled(False)
        # self.btn_review.setEnabled(False)
        grid.addWidget(self.btn_add, 0, 0, 1, 5)
        grid.addWidget(self.btn_review, 0, 6, 1, 9)

        self.lbl_err = QLabel()
        grid.addWidget(self.lbl_err, 2, 0, 1, 5)
        self.btn_group = QButtonGroup()
        self.btn_free = QRadioButton('свободные')
        self.btn_busy = QRadioButton('занятые')
        self.btn_free.toggle()
        self.btn_free.clicked.connect(self.change_city)
        self.btn_busy.clicked.connect(self.change_city)
        self.btn_group.addButton(self.btn_free)
        self.btn_group.addButton(self.btn_busy)
        grid.addWidget(self.btn_free, 2, 6, 1, 4)
        grid.addWidget(self.btn_busy, 2, 13, 1, 2)

        self.table_cities = QTableWidget()
        self.table_hotels = QTableWidget()
        grid.addWidget(self.table_cities, 3, 0, 7, 5)
        grid.addWidget(self.table_hotels, 3, 6, 7, 9)

        self.table_hotels.setColumnCount(1)

        # размеры таблицы table_hotels
        self.table_hotels.setColumnCount(3)
        self.table_hotels.setHorizontalHeaderItem(
            0, QTableWidgetItem('название'))
        self.table_hotels.setHorizontalHeaderItem(
            1, QTableWidgetItem('свободно мест'))
        self.table_hotels.setHorizontalHeaderItem(
            2, QTableWidgetItem('цена'))
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
        self.table_hotels.horizontalHeader().setSectionResizeMode(
            2, QHeaderView.ResizeToContents)
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

        cyties_names = self.cities.values()
        for i, row in enumerate(cyties_names):
            self.table_cities.setRowCount(
                self.table_cities.rowCount() + 1)
            self.table_cities.setItem(
                i, 0, QTableWidgetItem(str(row)))

        self.table_cities.cellClicked.connect(self.change_city)
        # self.btn_group.buttonToggled.connect(self.foo)

    def change_city(self):
        # если город выбран
        self.lbl_err.setText('')
        if (selected_city := self.table_cities.selectedItems()):
            selected_city = selected_city[0].text()
            self.selected_city = selected_city

            # кнопка free_hotels
            if self.btn_free.isChecked():
                self.btn_add.setEnabled(True)
                # self.btn_review.setEnabled(False)
                hotels_data = self.cur.execute(
                    SQL_GET_FREE_HOTELS,
                    (selected_city,)).fetchall()
            # кнопка busy hotels
            else:
                # self.btn_review.setEnabled(True)
                self.btn_add.setEnabled(False)
                hotels_data = self.cur.execute(
                    SQL_GET_BUSY_HOTELS,
                    (selected_city,)).fetchall()

            self.insert_hotels(hotels_data, selected_city)

    def insert_hotels(self, lst_rows: list[tuple], selected_city: str):
        self.table_hotels.setSortingEnabled(False)

        self.table_hotels.setRowCount(0)
        for i, row in enumerate(lst_rows):
            self.table_hotels.setRowCount(
                self.table_hotels.rowCount() + 1)
            for j, col in enumerate(row):
                item = QTableWidgetItem()
                if j == 0:
                    item.setText(col)
                    self.table_hotels.setItem(i, j, item)
                    # i, j, QTableWidgetItem(str(col)))
                elif j in (1, 2):
                    item.setData(Qt.DisplayRole, int(col))
                    self.table_hotels.setItem(i, j, item)
                    # i, j, QTableWidgetItem(str(int(col * kooficent))))

        self.table_hotels.setSortingEnabled(True)

    def add(self):
        if len(data_hotel := self.table_hotels.selectedItems()) != 0:
            # получение инфо о выбраном отеле из таблицы
            data_hotel = [int(el.text()) if el.text().isdigit()
                          else el.text()
                          for el in data_hotel[::2]]

            # получение ид этого отеля
            id_hotel = self.cur.execute(
                SQL_GET_HOTEL_ID,
                (data_hotel[0], data_hotel[1], self.selected_city)
            ).fetchone()[0]
            tpl_people = self.cur.execute(
                GET_PEOPLE_FROM_HOTEL, (id_hotel,)).fetchall()
            print(data_hotel, tpl_people)
            print(self.cities)
            # открытие формы с записью
            self.add_people_form = FormPeopleData(
                data_hotel, self.cities, id_hotel,
                self, self.selected_city, self.cur, self.db_conn
            )
            self.add_people_form.show()
            self.setEnabled(False)
        else:
            self.lbl_err.setText('Выберите отель')

    def review(self):
        if len(data_hotel := self.table_hotels.selectedItems()) != 0:
            # получение инфо о выбраном отеле из таблицы
            data_hotel = [int(el.text()) if el.text().isdigit()
                          else el.text()
                          for el in data_hotel[::2]]

            # получение ид этого отеля
            id_hotel = self.cur.execute(
                SQL_GET_HOTEL_ID,
                (data_hotel[0], data_hotel[1], self.selected_city)
            ).fetchone()[0]
            tpl_people = self.cur.execute(
                GET_PEOPLE_FROM_HOTEL, (id_hotel,)).fetchall()
            print(data_hotel, tpl_people)
            print(self.cities)
            # открытие формы с таблицей
            self.open_table = TablePeoplesInHotels(
                data_hotel[0], tpl_people, self.cities,
                id_hotel, self, self.cur, self.db_conn)
            self.open_table.show()
            self.setEnabled(False)
        else:
            self.lbl_err.setText('Выберите отель')

    def closeEvent(self, event) -> None:
        self.db_conn.close()
        # os.remove(DB_PATH)


class GenerationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('First form')
        self.setFixedSize(300, 0)
        vertical_layout = QVBoxLayout()
        self.setLayout(vertical_layout)
        self.lbl_error = QLabel()
        vertical_layout.addWidget(self.lbl_error)
        self.name_db = QLineEdit()
        form_name_db = QFormLayout()
        form_name_db.addRow('имя базы:', self.name_db)
        vertical_layout.addLayout(form_name_db)

        form_layout = QFormLayout()
        vertical_layout.addLayout(form_layout)

        create_btn = QPushButton('сгенерировать базу данных')
        vertical_layout.addWidget(create_btn)
        create_btn.clicked.connect(self.create_table)

        self.spin_bx1 = QSpinBox()
        self.spin_bx1.setMinimum(4)
        self.spin_bx1.setMaximum(20)
        form_layout.addRow('кол. городов', self.spin_bx1)
        self.spin_bx2 = QSpinBox()
        self.spin_bx2.setMinimum(1)
        self.spin_bx2.setMaximum(20)
        form_layout.addRow(
            'мин. кол. отелей\nв каждом из городов', self.spin_bx2)
        self.spin_bx3 = QSpinBox()
        self.spin_bx3.setMinimum(12)
        self.spin_bx3.setMaximum(20)
        form_layout.addRow(
            'макс. кол. отелей\nв каждом из городов', self.spin_bx3)
        self.spin_bx4 = QSpinBox()
        self.spin_bx4.setMinimum(1)
        self.spin_bx4.setMaximum(20)
        form_layout.addRow(
            'мин. кол. мест\nв каждом из отелей', self.spin_bx4)
        self.spin_bx5 = QSpinBox()
        self.spin_bx5.setMinimum(5)
        self.spin_bx5.setMaximum(20)
        form_layout.addRow(
            'макс. кол. мест\nв каждом из отелей', self.spin_bx5)
        self.spin_bx6 = QSpinBox()
        self.spin_bx6.setMinimum(1200)
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
            DB_PATH = f'{self.name_db.text()}.db'
            db_conn = sqlite3.connect(DB_PATH)
            cur = db_conn.cursor()
            cur.executescript(SQL_CREATE_DB)
            db_conn.commit()
            for sql_query in incert_sql_queries:
                cur.execute(sql_query)
                db_conn.commit()
            db_conn.close()

            self.not_delate_db = True
            self.window2 = Window2(DB_PATH)
            # self.window2.setStyleSheet(self.style0)
            self.window2.show()
            self.close()


class Start_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 0)
        style = """QPushButton {padding: 14px;}"""
        self.setStyleSheet(style)
        vlayout = QVBoxLayout()
        self.setLayout(vlayout)
        self.btn_open = QPushButton('открыть базу данных')
        self.btn_create = QPushButton('сгенирировать базу данных')
        vlayout.addWidget(self.btn_open)
        vlayout.addWidget(self.btn_create)

        self.btn_create.clicked.connect(self.open_generation)
        self.btn_open.clicked.connect(self.open_db_func)

    def open_generation(self):
        self.generate_form = GenerationForm()
        self.generate_form.show()
        self.close()

    def open_db_func(self):
        self.name = QFileDialog.getOpenFileName(
            self, 'Выбрать базу', '')[0]
        # print(self.name)
        self.window2 = Window2(self.name)
        self.window2.show()
        self.close()


def exception_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    window = Start_Window()
    window.show()
    # window = GenerationForm()
    # window.show()
    sys.exit(app.exec())
