    ################################################
    ###################  Reports ###################
    ################################################

class Reports():

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

