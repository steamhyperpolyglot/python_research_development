# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 435)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_counter = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("CPMono")
        font.setPointSize(28)
        self.lbl_counter.setFont(font)
        self.lbl_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_counter.setObjectName("lbl_counter")
        self.verticalLayout.addWidget(self.lbl_counter)
        self.btn_inc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_inc.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.btn_inc.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_inc.setIcon(icon)
        self.btn_inc.setIconSize(QtCore.QSize(24, 24))
        self.btn_inc.setObjectName("btn_inc")
        self.verticalLayout.addWidget(self.btn_inc)
        self.btn_dec = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dec.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.btn_dec.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_dec.setIcon(icon1)
        self.btn_dec.setIconSize(QtCore.QSize(24, 24))
        self.btn_dec.setObjectName("btn_dec")
        self.verticalLayout.addWidget(self.btn_dec)
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.btn_reset.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/arrow-return-180-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reset.setIcon(icon2)
        self.btn_reset.setIconSize(QtCore.QSize(24, 24))
        self.btn_reset.setObjectName("btn_reset")
        self.verticalLayout.addWidget(self.btn_reset)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_counter.setText(_translate("MainWindow", "TextLabel"))
        self.btn_inc.setText(_translate("MainWindow", "Increment"))
        self.btn_dec.setText(_translate("MainWindow", "Decrement"))
        self.btn_reset.setText(_translate("MainWindow", "Reset"))

