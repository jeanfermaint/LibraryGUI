import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from app_modules import *
import MySQLdb
import datetime
from xlrd import *
from xlsxwriter import *




ui,_ = loadUiType('testing.ui')
login,_ = loadUiType('login.ui')

# Database connection
db_host = "localhost"
db_name = "library"
db_user = "lcs"
db_password = "root"


class MainLogin(QWidget, login):
    def __init__(self):
        QWidget.__init__(self)

        self.setupUi(self)
        self.pushButton.clicked.connect(self.handleLogin)
        Themes.darkOrangeTheme(self)
        self.pushButton_2.setStyleSheet(u"QPushButton { border: none;\n"
                                        "       background-color: #323232;}\n"
                                        "       QPushButton:hover { color: #ffaa00;}")
        self.pushButton_3.setStyleSheet(u"QPushButton { border: none;\n"
                                        "       background-color: #323232;}\n"
                                        "       QPushButton:hover { color: #ffaa00;}")

    def handleLogin(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        self.cur.execute('''
            SELECT * FROM user WHERE user_name = %s and user_password = %s
            ''', (username, password))
        found = self.cur.fetchone()
        print(found)

        if found:
            print('User Match')
            self.window_2 = MainApp()
            self.close()
            self.window_2.show()

        else:
            self.label.setText('Enter a valid Username & Password')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handleUIChanges()
        self.handleButtons()
        Themes.darkOrangeTheme(self)

        self.showSubject()
        self.showAuthor()

        self.showSubjBox()
        self.showAuthorBox()

        self.showAllBorrowers()
        self.showAllBooks()
        # self.showAllTransactions()

    def handleLogout(self):
        self.mainLoginWindow = MainLogin()
        self.close()
        QMessageBox.information(self,'Logout', "You have been logged out successfully", QMessageBox.Close)
        self.mainLoginWindow.show()

    def handleUIChanges(self):
        self.hideThemes()
        self.tabWidget.tabBar().setVisible(False)

    def handleButtons(self):
        self.pushButton_5.clicked.connect(self.showThemes)
        self.pushButton_20.clicked.connect(self.hideThemes)

        self.pushButton.clicked.connect(self.openDayToDayTab)
        self.pushButton_2.clicked.connect(self.openBookTab)
        self.pushButton_21.clicked.connect(self.openBorrowerTab)
        self.pushButton_3.clicked.connect(self.openUsersTab)
        self.pushButton_4.clicked.connect(self.OpenSettingsTab)

        self.pushButton_8.clicked.connect(self.addNewBook)
        self.pushButton_9.clicked.connect(self.searchBook)
        self.pushButton_10.clicked.connect(self.editBook)
        self.pushButton_7.clicked.connect(self.deleteBook)

        self.pushButton_14.clicked.connect(self.addSubject)
        self.pushButton_15.clicked.connect(self.addAuthor)

        self.pushButton_11.clicked.connect(self.addNewUser)
        self.pushButton_13.clicked.connect(self.enableEditUser)
        self.pushButton_12.clicked.connect(self.editUser)

        self.pushButton_18.clicked.connect(lambda: Themes.darkOrangeTheme(self))
        self.pushButton_17.clicked.connect(lambda: Themes.darkBlueTheme(self))
        self.pushButton_16.clicked.connect(lambda: Themes.darkGrayTheme(self))
        self.pushButton_19.clicked.connect(lambda: Themes.qDarkTheme(self))

        self.pushButton_23.clicked.connect(self.addNewBorrower)
        self.pushButton_26.clicked.connect(self.searchBorrower)
        self.pushButton_25.clicked.connect(self.enableEditBorrower)
        self.pushButton_24.clicked.connect(self.editBorrower)
        self.pushButton_27.clicked.connect(self.deleteBorrower)

        self.pushButton_6.clicked.connect(self.handleDayTransactions)

        self.pushButton_22.clicked.connect(self.dayReport)
        self.pushButton_29.clicked.connect(self.bookReport)
        self.pushButton_30.clicked.connect(self.borrowerReport)

        self.pushButton_28.clicked.connect(self.handleLogout)

    def showThemes(self):
        self.groupBox_2.show()

    def hideThemes(self):
        self.groupBox_2.hide()

    ################################################
    ################ Opening Tabs ##################
    ################################################

    def openDayToDayTab(self):
        self.tabWidget.setCurrentIndex(0)

    def openBookTab(self):
        self.tabWidget.setCurrentIndex(1)

    def openBorrowerTab(self):
        self.tabWidget.setCurrentIndex(2)

    def openUsersTab(self):
        self.tabWidget.setCurrentIndex(3)

    def OpenSettingsTab(self):
        self.tabWidget.setCurrentIndex(4)

    ################################################
    ############### Day Operations #################
    ################################################

    def handleDayTransactions(self):
        book_title = self.lineEdit.text()
        borrower_name = self.lineEdit23.text()
        trans_type = self.comboBox.currentText()
        days_number = self.comboBox_2.currentText()
        today_date = datetime.date.today()
        to_date = today_date + datetime.timedelta(days=days_number)

        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        self.cur.execute('''
        INSERT INTO day_transactions(book_name, borrower, type, date, to_date) 
        VALUES (%s , %s , %s , %s , %s , %s)
        ''', (book_title,borrower_name,trans_type,days_number,to_date))

        self.db.commit()
        QMessageBox.information(self,'Done', "New Transaction Completed", QMessageBox.Close)

        self.showAllTransactions()
        # self.db.close()

    def showAllTransactions(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT book_name, borrower, type, date, to_date FROM day_transactions''')

        data = self.cur.fetchall()

        print(data)
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_pos = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_pos)

        # self.db.close()

    ################################################
    ################### Books ######################
    ################################################

    def showAllBooks(self):

        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT book_code,book_name,book_subject,book_author,book_price
            FROM book''')
        data = self.cur.fetchall()

        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_pos = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(row_pos)
        # self.db.close()

    def addNewBook(self):

        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()
        book_code = self.lineEdit_4.text()
        book_subject = self.lineEdit_24.text()
        book_author = self.lineEdit_25.text()
        book_description = self.textEdit.toPlainText()
        book_price = self.lineEdit_21.text()


        self.cur.execute('''
            INSERT INTO book (book_name,book_description,book_code,book_subject,book_author,book_price)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (book_title, book_description, book_code, book_subject, book_author, book_price))

        self.db.commit()
        QMessageBox.information(self,'Done',"New Book Added",QMessageBox.Close)
        self.statusBar().showMessage('New Book Added')

        self.lineEdit_5.setText('')         # book title
        self.textEdit.setPlainText('')      # book description
        self.lineEdit_4.setText('')         # book code
        self.lineEdit_24.setText('')        # book subjects
        self.lineEdit_25.setText('')        # book authors
        self.lineEdit_21.setText('')        # book price
        self.showAllBooks()

        # self.db.close()

    def searchBook(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
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
        # self.db.close()

    def editBook(self):

        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        book_title = self.lineEdit_6.text()
        book_description = self.textEdit_2.toPlainText()
        book_code = self.lineEdit_3.text()
        book_subject = self.comboBox_3.currentText()
        book_author = self.comboBox_4.currentText()
        book_price = self.lineEdit_22.text()

        search_book_title = self.lineEdit_2.text()
        self.cur.execute('''UPDATE book SET book_name=%s ,book_description=%s ,book_code=%s ,
            book_subject=%s ,book_author=%s ,book_price=%s WHERE book_name = %s
            ''', (book_title, book_description, book_code, book_subject, book_author, book_price, search_book_title))

        self.db.commit()
        QMessageBox.information(self,'Done',"Book Updated", QMessageBox.Close)
        self.statusBar().showMessage('Book Updated')
        self.showAllBooks()
        # self.db.close()

    def deleteBook(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()

        warning = QMessageBox.warning(self, 'Delete Book', "Are you sure you want to delete this book?",
                                      QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            delete = '''DELETE FROM book WHERE book_name = %s '''
            self.cur.execute(delete, [(book_title)])
            self.db.commit()
            QMessageBox.information(self,'Done', "Book Deleted", QMessageBox.Close)
            self.statusBar().showMessage('Book Deleted')

            self.showAllBooks()

        # self.db.close()

    ################################################
    ################## Borrowers ###################
    ################################################

    def showAllBorrowers(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT borrower_name , borrower_ID , borrower_type , borrower_email , borrower_phone FROM borrower
        ''')
        data = self.cur.fetchall()

        print(data)
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_pos = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_pos)

        # self.db.close()

    def addNewBorrower(self):
        borrower_name = self.lineEdit_28.text()
        borrower_email = self.lineEdit_29.text()
        borrower_phone = self.lineEdit_30.text()
        borrower_type = self.comboBox_7.currentText()
        borrower_ID = self.lineEdit_33.text()

        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        self.cur.execute('''
                   INSERT INTO borrower(borrower_name , borrower_email , borrower_phone , borrower_type , borrower_ID)
                   VALUES (%s , %s , %s , %s , %s)
               ''', (borrower_name, borrower_email, borrower_phone, borrower_type, borrower_ID))
        self.db.commit()
        # self.db.close()
        QMessageBox.information(self,'Done',"New Borrower Added", QMessageBox.Close)
        self.statusBar().showMessage('New Borrower Added')
        self.showAllBorrowers()

    def searchBorrower(self):
        borrower_ID = self.lineEdit_41.text()

        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        sql = ''' SELECT * FROM borrower WHERE borrower_ID = %s '''
        self.cur.execute(sql, [(borrower_ID)])
        data = self.cur.fetchone()
        print(data)

        self.lineEdit_37.setText(data[0])
        self.lineEdit_34.setText(data[1])
        self.lineEdit_36.setText(data[2])
        self.lineEdit_35.setText(data[3])

        # self.db.close()

    def enableEditBorrower(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        username = self.lineEdit_39.text()
        password = self.lineEdit_40.text()

        self.cur.execute('''
                    SELECT * FROM user WHERE user_name=%s and user_password=%s
                    ''', (username, password))
        found = self.cur.fetchone()
        print(found)

        if found:
            print('User Match')
            QMessageBox.information(self,'Done', "Edit Enabled", QMessageBox.Close)
            self.statusBar().showMessage('Valid Username & Password')
            self.groupBox_9.setEnabled(True)

        else:
            self.statusBar().showMessage('Enter Valid Username & Password')
            QMessageBox.warning(self, 'Invalid User or Password', "Please enter a valid Username & Password.",
                                QMessageBox.Close, QMessageBox.Close)

        # borrower_ID = self.lineEdit_45.text()


        # self.db.close()

    def editBorrower(self):
        original_borrower_ID = self.lineEdit_45.text()
        borrower_name = self.lineEdit_44.text()
        borrower_email = self.lineEdit_38.text()
        borrower_phone = self.lineEdit_43.text()
        borrower_ID = self.lineEdit_42.text()

        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        sql = ''' SELECT * FROM borrower WHERE borrower_ID = %s '''
        self.cur.execute(sql, [(original_borrower_ID)])
        data = self.cur.fetchone()
        print(data)

        self.lineEdit_44.setText(data[1])
        self.lineEdit_38.setText(data[2])
        self.lineEdit_43.setText(data[3])
        self.lineEdit_42.setText(data[4])

        self.cur.execute('''
            UPDATE borrower SET borrower_name = %s , borrower_email = %s , borrower_phone = %s , borrower_ID = %s
            WHERE borrower_ID = %s''',
                         (borrower_name, borrower_email, borrower_phone, borrower_ID, original_borrower_ID))
        self.db.commit()
        # self.db.close()
        QMessageBox.information(self,'Done',"Borrower Updated", QMessageBox.Close)
        self.statusBar().showMessage('Borrower Data Updated')
        self.showAllBorrowers()

    def deleteBorrower(self):
        borrower_ID = self.lineEdit_41.text()

        warning = QMessageBox.warning(self, 'Delete Borrower', "Delete Borrower?", QMessageBox.Yes | QMessageBox.No)

        if warning == QMessageBox.Yes:
            self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
            self.cur = self.db.cursor()

            sql = ''' DELETE FROM borrower WHERE borrower_ID = %s '''
            self.cur.execute(sql, [(borrower_ID)])

            self.db.commit()
            # self.db.close()
            QMessageBox.information(self, 'Done', "Borrower Deleted", QMessageBox.Close)
            self.statusBar().showMessage('Borrower Deleted')
            self.showAllBorrowers()

        # self.db.close()
    ################################################
    #################### Users #####################
    ################################################

    def addNewUser(self):

        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        user_name = self.lineEdit_7.text()
        user_password = self.lineEdit_8.text()
        user_retype = self.lineEdit_9.text()
        user_phone = self.lineEdit_10.text()
        user_email = self.lineEdit_15.text()

        # checking for matching passwords
        if user_password == user_retype:
            self.cur.execute('''
                INSERT INTO user (user_name, user_email, user_phone, user_password) 
                VALUES (%s , %s , %s , %s)
            ''', (user_name, user_email, user_phone, user_password))

            self.db.commit()
            self.statusBar().showMessage('New User Added')

        else:
            self.label_29.setText('Please enter a valid password twice')
            QMessageBox.warning(self, 'Invalid Password', "Enter a valid password twice. Please try again.",
                                QMessageBox.Close, QMessageBox.Close)

        # self.db.close()

    def enableEditUser(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        username = self.lineEdit_17.text()
        password = self.lineEdit_18.text()

        self.cur.execute('''
            SELECT * FROM user WHERE user_name=%s and user_password=%s
            ''', (username, password))
        found = self.cur.fetchone()
        print(found)

        if found:
            print('User Match')
            self.statusBar().showMessage('Valid Username & Password')
            self.groupBox_5.setEnabled(True)

            self.lineEdit_11.setText(found[1])
            self.lineEdit_14.setText(found[4])
            self.lineEdit_13.setText(found[3])
            self.lineEdit_16.setText(found[2])

        else:
            self.statusBar().showMessage('Enter Valid Username & Password')
            QMessageBox.warning(self, 'Invalid User or Password', "Please enter a valid Username & Password.",
                                QMessageBox.Close, QMessageBox.Close)

        # self.db.close()

    def editUser(self):

        username = self.lineEdit_11.text()
        password = self.lineEdit_14.text()
        retype = self.lineEdit_12.text()
        email = self.lineEdit_16.text()
        phone = self.lineEdit_13.text()

        original_name = self.lineEdit_17.text()

        if password == retype:
            self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
            self.cur = self.db.cursor()

            print(username)
            print(email)
            print(phone)
            print(password)

            self.cur.execute('''
                UPDATE user SET user_name=%s , user_email=%s , user_phone=%s , user_password=%s
                WHERE user_name=%s
            ''', (username, email, phone, password, original_name))

            self.db.commit()
            QMessageBox.information(self, 'Done', "User Data Updated Successfully", QMessageBox.Ok)
            self.statusBar().showMessage('User Data Updated Successfully')

        else:
            QMessageBox.warning(self, 'Invalid Password', "Enter a valid Password twice. Please try again.",
                                QMessageBox.Close)
            print('Please enter a valid Password')

        # self.db.close()

    ################################################
    #################### Admin #####################
    ################################################

    def addSubject(self):

        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        subject_name = self.lineEdit_19.text()

        self.cur.execute('''INSERT INTO subject (subject_name) VALUES ("%s")''', (subject_name,))

        self.db.commit()
        QMessageBox.information(self,'Done', "New Subject Added", QMessageBox.Ok)
        self.statusBar().showMessage('New Subject Added')
        self.lineEdit_19.setText('')
        self.showSubject()
        # self.db.close()

    def showSubject(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT subject_name FROM subject''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_pos = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_pos)

        # self.db.close()

    def addAuthor(self):

        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        author_name = self.lineEdit_20.text()

        self.cur.execute('''INSERT INTO author (author_name) VALUES ("%s")''', (author_name,))

        self.db.commit()
        QMessageBox.information(self,'Done',"New Author Added", QMessageBox.Ok)
        self.statusBar().showMessage('New Author Added')
        self.lineEdit_20.setText('')
        self.showAuthor()
        # self.db.close()

    def showAuthor(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
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

        # self.db.close()

    ################################################
    ########## Show Settings Data in UI ############
    ################################################

    def showSubjBox(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT subject_name FROM subject''')
        data = self.cur.fetchall()

        for subject in data:
            #self.comboBox_5.addItem(subject[0])
            self.comboBox_3.addItem(subject[0])

        # self.db.close()

    def showAuthorBox(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT author_name FROM author''')
        data = self.cur.fetchall()

        for author in data:
            #self.comboBox_6.addItem(author[0])
            self.comboBox_4.addItem(author[0])

        # self.db.close()

    ################################################
    ###################  Reports ###################
    ################################################

    def dayReport(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        self.cur.execute('''
        SELECT book_name,borrower,type,date,to_date FROM day_transactions
        ''')

        data = self.cur.fetchall()

        wb = Workbook('day_transactions.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0,0,'book title')
        sheet1.write(0,1,'borrower name')
        sheet1.write(0,2,'type')
        sheet1.write(0,3,'from date')
        sheet1.write(0,4,'to date')

        row_num = 1
        for row in data:
            column_num = 0
            for item in row:
                sheet1.write(row_num,column_num,str(item))
                column_num += 1
            row_num += 1

        wb.close()
        self.statusBar().showMessage('Report Created Successfully')
        QMessageBox.information(self,'Done',"Report Created Successfully", QMessageBox.Ok)

    def bookReport(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        self.cur.execute('''
        SELECT book_name,book_code,book_subject,book_author,book_price,book_status
         FROM book''')

        data = self.cur.fetchall()

        wb = Workbook('book_report.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0, 0, 'book code')
        sheet1.write(0, 1, 'book title')
        sheet1.write(0, 2, 'book subject')
        sheet1.write(0, 3, 'book author')
        sheet1.write(0, 4, 'book price')
        sheet1.write(0, 5, 'book status')

        row_num = 1
        for row in data:
            column_num = 0
            for item in row:
                sheet1.write(row_num, column_num, str(item))
                column_num += 1
            row_num += 1

        wb.close()
        self.statusBar().showMessage('Report Created Successfully')
        QMessageBox.information(self, 'Done', "Book Report Created Successfully", QMessageBox.Ok)

    def borrowerReport(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        self.cur.execute('''
        SELECT borrower_name,borrower_email,borrower_phone FROM borrower
        ''')

        data = self.cur.fetchall()

        wb = Workbook('borrower_report.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0, 0, 'borrower name')
        sheet1.write(0, 1, 'borrower email')
        sheet1.write(0, 2, 'borrower phone')


        row_num = 1
        for row in data:
            column_num = 0
            for item in row:
                sheet1.write(row_num, column_num, str(item))
                column_num += 1
            row_num += 1

        wb.close()
        self.statusBar().showMessage('Report Created Successfully')
        QMessageBox.information(self, 'Done', "Borrower Report Created Successfully", QMessageBox.Ok)


def main():
    app = QApplication(sys.argv)
    # window = MainApp()
    window = MainLogin()
    window.setFixedHeight(480)
    window.setFixedWidth(480)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
