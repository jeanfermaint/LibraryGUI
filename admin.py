    ################################################
    #################### Admin #####################
    ################################################

class Admin():

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

        self.db.close()

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

        self.db.close()



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
        self.db.close()


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
        self.db.close()

