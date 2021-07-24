import sys
import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QDialog
from try_db import Ui_MainWindow
from dialog import Ui_Dialog


class Table(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = Db()
        self.table_films.setColumnCount(6)
        self.table_films.setHorizontalHeaderLabels(['choose', 'id', 'title', 'year', 'genre', 'duration'])
        self.btn_search.clicked.connect(self.search)
        self.fill_table(self.db.all_films())
        self.genre.addItems([''] + list(self.db.all_gen().values()))
        self.years = [str(i) for i in range(self.db.min_max_year()[0], self.db.min_max_year()[1] + 1)]
        self.year.addItems([''] + self.years)
        self.duration_max.setMaximum(200)
        self.duration_min.setMaximum(199)
        self.table_films.itemChanged.connect(self.changed)
        self.btn_add.clicked.connect(self.add_new_film)
        self.btn_delete.clicked.connect(self.delete_films)
        self.selected_films = list()
        self.editing = False

    def fill_table(self, film_list: list):
        self.editing = True
        self.table_films.setRowCount(len(film_list))
        for i in range(len(film_list)):
            genre = self.db.get_genre(film_list[i][3])
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(False)
            self.table_films.setItem(i, 0, checkbox)
            id_item = QTableWidgetItem(str(film_list[i][0]))
            id_item.setFlags(Qt.ItemIsEnabled)
            self.table_films.setItem(i, 1, id_item)
            self.table_films.setItem(i, 2, QTableWidgetItem(str(film_list[i][1])))
            self.table_films.setItem(i, 3, QTableWidgetItem(str(film_list[i][2])))
            self.table_films.setItem(i, 4, QTableWidgetItem(genre))
            self.table_films.setItem(i, 5, QTableWidgetItem(str(film_list[i][4])))
        self.editing = False

    def search(self):
        options = dict()
        print("начало поиска?")
        options['title'] = self.title.text()
        print("начало поиска?")
        options['genre'] = self.genre.currentText()
        print("начало поиска?")
        options['year'] = self.year.currentText()
        options['dur_min'] = self.duration_min.value()
        options['dur_max'] = self.duration_max.value()

        new_films = self.db.get_films(options)
        self.fill_table(new_films)
        print("ставлю на поиск")

    def changed(self, item: QTableWidgetItem):
        if not self.editing:
            row = item.row()
            types = {0: 'checkbox', 1: 'id', 2: 'title', 3: 'year', 4: 'genre', 5: 'duration'}
            value_type = types[item.column()]
            if value_type != 'checkbox':
                new_val = self.table_films.item(row, item.column()).text()
                val_id = self.table_films.item(row, 1).text()
                self.db.update_value(value_type, new_val, val_id)
            else:
                val_id = self.table_films.item(row, 1).text()
                if self.table_films.item(row, item.column()).checkState():
                    self.selected_films.append(val_id)
                else:
                    self.selected_films.remove(val_id)

    def add_new_film(self):
        a = AddNewFilm()
        a.show()
        a.exec()
        self.fill_table(self.db.all_films())

    def delete_films(self):
        self.db.delete_films(self.selected_films)
        self.fill_table(self.db.all_films())

# -----------------------------------------


class Db:
    def __init__(self):
        self.__connect = sqlite3.connect('films.db')
        self.__cursor = self.__connect.cursor()

    def all_gen(self):
        id_genre = self.__cursor.execute("""SELECT id, title FROM genres""").fetchall()
        id_genre = {id: title for id, title in id_genre}
        return id_genre

    def all_films(self):
        return self.__cursor.execute("""SELECT * FROM films""").fetchall()

    def get_genre(self, genre_id: int):
        return self.all_gen()[genre_id]

    def get_id_genre(self, genre: str):
        new_dict = {val: key for key, val in self.all_gen().items()}
        return new_dict[genre]

    def get_films(self, options: dict):
        title = options['title'] + '%'
        year = options['year'] if options['year'] != '' else 0
        genre = self.get_id_genre(options['genre']) if options['genre'] != '' else 0
        dur_max = options['dur_max']
        print("а я ставлю на гет фильм перед поиском")
        select_str = """SELECT * FROM films WHERE title like ?"""
        values = [title]
        if year:
            select_str += """ AND year = ?"""
            values.append(year)
        if genre:
            select_str += """ AND genre = ?"""
            values.append(genre)
        if dur_max:
            select_str += """ AND duration BETWEEN ? AND ?"""
            values.append(options['dur_min'])
            values.append(dur_max)
        print("а я - на конец гета")
        return self.__cursor.execute(select_str, tuple(values)).fetchall()

    def update_value(self, old_val: str, new_val: str, film_id: int):
        self.__cursor.execute( """UPDATE films SET ? = ? WHERE id = ?""", tuple(old_val, new_val, film_id))
        self.__connect.commit()

    def add_new_film(self, values: dict):
        values['genre'] = self.get_id_genre(values['genre'])
        values = tuple([self.max_id() + 1] + list(values.values()))
        self.__cursor.execute("""INSERT INTO films VALUES(?, ?, ?, ?, ?)""", values)
        self.__connect.commit()

    def delete_films(self, films_id: list):
        for i in films_id:
            self.__cursor.execute("""DELETE from films WHERE id = ?""", tuple(i))
        self.__connect.commit()

    def min_max_year(self):
        min_year = self.__cursor.execute("""SELECT MIN(year) FROM films""").fetchone()
        max_year = self.__cursor.execute("""SELECT MAX(year) FROM films""").fetchone()
        return [min_year[0], max_year[0]]

    def max_id(self):
        return self.__cursor.execute("""SELECT MAX(id) FROM films""").fetchone()[0]


class AddNewFilm(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = Db()
        self.genre.addItems(list(self.db.all_gen().values()))
        self.pushButton.clicked.connect(self.add_film)

    def add_film(self):
        title = self.title.text()
        year = self.year_spinBox.value()
        duration = self.time_spinBox.value()
        genre = self.genre.currentText()
        values = {'title': title, 'year': year, 'genre': genre, 'duration': duration}
        self.db.add_new_film(values)

# --------------------------------------------------


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Table()
    form.show()
    sys.exit(app.exec())