import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE home
        self.ui.btn_home.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_home))
        # PAGE search
        self.ui.btn_search.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_search))
        # PAGE librarian
        self.ui.btn_librarian.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_Librarian_Login))
        # PAGE login
        self.ui.btn_login.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_login))
        # PAGE signup
        self.ui.btn_signup.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_signup))
        self.ui.btn_signup_2.clicked.connect(lambda: self.show_signup())
        self.ui.btn_signup_2.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_login))


        # PAGE user
        self.ui.btn_login_2.clicked.connect(lambda: self.show_popup())
        self.ui.btn_login_2.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_user))
        self.ui.btn_request.clicked.connect(lambda: self.show_bookNotFound())
        self.ui.btn_remove.clicked.connect(lambda: self.show_bookNotFound())

        # PAGE reset Password
        self.ui.btn_password.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_passwordreset))
        # PAGE login
        self.ui.btn_reset.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_login))


        # PAGE Librarian
        self.ui.btn_Librarian_login.clicked.connect(lambda: self.show_popup())
        self.ui.btn_Librarian_login.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_Librarian))
        self.ui.btn_Request.clicked.connect(lambda: self.show_bookNotFound())
        self.ui.btn_Remove.clicked.connect(lambda: self.show_bookNotFound())
        self.ui.btn_Checkout.clicked.connect(lambda: self.show_checkSuccess())
        self.ui.btn_Checkin.clicked.connect(lambda: self.show_checkSuccess())
        self.ui.btn_Scan.clicked.connect(lambda: self.show_scanUser())
        # PAGE reset Password
        self.ui.btn_Librarian_password.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_Librarian_Reset))
        # PAGE login
        self.ui.btn_Librarian_reset.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_Librarian_Login))
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("login Success!")
        msg.setText("login successful!")
        x = msg.exec_()
    def show_signup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Email already exists!")
        x = msg.exec_()
    def show_bookNotFound(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Book not found!")
        x = msg.exec_()
    def show_checkSuccess(self):
        msg = QMessageBox()
        msg.setWindowTitle("Process Success!")
        msg.setText("Transactions completed!")
        x = msg.exec_()
    def show_scanUser(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Borrower Not found!")
        x = msg.exec_()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())