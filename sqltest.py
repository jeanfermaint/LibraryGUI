import sys

import MySQLdb
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.uic import loadUiType

#print("Connecting to database using MySQLdb")
#db_con = MySQLdb.connect(host='localhost',db='library',user='lcs',password='root')
#print("Successfully Connected to database using MySQLdb!")

ui,_ = loadUiType('testing.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()

    def Handle_UI_Changes(self):
        self.Hide_Themes()
        self.tabWidget.tabBar().setVisible(False)

    def Handle_Buttons(self):

        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_20.clicked.connect(self.Hide_Themes)

        self.pushButton.clicked.connect(self.Open_Day_to_Day_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_Tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)

        self.pushButton_8.clicked.connect(self.Add_New_Book)

        self.pushButton_14.clicked.connect(self.Add_Subject)

    def Show_Themes(self):
        self.groupBox_2.show()

    def Hide_Themes(self):
        self.groupBox_2.hide()


    def Open_Day_to_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    def Add_Subject(self):
        self.db = MySQLdb.connect(host='localhost', db='library', user='lcs', password='root')
        self.cur = self.db.cursor()

        subject_name = self.lineEdit_19.text()

        self.cur.execute('''INSERT INTO subject (subject_name) VALUES ("%s")''', (subject_name,))

        self.db.commit()
        self.statusBar().showMessage('New Subject Added')
        self.db.close()

    def Add_New_Book(self):

        self.db = MySQLdb.connect(host='localhost',db='library',user='lcs',password='root')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()
        book_code = self.lineEdit_4.text()
        book_subject = self.comboBox_5.CurrentText()
        book_author = self.comboBox_6.CurrentText()
        #book_publisher = self.comboBox_?.CurrentText()
        book_price = self.lineEdit_21.text()
        self.db.close()






def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
    #db_con.close()

if __name__ == '__main__':
    main()