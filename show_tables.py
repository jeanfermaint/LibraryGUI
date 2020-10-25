    ################################################
    ################ Data Transfer##################
    ################################################

class ShowInTables():

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

        self.db.close()



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
        self.db.close()


    def showAllBorrowers(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT borrower_name , borrower_type , borrower_email , borrower_phone FROM borrower
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

        self.db.close()


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

        self.db.close()


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

        self.db.close()


