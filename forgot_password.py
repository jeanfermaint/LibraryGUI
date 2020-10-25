import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from app_modules import *


reset_pass,_ = loadUiType('forgotpassword.ui')

class PasswordReset(QWidget, reset_pass):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        Themes.darkOrangeTheme(self)


def main():
    app = QApplication(sys.argv)
    window = PasswordReset()
    window.setFixedHeight(580)
    window.setFixedWidth(520)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
