from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb

from PyQt5.uic import loadUiType


ui,_ = loadUiType('testing.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()

        self.Show_Subject()
        self.Show_Author()

        self.Show_Subj_Box()
        self.Show_Author_Box()


    def Handle_UI_Changes(self):
        self.Hide_Themes()
        self.tabWidget.tabBar().setVisible(False)

    def Handle_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_20.clicked.connect(self.Hide_Themes)

        self.pushButton.clicked.connect(self.Open_Day_to_Day_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_21.clicked.connect(self.Open_Borrower_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_Tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)

        self.pushButton_8.clicked.connect(self.Add_New_Book)
        self.pushButton_9.clicked.connect(self.Search_Book)
        self.pushButton_10.clicked.connect(self.Edit_Book)
        self.pushButton_7.clicked.connect(self.Delete_Book)

        self.pushButton_14.clicked.connect(self.Add_Subject)
        self.pushButton_15.clicked.connect(self.Add_Author)

        self.pushButton_11.clicked.connect(self.Add_New_User)
        self.pushButton_13.clicked.connect(self.Login)
        self.pushButton_12.clicked.connect(self.Edit_User)

        self.pushButton_18.clicked.connect(self.Dark_Orange_Theme)
        self.pushButton_17.clicked.connect(self.Dark_Blue_Theme)
        self.pushButton_16.clicked.connect(self.Dark_Gray_Theme)
        self.pushButton_19.clicked.connect(self.QDark_Theme)


    def Show_Themes(self):
        self.groupBox_2.show()

    def Hide_Themes(self):
        self.groupBox_2.hide()

    ################################################
    ################ Opening Tabs ################

    def Open_Day_to_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Borrower_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(4)

    ################################################
     ################## Books #####################

    def Show_All_Books(self):

        self.db = MySQLdb.connect(host='localhost',db='library',user='lcs',password='root')
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT book_code,book_name,book_subject,book_author,book_price
            FROM book''')
        data = self.cur.fetchall()

        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_4.setItem(row,column,QTableWidgetItem(str(item)))
                column += 1

            row_pos = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(row_pos)

        #self.db.close()

    def Add_New_Book(self):

        self.db = MySQLdb.connect(host='localhost',db='library',user='lcs',password='root')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()
        book_code = self.lineEdit_4.text()
        book_subject = self.comboBox_5.CurrentText()
        book_author = self.comboBox_6.CurrentText()
        book_description = self.textEdit.toPlainText()
        #book_publisher = self.comboBox_?.CurrentText()
        book_price = self.lineEdit_21.text()

        self.cur.execute('''
            INSERT INTO book (book_name,book_description,book_code,book_subject,_book_author,book_price)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (book_title,book_description,book_code,book_subject,book_author,book_price))

        self.db.commit()
        self.statusBar().showMessage('New Book Added')

        self.lineEdit_5.setText('') #book title
        self.textEdit.setPlainText('') #book description
        self.lineEdit_4.setText('') #book code
        self.comboBox_5.setCurrentIndex(0) #book subjects
        self.comboBox_6.setCurrentIndex(0) #book authors
        #self.comboBox_?.setCurrentIndex(0) #book publishers
        self.lineEdit_21.setText('')
        self.Show_All_Books()

        #self.db.close()

    def Search_Book(self):
        self.db = MySQLdb.connect(host='localhost', db='library', user='lcs', password='root')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()

        search = '''SELECT * FROM book WHERE book_name = %s'''
        self.cur.execute(search, [(book_title)])

        data = self.cur.fetchone()

        print(data)
        self.lineEdit_6.setText(data[1])
        self.textEdit_2.setPlainText(data[2])
        self.lineEdit_3.setText(data[3])
        self.comboBox_3.setCurrentText(data[4])
        self.comboBox_4.setCurrentText(data[5])
        self.lineEdit_22.setText(str(data[6]))


    def Edit_Book(self):

        self.db = MySQLdb.connect(host='localhost',db='library',user='lcs',password='root')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_6.text()
        book_description = self.textEdit_2.toPlainText()
        book_code = self.lineEdit_3.text()
        book_subject = self.comboBox_3.currentText()
        book_author = self.comboBox_4.currentText()
        book_price = self.lineEdit_22.text()

        search_book_title = self.lineEdit_2.text()
        self.cur.execute('''UPDATE book SET book_name=%s ,book_description=%s ,book_code=%s ,book_subject=%s ,book_author=%s ,book_price=%s
            WHERE book_name = %s''', (book_title,book_description,book_code,book_subject,book_author,book_price,search_book_title))

        self.db.commit()
        self.statusBar().showMessage('Book Updated')
        self.Show_All_Books()

    def Delete_Book(self):
        self.db = MySQLdb.connect(host='localhost', db='library', user='lcs', password='root')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()

        warning = QMessageBox.warning(self,'Delete Book',"Are you sure you want to delete this book?", QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :
            delete = '''DELETE FROM book WHERE book_name = %s '''
            self.cur.execute(delete, [(book_title)])
            self.db.commit()
            self.statusBar().showMessage('Book Deleted')

            self.Show_All_Books()

    ################################################
    ################## Borrowers ###################

    def Show_All_Borrowers(self):
        pass

    def Add_New_Borrower(self):
        pass

    def Search_Borrower(self):
        pass

    def Edit_Borrower(self):
        pass

    def Delete_Borrower(self):
        pass


    ################################################
    ################## Users #####################

    def Add_New_User(self):

        self.db = MySQLdb.connect(host='localhost',db='library',user='lcs',password='root')
        self.cur = self.db.cursor()

        user_name = self.lineEdit_7.text()
        user_password = self.lineEdit_8.text()
        user_retypepwd = self.lineEdit_9.text()
        user_phone = self.lineEdit_10.text()
        user_email = self.lineEdit_15.text()

        # checking for matching passwords
        if user_password == user_retypepwd:
            self.cur.execute('''
            INSERT INTO user (user_name, user_email, user_phone, user_password) 
            VALUES (%s , %s , %s , %s)
            ''', (user_name,user_email,user_phone,user_password))

            self.db.commit()
            self.statusBar().showMessage('New User Added')

        else:
            #self.label_29.setText('Please enter a valid password twice')
            QMessageBox.warning(self,'Invalid Password', "Enter a valid password twice. Please try again.",QMessageBox.Close, QMessageBox.Close)
        #self.db.close()

    def Login(self):
        self.db = MySQLdb.connect(host='localhost', db='library', user='lcs', password='root')
        self.cur = self.db.cursor()

        username = self.lineEdit_17.text()
        password = self.lineEdit_18.text()

        sql = '''SELECT * FROM user'''

        self.cur.execute(sql)
        data = self.cur.fetchall()

        for row in data:
            if username == row[1] and password == row[4]:
                print('User Match')
                self.statusBar().showMessage('Valid Username & Password')
                self.groupBox_5.setEnabled(True)

                self.lineEdit_11.setText(row[1])
                self.lineEdit_14.setText(row[4])
                self.lineEdit_13.setText(row[3])
                self.lineEdit_16.setText(row[2])

            else:
                self.statusBar().showMessage('Enter Valid Username & Password')
                QMessageBox.warning(self,'Invalid User or Password', "Please enter a valid username and password.",QMessageBox.Close,QMessageBox.Close)

    def Edit_User(self):

        username = self.lineEdit_11.text()
        password = self.lineEdit_14.text()
        retypepwd = self.lineEdit_12.text()
        email = self.lineEdit_16.text()
        phone = self.lineEdit_13.text()

        original_name = self.lineEdit_17.text()

        if password == retypepwd:
            self.db = MySQLdb.connect(host='localhost', db='library', user='lcs', password='root')
            self.cur = self.db.cursor()

            print(username)
            print(email)
            print(phone)
            print(password)

            self.cur.execute('''
                UPDATE user SET user_name=%s , user_email=%s , user_phone=%s , user_password=%s
                WHERE user_name=%s
                ''', (username,email,phone,password,original_name))

            self.db.commit()
            QMessageBox.information(self,'Message',"User Data Updated Successfully",QMessageBox.Ok,QMessageBox.Ok)
            self.statusBar().showMessage('User Data Updated Successfully')

        else:
            QMessageBox.warning(self,'Invalid Password', "Enter a valid Password twice. Please try again.",
                                QMessageBox.Close,)
            print('Please enter a valid Password')

    ################################################
    ################## Settings ###################

    def Add_Subject(self):

        self.db = MySQLdb.connect(host='localhost',db='library',user='lcs',password='root')
        self.cur = self.db.cursor()

        subject_name = self.lineEdit_19.text()

        self.cur.execute('''INSERT INTO subject (subject_name) VALUES ("%s")''', (subject_name,))

        self.db.commit()
        self.statusBar().showMessage('New Subject Added')
        self.lineEdit_19.setText('')
        self.Show_Subject()
        #self.db.close()

    def Show_Subject(self):
        self.db = MySQLdb.connect(host='localhost', db='library', user='lcs', password='root')
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT subject_name FROM subject''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(data):
                for column , item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_pos = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_pos)

        #self.db.close()

    def Add_Author(self):

        self.db = MySQLdb.connect(host='localhost', db='library', user='lcs', password='root')
        self.cur = self.db.cursor()

        author_name = self.lineEdit_20.text()

        self.cur.execute('''INSERT INTO author (author_name) VALUES ("%s")''', (author_name,))

        self.db.commit()
        self.statusBar().showMessage('New Author Added')
        self.lineEdit_20.setText('')
        self.Show_Author()
        #self.db.close()


    def Show_Author(self):
        self.db = MySQLdb.connect(host='localhost', db='library', user='lcs', password='root')
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT author_name FROM author''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_pos = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_pos)

        #self.db.close()

    def Add_Publisher(self):
        pass
    def Show_Publisher(self):
        pass

    ################################################
    ########## Show Settings Data in UI ###########

    def Show_Subj_Box(self):
        self.db = MySQLdb.connect(host='localhost', db='library', user='lcs', password='root')
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT subject_name FROM subject''')
        data = self.cur.fetchall()

        for subject in data:
            self.comboBox_5.addItem(subject[0])
            self.comboBox_3.addItem(subject[0])

        #self.db.close()

    def Show_Author_Box(self):
        self.db = MySQLdb.connect(host='localhost',db='library',user='lcs',password='root')
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT author_name FROM author''')
        data = self.cur.fetchall()

        for author in data:
            self.comboBox_6.addItem(author[0])
            self.comboBox_4.addItem(author[0])

        #self.db.close()

    def Show_Publish_Box(self):
        pass



   ########################################
    ###########  UI Themes ###############

    def Dark_Blue_Theme(self):
        style = open('themes/darkblue.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Gray_Theme(self):
        style = open('themes/darkgray.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Orange_Theme(self):
        style = open('themes/darkorange.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def QDark_Theme(self):
        style = open('themes/qdark.css', 'r')
        style = style.read()
        self.setStyleSheet(style)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()