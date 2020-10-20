# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 639)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_Toggle = QFrame(self.Top_Bar)
        self.frame_Toggle.setObjectName(u"frame_Toggle")
        self.frame_Toggle.setMaximumSize(QSize(70, 40))
        self.frame_Toggle.setStyleSheet(u"")
        self.frame_Toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_Toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_Toggle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_Toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy1)
        self.Btn_Toggle.setMinimumSize(QSize(70, 40))
        self.Btn_Toggle.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Toggle.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_Toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(1000, 500))
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.frame_top_menus)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 40))
        self.btn_home.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_search = QPushButton(self.frame_top_menus)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(0, 40))
        self.btn_search.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/cil-find-in-page.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.btn_search)

        self.btn_librarian = QPushButton(self.frame_top_menus)
        self.btn_librarian.setObjectName(u"btn_librarian")
        self.btn_librarian.setMinimumSize(QSize(0, 40))
        self.btn_librarian.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/cil-paperclip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_librarian.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.btn_librarian)


        self.verticalLayout_2.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, -1, 0)
        self.Pages_Widget = QStackedWidget(self.frame_pages)
        self.Pages_Widget.setObjectName(u"Pages_Widget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setMinimumSize(QSize(1000, 500))
        self.label_3 = QLabel(self.page_home)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 521, 61))
        font = QFont()
        font.setFamily(u"Cambria")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_login = QPushButton(self.page_home)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(50, 130, 100, 75))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy2)
        self.btn_login.setMinimumSize(QSize(100, 75))
        self.btn_login.setMaximumSize(QSize(100, 75))
        font1 = QFont()
        font1.setFamily(u"Cambria")
        font1.setPointSize(18)
        self.btn_login.setFont(font1)
        self.btn_login.setLayoutDirection(Qt.LeftToRight)
        self.btn_login.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_login.setIcon(icon4)
        self.btn_signup = QPushButton(self.page_home)
        self.btn_signup.setObjectName(u"btn_signup")
        self.btn_signup.setGeometry(QRect(220, 130, 100, 75))
        sizePolicy2.setHeightForWidth(self.btn_signup.sizePolicy().hasHeightForWidth())
        self.btn_signup.setSizePolicy(sizePolicy2)
        self.btn_signup.setMinimumSize(QSize(100, 75))
        self.btn_signup.setMaximumSize(QSize(100, 75))
        self.btn_signup.setFont(font1)
        self.btn_signup.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/cil-user-follow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_signup.setIcon(icon5)
        self.Pages_Widget.addWidget(self.page_home)
        self.page_search = QWidget()
        self.page_search.setObjectName(u"page_search")
        self.label_2 = QLabel(self.page_search)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 251, 61))
        font2 = QFont()
        font2.setFamily(u"Cambria")
        font2.setPointSize(28)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: #FFF")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.page_search)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 120, 241, 101))
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 20, 70, 18))
        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(20, 40, 70, 18))
        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(20, 60, 70, 18))
        self.groupBox_2 = QGroupBox(self.page_search)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 240, 311, 261))
        self.groupBox_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QRect(10, 50, 281, 21))
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);")
        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QRect(10, 110, 281, 21))
        self.lineEdit_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);")
        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QRect(10, 180, 281, 21))
        self.lineEdit_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 30, 47, 14))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 160, 47, 14))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 90, 47, 14))
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 220, 75, 23))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.tableWidget = QTableWidget(self.page_search)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(330, 110, 301, 401))
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setRowCount(0)
        self.Pages_Widget.addWidget(self.page_search)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.label_13 = QLabel(self.page_login)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 10, 401, 101))
        font3 = QFont()
        font3.setFamily(u"Cambria")
        font3.setPointSize(24)
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.groupBox_4 = QGroupBox(self.page_login)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 140, 601, 421))
        self.groupBox_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.password_2 = QLineEdit(self.groupBox_4)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setGeometry(QRect(10, 150, 113, 20))
        self.password_2.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.email_2 = QLineEdit(self.groupBox_4)
        self.email_2.setObjectName(u"email_2")
        self.email_2.setGeometry(QRect(10, 70, 113, 20))
        self.email_2.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 50, 61, 16))
        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 130, 61, 16))
        self.btn_login_2 = QPushButton(self.groupBox_4)
        self.btn_login_2.setObjectName(u"btn_login_2")
        self.btn_login_2.setGeometry(QRect(10, 230, 112, 75))
        sizePolicy.setHeightForWidth(self.btn_login_2.sizePolicy().hasHeightForWidth())
        self.btn_login_2.setSizePolicy(sizePolicy)
        self.btn_login_2.setMinimumSize(QSize(100, 75))
        self.btn_login_2.setMaximumSize(QSize(112, 75))
        self.btn_login_2.setFont(font1)
        self.btn_login_2.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.btn_login_2.setIcon(icon4)
        self.btn_password = QPushButton(self.groupBox_4)
        self.btn_password.setObjectName(u"btn_password")
        self.btn_password.setGeometry(QRect(10, 180, 81, 20))
        self.btn_password.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.lbl_InPassword = QLabel(self.groupBox_4)
        self.lbl_InPassword.setObjectName(u"lbl_InPassword")
        self.lbl_InPassword.setEnabled(True)
        self.lbl_InPassword.setGeometry(QRect(10, 170, 201, 16))
        self.lbl_InEmail = QLabel(self.groupBox_4)
        self.lbl_InEmail.setObjectName(u"lbl_InEmail")
        self.lbl_InEmail.setEnabled(True)
        self.lbl_InEmail.setGeometry(QRect(10, 90, 151, 16))
        self.Pages_Widget.addWidget(self.page_login)
        self.page_passwordreset = QWidget()
        self.page_passwordreset.setObjectName(u"page_passwordreset")
        self.label_14 = QLabel(self.page_passwordreset)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 10, 551, 101))
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.groupBox_5 = QGroupBox(self.page_passwordreset)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 130, 601, 421))
        self.groupBox_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.first_2 = QLineEdit(self.groupBox_5)
        self.first_2.setObjectName(u"first_2")
        self.first_2.setGeometry(QRect(10, 60, 113, 20))
        self.first_2.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.new_password = QLineEdit(self.groupBox_5)
        self.new_password.setObjectName(u"new_password")
        self.new_password.setGeometry(QRect(10, 300, 113, 20))
        self.new_password.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.email_3 = QLineEdit(self.groupBox_5)
        self.email_3.setObjectName(u"email_3")
        self.email_3.setGeometry(QRect(10, 180, 113, 20))
        self.email_3.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.dateEdit_2 = QDateEdit(self.groupBox_5)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(10, 240, 110, 22))
        self.dateEdit_2.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"border: none;")
        self.dateEdit_2.setFrame(False)
        self.dateEdit_2.setAccelerated(False)
        self.dateEdit_2.setCalendarPopup(True)
        self.last_2 = QLineEdit(self.groupBox_5)
        self.last_2.setObjectName(u"last_2")
        self.last_2.setGeometry(QRect(10, 120, 113, 20))
        self.last_2.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 40, 61, 16))
        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 220, 61, 16))
        self.label_19 = QLabel(self.groupBox_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 160, 61, 16))
        self.label_20 = QLabel(self.groupBox_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 100, 61, 16))
        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 280, 101, 16))
        self.btn_reset = QPushButton(self.groupBox_5)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setGeometry(QRect(10, 330, 112, 75))
        sizePolicy.setHeightForWidth(self.btn_reset.sizePolicy().hasHeightForWidth())
        self.btn_reset.setSizePolicy(sizePolicy)
        self.btn_reset.setMinimumSize(QSize(100, 75))
        self.btn_reset.setMaximumSize(QSize(112, 75))
        self.btn_reset.setFont(font1)
        self.btn_reset.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/cil-hand-point-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reset.setIcon(icon6)
        self.Pages_Widget.addWidget(self.page_passwordreset)
        self.page_Librarian_Reset = QWidget()
        self.page_Librarian_Reset.setObjectName(u"page_Librarian_Reset")
        self.groupBox_11 = QGroupBox(self.page_Librarian_Reset)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(10, 130, 601, 421))
        self.groupBox_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.first_4 = QLineEdit(self.groupBox_11)
        self.first_4.setObjectName(u"first_4")
        self.first_4.setGeometry(QRect(10, 60, 113, 20))
        self.first_4.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.new_password_2 = QLineEdit(self.groupBox_11)
        self.new_password_2.setObjectName(u"new_password_2")
        self.new_password_2.setGeometry(QRect(10, 300, 113, 20))
        self.new_password_2.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.email_5 = QLineEdit(self.groupBox_11)
        self.email_5.setObjectName(u"email_5")
        self.email_5.setGeometry(QRect(10, 180, 113, 20))
        self.email_5.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.dateEdit_3 = QDateEdit(self.groupBox_11)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setGeometry(QRect(10, 240, 110, 22))
        self.dateEdit_3.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"border: none;")
        self.dateEdit_3.setFrame(False)
        self.dateEdit_3.setAccelerated(False)
        self.dateEdit_3.setCalendarPopup(True)
        self.last_3 = QLineEdit(self.groupBox_11)
        self.last_3.setObjectName(u"last_3")
        self.last_3.setGeometry(QRect(10, 120, 113, 20))
        self.last_3.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.label_34 = QLabel(self.groupBox_11)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(10, 40, 61, 16))
        self.label_35 = QLabel(self.groupBox_11)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 220, 61, 16))
        self.label_36 = QLabel(self.groupBox_11)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(10, 160, 61, 16))
        self.label_37 = QLabel(self.groupBox_11)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 100, 61, 16))
        self.label_38 = QLabel(self.groupBox_11)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, 280, 101, 16))
        self.btn_Librarian_reset = QPushButton(self.groupBox_11)
        self.btn_Librarian_reset.setObjectName(u"btn_Librarian_reset")
        self.btn_Librarian_reset.setGeometry(QRect(10, 330, 112, 75))
        sizePolicy.setHeightForWidth(self.btn_Librarian_reset.sizePolicy().hasHeightForWidth())
        self.btn_Librarian_reset.setSizePolicy(sizePolicy)
        self.btn_Librarian_reset.setMinimumSize(QSize(100, 75))
        self.btn_Librarian_reset.setMaximumSize(QSize(112, 75))
        self.btn_Librarian_reset.setFont(font1)
        self.btn_Librarian_reset.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.btn_Librarian_reset.setIcon(icon6)
        self.label_39 = QLabel(self.page_Librarian_Reset)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(20, 10, 551, 101))
        self.label_39.setFont(font3)
        self.label_39.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Pages_Widget.addWidget(self.page_Librarian_Reset)
        self.page_user = QWidget()
        self.page_user.setObjectName(u"page_user")
        self.groupBox_6 = QGroupBox(self.page_user)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 90, 341, 171))
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.groupBox_6.setFont(font4)
        self.groupBox_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.label_23 = QLabel(self.groupBox_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 40, 61, 16))
        self.lbl_first = QLabel(self.groupBox_6)
        self.lbl_first.setObjectName(u"lbl_first")
        self.lbl_first.setGeometry(QRect(80, 40, 47, 14))
        self.label_25 = QLabel(self.groupBox_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 70, 61, 16))
        self.lbl_last = QLabel(self.groupBox_6)
        self.lbl_last.setObjectName(u"lbl_last")
        self.lbl_last.setGeometry(QRect(80, 70, 47, 14))
        self.lbl_email = QLabel(self.groupBox_6)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(80, 100, 47, 14))
        self.label_28 = QLabel(self.groupBox_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 100, 47, 14))
        self.label_29 = QLabel(self.groupBox_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 130, 47, 14))
        self.lbl_dob = QLabel(self.groupBox_6)
        self.lbl_dob.setObjectName(u"lbl_dob")
        self.lbl_dob.setGeometry(QRect(80, 130, 47, 14))
        self.lbl_fines = QLabel(self.groupBox_6)
        self.lbl_fines.setObjectName(u"lbl_fines")
        self.lbl_fines.setGeometry(QRect(80, 160, 47, 14))
        self.label_30 = QLabel(self.groupBox_6)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 160, 47, 14))
        self.label_22 = QLabel(self.page_user)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 10, 521, 61))
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.groupBox_7 = QGroupBox(self.page_user)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(10, 290, 341, 281))
        self.groupBox_7.setFont(font4)
        self.groupBox_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.label_24 = QLabel(self.groupBox_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 40, 201, 16))
        self.tableWidget_2 = QTableWidget(self.groupBox_7)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(10, 80, 301, 201))
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"color: rgb(0, 0, 0);")
        self.tableWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setRowCount(0)
        self.groupBox_8 = QGroupBox(self.page_user)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(370, 290, 341, 281))
        self.groupBox_8.setFont(font4)
        self.groupBox_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.label_26 = QLabel(self.groupBox_8)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 40, 201, 16))
        self.tableWidget_3 = QTableWidget(self.groupBox_8)
        if (self.tableWidget_3.columnCount() < 3):
            self.tableWidget_3.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(10, 80, 301, 201))
        self.tableWidget_3.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"color: rgb(0, 0, 0);")
        self.tableWidget_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_3.setShowGrid(False)
        self.tableWidget_3.setRowCount(0)
        self.groupBox_9 = QGroupBox(self.page_user)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(380, 90, 341, 171))
        self.groupBox_9.setFont(font4)
        self.groupBox_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.label_27 = QLabel(self.groupBox_9)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 30, 281, 16))
        self.first_3 = QLineEdit(self.groupBox_9)
        self.first_3.setObjectName(u"first_3")
        self.first_3.setEnabled(True)
        self.first_3.setGeometry(QRect(10, 60, 113, 20))
        self.first_3.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.btn_request = QPushButton(self.groupBox_9)
        self.btn_request.setObjectName(u"btn_request")
        self.btn_request.setGeometry(QRect(10, 100, 75, 23))
        self.btn_request.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.first_11 = QLineEdit(self.groupBox_9)
        self.first_11.setObjectName(u"first_11")
        self.first_11.setEnabled(True)
        self.first_11.setGeometry(QRect(150, 60, 113, 20))
        self.first_11.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.btn_remove = QPushButton(self.groupBox_9)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setGeometry(QRect(150, 100, 75, 23))
        self.btn_remove.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.Pages_Widget.addWidget(self.page_user)
        self.page_Librarian_Login = QWidget()
        self.page_Librarian_Login.setObjectName(u"page_Librarian_Login")
        self.groupBox_10 = QGroupBox(self.page_Librarian_Login)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(10, 140, 601, 421))
        self.groupBox_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.password_3 = QLineEdit(self.groupBox_10)
        self.password_3.setObjectName(u"password_3")
        self.password_3.setGeometry(QRect(10, 150, 113, 20))
        self.password_3.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.email_4 = QLineEdit(self.groupBox_10)
        self.email_4.setObjectName(u"email_4")
        self.email_4.setGeometry(QRect(10, 70, 113, 20))
        self.email_4.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.label_31 = QLabel(self.groupBox_10)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 50, 61, 16))
        self.label_32 = QLabel(self.groupBox_10)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 130, 61, 16))
        self.btn_Librarian_login = QPushButton(self.groupBox_10)
        self.btn_Librarian_login.setObjectName(u"btn_Librarian_login")
        self.btn_Librarian_login.setGeometry(QRect(10, 230, 112, 75))
        sizePolicy.setHeightForWidth(self.btn_Librarian_login.sizePolicy().hasHeightForWidth())
        self.btn_Librarian_login.setSizePolicy(sizePolicy)
        self.btn_Librarian_login.setMinimumSize(QSize(100, 75))
        self.btn_Librarian_login.setMaximumSize(QSize(112, 75))
        self.btn_Librarian_login.setFont(font1)
        self.btn_Librarian_login.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.btn_Librarian_login.setIcon(icon4)
        self.btn_Librarian_password = QPushButton(self.groupBox_10)
        self.btn_Librarian_password.setObjectName(u"btn_Librarian_password")
        self.btn_Librarian_password.setGeometry(QRect(10, 180, 81, 20))
        self.btn_Librarian_password.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.lbl_InPassword_2 = QLabel(self.groupBox_10)
        self.lbl_InPassword_2.setObjectName(u"lbl_InPassword_2")
        self.lbl_InPassword_2.setEnabled(True)
        self.lbl_InPassword_2.setGeometry(QRect(10, 170, 201, 16))
        self.lbl_InEmail_2 = QLabel(self.groupBox_10)
        self.lbl_InEmail_2.setObjectName(u"lbl_InEmail_2")
        self.lbl_InEmail_2.setEnabled(True)
        self.lbl_InEmail_2.setGeometry(QRect(10, 90, 151, 16))
        self.label_33 = QLabel(self.page_Librarian_Login)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(20, 10, 581, 101))
        self.label_33.setFont(font3)
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Pages_Widget.addWidget(self.page_Librarian_Login)
        self.page_Librarian = QWidget()
        self.page_Librarian.setObjectName(u"page_Librarian")
        self.groupBox_12 = QGroupBox(self.page_Librarian)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(10, 290, 321, 281))
        self.groupBox_12.setFont(font4)
        self.groupBox_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.label_40 = QLabel(self.groupBox_12)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 40, 201, 16))
        self.tableWidget_4 = QTableWidget(self.groupBox_12)
        if (self.tableWidget_4.columnCount() < 3):
            self.tableWidget_4.setColumnCount(3)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(10, 80, 301, 201))
        self.tableWidget_4.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"color: rgb(0, 0, 0);")
        self.tableWidget_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_4.setShowGrid(False)
        self.tableWidget_4.setRowCount(0)
        self.label_41 = QLabel(self.page_Librarian)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(20, 10, 521, 61))
        self.label_41.setFont(font)
        self.label_41.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.groupBox_13 = QGroupBox(self.page_Librarian)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(220, 90, 191, 171))
        self.groupBox_13.setFont(font4)
        self.groupBox_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.label_42 = QLabel(self.groupBox_13)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(10, 40, 61, 16))
        self.lbl_first_2 = QLabel(self.groupBox_13)
        self.lbl_first_2.setObjectName(u"lbl_first_2")
        self.lbl_first_2.setGeometry(QRect(80, 40, 47, 14))
        self.label_43 = QLabel(self.groupBox_13)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(10, 70, 61, 16))
        self.lbl_last_2 = QLabel(self.groupBox_13)
        self.lbl_last_2.setObjectName(u"lbl_last_2")
        self.lbl_last_2.setGeometry(QRect(80, 70, 47, 14))
        self.lbl_email_2 = QLabel(self.groupBox_13)
        self.lbl_email_2.setObjectName(u"lbl_email_2")
        self.lbl_email_2.setGeometry(QRect(80, 100, 47, 14))
        self.label_44 = QLabel(self.groupBox_13)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(10, 100, 47, 14))
        self.label_45 = QLabel(self.groupBox_13)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(10, 130, 47, 14))
        self.lbl_dob_2 = QLabel(self.groupBox_13)
        self.lbl_dob_2.setObjectName(u"lbl_dob_2")
        self.lbl_dob_2.setGeometry(QRect(80, 130, 47, 14))
        self.lbl_fines_2 = QLabel(self.groupBox_13)
        self.lbl_fines_2.setObjectName(u"lbl_fines_2")
        self.lbl_fines_2.setGeometry(QRect(80, 160, 47, 14))
        self.label_46 = QLabel(self.groupBox_13)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(10, 160, 47, 14))
        self.groupBox_14 = QGroupBox(self.page_Librarian)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setGeometry(QRect(350, 290, 321, 281))
        self.groupBox_14.setFont(font4)
        self.groupBox_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.label_47 = QLabel(self.groupBox_14)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(10, 40, 201, 16))
        self.tableWidget_5 = QTableWidget(self.groupBox_14)
        if (self.tableWidget_5.columnCount() < 3):
            self.tableWidget_5.setColumnCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setGeometry(QRect(10, 80, 301, 201))
        self.tableWidget_5.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"color: rgb(0, 0, 0);")
        self.tableWidget_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_5.setShowGrid(False)
        self.tableWidget_5.setRowCount(0)
        self.groupBox_15 = QGroupBox(self.page_Librarian)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(430, 90, 261, 171))
        self.groupBox_15.setFont(font4)
        self.groupBox_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.label_48 = QLabel(self.groupBox_15)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(10, 30, 281, 16))
        self.first_5 = QLineEdit(self.groupBox_15)
        self.first_5.setObjectName(u"first_5")
        self.first_5.setEnabled(True)
        self.first_5.setGeometry(QRect(10, 50, 113, 20))
        self.first_5.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.btn_Request = QPushButton(self.groupBox_15)
        self.btn_Request.setObjectName(u"btn_Request")
        self.btn_Request.setGeometry(QRect(10, 80, 75, 23))
        self.btn_Request.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.first_10 = QLineEdit(self.groupBox_15)
        self.first_10.setObjectName(u"first_10")
        self.first_10.setEnabled(True)
        self.first_10.setGeometry(QRect(10, 110, 113, 20))
        self.first_10.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.btn_Remove = QPushButton(self.groupBox_15)
        self.btn_Remove.setObjectName(u"btn_Remove")
        self.btn_Remove.setGeometry(QRect(10, 140, 75, 23))
        self.btn_Remove.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.groupBox_16 = QGroupBox(self.page_Librarian)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setGeometry(QRect(10, 90, 191, 171))
        self.groupBox_16.setFont(font4)
        self.groupBox_16.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.label_53 = QLabel(self.groupBox_16)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(10, 30, 111, 16))
        self.first_6 = QLineEdit(self.groupBox_16)
        self.first_6.setObjectName(u"first_6")
        self.first_6.setEnabled(True)
        self.first_6.setGeometry(QRect(10, 50, 113, 20))
        self.first_6.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.btn_Scan = QPushButton(self.groupBox_16)
        self.btn_Scan.setObjectName(u"btn_Scan")
        self.btn_Scan.setGeometry(QRect(10, 80, 75, 23))
        self.btn_Scan.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.groupBox_17 = QGroupBox(self.page_Librarian)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setGeometry(QRect(710, 90, 191, 121))
        self.groupBox_17.setFont(font4)
        self.groupBox_17.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.btn_Checkout = QPushButton(self.groupBox_17)
        self.btn_Checkout.setObjectName(u"btn_Checkout")
        self.btn_Checkout.setGeometry(QRect(10, 80, 75, 23))
        self.btn_Checkout.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.first_7 = QLineEdit(self.groupBox_17)
        self.first_7.setObjectName(u"first_7")
        self.first_7.setEnabled(True)
        self.first_7.setGeometry(QRect(10, 50, 113, 20))
        self.first_7.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.label_55 = QLabel(self.groupBox_17)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(10, 30, 111, 16))
        self.groupBox_18 = QGroupBox(self.page_Librarian)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setGeometry(QRect(710, 230, 191, 121))
        self.groupBox_18.setFont(font4)
        self.groupBox_18.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.first_9 = QLineEdit(self.groupBox_18)
        self.first_9.setObjectName(u"first_9")
        self.first_9.setEnabled(True)
        self.first_9.setGeometry(QRect(10, 50, 113, 20))
        self.first_9.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.label_57 = QLabel(self.groupBox_18)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(10, 30, 111, 16))
        self.btn_Checkin = QPushButton(self.groupBox_18)
        self.btn_Checkin.setObjectName(u"btn_Checkin")
        self.btn_Checkin.setGeometry(QRect(10, 90, 75, 23))
        self.btn_Checkin.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.line = QFrame(self.page_Librarian)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(200, 80, 20, 191))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.page_Librarian)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(410, 80, 20, 201))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.page_Librarian)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(690, 80, 20, 281))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.page_Librarian)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(330, 290, 20, 281))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self.page_Librarian)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(700, 210, 211, 20))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_6 = QFrame(self.page_Librarian)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(10, 270, 681, 16))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.Pages_Widget.addWidget(self.page_Librarian)
        self.page_signup = QWidget()
        self.page_signup.setObjectName(u"page_signup")
        self.label_7 = QLabel(self.page_signup)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 10, 401, 101))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.groupBox_3 = QGroupBox(self.page_signup)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 140, 601, 421))
        self.groupBox_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        self.first = QLineEdit(self.groupBox_3)
        self.first.setObjectName(u"first")
        self.first.setGeometry(QRect(10, 60, 113, 20))
        self.first.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.password = QLineEdit(self.groupBox_3)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(10, 300, 113, 20))
        self.password.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.email = QLineEdit(self.groupBox_3)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(10, 180, 113, 20))
        self.email.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.dateEdit = QDateEdit(self.groupBox_3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(10, 240, 110, 22))
        self.dateEdit.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"border: none;")
        self.dateEdit.setFrame(False)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setCalendarPopup(True)
        self.last = QLineEdit(self.groupBox_3)
        self.last.setObjectName(u"last")
        self.last.setGeometry(QRect(10, 120, 113, 20))
        self.last.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 40, 61, 16))
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 220, 61, 16))
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 160, 61, 16))
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 100, 61, 16))
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 280, 61, 16))
        self.btn_signup_2 = QPushButton(self.groupBox_3)
        self.btn_signup_2.setObjectName(u"btn_signup_2")
        self.btn_signup_2.setGeometry(QRect(10, 330, 112, 75))
        sizePolicy.setHeightForWidth(self.btn_signup_2.sizePolicy().hasHeightForWidth())
        self.btn_signup_2.setSizePolicy(sizePolicy)
        self.btn_signup_2.setMinimumSize(QSize(100, 75))
        self.btn_signup_2.setMaximumSize(QSize(112, 75))
        self.btn_signup_2.setFont(font1)
        self.btn_signup_2.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.btn_signup_2.setIcon(icon5)
        self.Pages_Widget.addWidget(self.page_signup)

        self.verticalLayout_4.addWidget(self.Pages_Widget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages_Widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"Toggle", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_librarian.setText(QCoreApplication.translate("MainWindow", u"Librarian", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Simple Library", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_signup.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Search Page", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Select search ", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Search boxes", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Author name", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Title", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter genre", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Book ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Availability", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Login page", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Login Using Email and Password", None))
        self.password_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.email_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example@gmail.com", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_login_2.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_password.setText(QCoreApplication.translate("MainWindow", u"Forgot Password", None))
        self.lbl_InPassword.setText(QCoreApplication.translate("MainWindow", u"Incorrect Password Label", None))
        self.lbl_InEmail.setText(QCoreApplication.translate("MainWindow", u"Incorrect Email Label ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Password reset page", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Reset Password now", None))
        self.first_2.setText("")
        self.first_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bob", None))
        self.new_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.email_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example@gmail.com", None))
        self.last_2.setText("")
        self.last_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Smith", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Reset Password now", None))
        self.first_4.setText("")
        self.first_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bob", None))
        self.new_password_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.email_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example@gmail.com", None))
        self.last_3.setText("")
        self.last_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Smith", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.btn_Librarian_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Password reset page", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"User Account Information:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.lbl_first.setText(QCoreApplication.translate("MainWindow", u"Ex", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.lbl_last.setText(QCoreApplication.translate("MainWindow", u"Ex", None))
        self.lbl_email.setText(QCoreApplication.translate("MainWindow", u"Ex", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"DOB:", None))
        self.lbl_dob.setText(QCoreApplication.translate("MainWindow", u"Ex", None))
        self.lbl_fines.setText(QCoreApplication.translate("MainWindow", u"Ex", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Fines:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Welcome to the User Page", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"User Current Books Information", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Currenty Checked Books:", None))
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Book ID", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Return Date", None));
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Requested Holds", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Currenty Requested Books:", None))
        ___qtablewidgetitem6 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Book ID", None));
        ___qtablewidgetitem7 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem8 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Requested Date", None));
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Request a Book", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Enter Book ID to check if reuqest is available:", None))
        self.first_3.setText("")
        self.first_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1234567", None))
        self.btn_request.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.first_11.setText("")
        self.first_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1234567", None))
        self.btn_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Login Using Email and Password", None))
        self.password_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.email_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example@gmail.com", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_Librarian_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_Librarian_password.setText(QCoreApplication.translate("MainWindow", u"Forgot Password", None))
        self.lbl_InPassword_2.setText(QCoreApplication.translate("MainWindow", u"Incorrect Password Label", None))
        self.lbl_InEmail_2.setText(QCoreApplication.translate("MainWindow", u"Incorrect Email Label ", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Librarian Login page", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"User Current Books Information", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Currenty Checked Books:", None))
        ___qtablewidgetitem9 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Book ID", None));
        ___qtablewidgetitem10 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem11 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Return Date", None));
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Librarian Page", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"User Account Information:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.lbl_first_2.setText(QCoreApplication.translate("MainWindow", u"Ex", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.lbl_last_2.setText(QCoreApplication.translate("MainWindow", u"Ex", None))
        self.lbl_email_2.setText(QCoreApplication.translate("MainWindow", u"Ex", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"DOB:", None))
        self.lbl_dob_2.setText(QCoreApplication.translate("MainWindow", u"Ex", None))
        self.lbl_fines_2.setText(QCoreApplication.translate("MainWindow", u"Ex", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Fines:", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Requested Holds", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Currenty Requested Books:", None))
        ___qtablewidgetitem12 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Book ID", None));
        ___qtablewidgetitem13 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem14 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Requested Date", None));
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Request or Remove a Book for User", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Enter Book ID to check if reuqest is available:", None))
        self.first_5.setText("")
        self.first_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1234567", None))
        self.btn_Request.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.first_10.setText("")
        self.first_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1234567", None))
        self.btn_Remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Scan User", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Enter User ID:", None))
        self.first_6.setText("")
        self.first_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1234567", None))
        self.btn_Scan.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Check Out", None))
        self.btn_Checkout.setText(QCoreApplication.translate("MainWindow", u"Check Out", None))
        self.first_7.setText("")
        self.first_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1234567", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Enter Book ID:", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Check In", None))
        self.first_9.setText("")
        self.first_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1234567", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Enter Book ID:", None))
        self.btn_Checkin.setText(QCoreApplication.translate("MainWindow", u"Check Out", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Sign Up page", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"No Account? No Problem, create one today!!!", None))
        self.first.setText("")
        self.first.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bob", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example@gmail.com", None))
        self.last.setText("")
        self.last.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Smith", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_signup_2.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
    # retranslateUi

