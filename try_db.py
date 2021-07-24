# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'try_db.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setEnabled(True)
        self.horizontalWidget.setGeometry(QtCore.QRect(0, 30, 600, 31))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(11, 4, 11, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.genre = QtWidgets.QComboBox(self.horizontalWidget)
        self.genre.setObjectName("genre")
        self.horizontalLayout.addWidget(self.genre)
        self.year = QtWidgets.QComboBox(self.horizontalWidget)
        self.year.setObjectName("year")
        self.horizontalLayout.addWidget(self.year)
        self.duration = QtWidgets.QComboBox(self.horizontalWidget)
        self.duration.setObjectName("duration")
        self.horizontalLayout.addWidget(self.duration)
        self.name = QtWidgets.QTextEdit(self.horizontalWidget)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.btn_search = QtWidgets.QPushButton(self.horizontalWidget)
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout.addWidget(self.btn_search)
        self.horizontalWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget1.setGeometry(QtCore.QRect(0, 387, 491, 40))
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(11, 6, 0, 2)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_save = QtWidgets.QPushButton(self.horizontalWidget1)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_2.addWidget(self.btn_save)
        self.btn_add = QtWidgets.QPushButton(self.horizontalWidget1)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout_2.addWidget(self.btn_add)
        self.btn_delete = QtWidgets.QPushButton(self.horizontalWidget1)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout_2.addWidget(self.btn_delete)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 10, 73, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(91, 10, 73, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(165, 10, 83, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(251, 10, 238, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.table_films = QtWidgets.QTableWidget(self.centralwidget)
        self.table_films.setGeometry(QtCore.QRect(10, 64, 580, 325))
        self.table_films.setObjectName("table_films")
        self.table_films.setColumnCount(0)
        self.table_films.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_search.setText(_translate("MainWindow", "Поиск"))
        self.btn_save.setText(_translate("MainWindow", "Сохранить изменения"))
        self.btn_add.setText(_translate("MainWindow", "Добавить"))
        self.btn_delete.setText(_translate("MainWindow", "Удалить"))
        self.label.setText(_translate("MainWindow", "Жанры"))
        self.label_2.setText(_translate("MainWindow", "Год "))
        self.label_3.setText(_translate("MainWindow", "Длительность"))
        self.label_4.setText(_translate("MainWindow", "Название"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
