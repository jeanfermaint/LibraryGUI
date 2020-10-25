import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from app_modules import *
from index import *


# Database connection
db_host = "localhost"
db_name = "library"
db_user = "lcs"
db_password = "root"


reset_pass,_ = loadUiType('forgotpassword.ui')

class PasswordReset(QWidget, reset_pass):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        Themes.darkOrangeTheme(self)

        self.pushButton_3.clicked.connect(self.getResetCode)
        self.pushButton_4.clicked.connect(self.insertCode)
        self.pushButton.clicked.connect(self.resetPassword)
        self.pushButton_2.clicked.connect(self.resetPassword)



    def getResetCode(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT reset_code FROM codes''')
        codeFound = self.cur.fetchone()

        print(codeFound[0])
        QMessageBox.information(self, 'Code Found', "Please enter the following code: " + codeFound[0], QMessageBox.Ok)



    def insertCode(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()
        codeInput = self.lineEdit.text()

        self.cur.execute('''SELECT reset_code FROM codes''')
        match = self.cur.fetchone()

        if codeInput == match[0]:
            print(match[0])
            QMessageBox.information(self, 'Done', "Valid Code Entered", QMessageBox.Close)
            self.groupBox.setEnabled(True)
        else:
            print('No Match')
            QMessageBox.warning(self, 'Warning!', "Invalid Code Entered", QMessageBox.Close)


    def resetPassword(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        new_pass = self.lineEdit_2.text()
        confirm_pass = self.lineEdit_3.text()

        if new_pass == confirm_pass:
            self.cur.execute('''UPDATE user_password WHERE user_name = %s''', (MainLogin.username))
            self.db.commit()
            self.window_login = MainLogin()
            self.close()
            self.window_login.show()

        else:
            QMessageBox.warning(self, 'Warning', "Please enter a valid password", QMessageBox.Close)



    def cancelReset(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()
        self.window_login = MainLogin()
        self.close()
        QMessageBox.information(self, 'Cancel', "You have cancelled the password reset", QMessageBox.Close)
        self.window_login.show()


def main():
    app = QApplication(sys.argv)
    window = PasswordReset()
    window.setFixedHeight(580)
    window.setFixedWidth(520)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
