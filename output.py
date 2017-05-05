# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
from __future__ import print_function

from PyQt5 import QtCore, QtGui, QtWidgets
import httplib2
import os
from os import system
from data import *
from copy import copy

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
    
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'IITB Course Calendar'

class Ui_MainWindow(object):
    loggedIn = False
    dataPresent = True
    addedToCalendar = False
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 642)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 961, 261))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(480, 280, 481, 341))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.gridLayoutWidget_3)
        self.commandLinkButton.setAutoDefault(False)
        self.commandLinkButton.setDefault(False)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.gridLayout_3.addWidget(self.commandLinkButton, 1, 0, 1, 1)
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget_3)
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.gridLayout_3.addWidget(self.commandLinkButton_4, 2, 0, 1, 1)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget_3)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.gridLayout_3.addWidget(self.commandLinkButton_2, 1, 1, 1, 1)
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget_3)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.gridLayout_3.addWidget(self.commandLinkButton_3, 0, 0, 1, 1)
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget_3)
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.gridLayout_3.addWidget(self.commandLinkButton_6, 2, 1, 1, 1)
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget_3)
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        self.gridLayout_3.addWidget(self.commandLinkButton_5, 0, 1, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 380, 461, 221))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_4.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAutoFillBackground(True)
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_4.addWidget(self.lineEdit_4, 4, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(True)
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.dateEdit_4 = QtWidgets.QDateEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.dateEdit_4.setFont(font)
        self.dateEdit_4.setAutoFillBackground(True)
        self.dateEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_4.setDate(QtCore.QDate(2000, 1, 1))
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.gridLayout_4.addWidget(self.dateEdit_4, 5, 0, 1, 1)
        self.dateEdit_3 = QtWidgets.QDateEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.dateEdit_3.setFont(font)
        self.dateEdit_3.setAutoFillBackground(True)
        self.dateEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_3.setDate(QtCore.QDate(2000, 1, 2))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.gridLayout_4.addWidget(self.dateEdit_3, 5, 1, 1, 1)
        self.dateEdit_6 = QtWidgets.QDateEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dateEdit_6.setFont(font)
        self.dateEdit_6.setAutoFillBackground(True)
        self.dateEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_6.setDate(QtCore.QDate(2000, 1, 1))
        self.dateEdit_6.setObjectName("dateEdit_6")
        self.gridLayout_4.addWidget(self.dateEdit_6, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_3.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAutoFillBackground(True)
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 4, 0, 1, 1)
        self.dateEdit_5 = QtWidgets.QDateEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.dateEdit_5.setFont(font)
        self.dateEdit_5.setAutoFillBackground(True)
        self.dateEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_5.setDate(QtCore.QDate(2000, 1, 2))
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.gridLayout_4.addWidget(self.dateEdit_5, 2, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAutoFillBackground(True)
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 3, 0, 1, 2)
        self.gridLayout_4.setRowStretch(0, 10)
        self.gridLayout_4.setRowStretch(3, 2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 280, 461, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commandLinkButton_9 = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton_9.setObjectName("commandLinkButton_9")
        self.horizontalLayout.addWidget(self.commandLinkButton_9)
        self.commandLinkButton_8 = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton_8.setObjectName("commandLinkButton_8")
        self.horizontalLayout.addWidget(self.commandLinkButton_8)
        self.commandLinkButton_7 = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton_7.setObjectName("commandLinkButton_7")
        self.horizontalLayout.addWidget(self.commandLinkButton_7)
        self.tableWidget.raise_()
        self.gridLayoutWidget_3.raise_()
        self.gridLayoutWidget_4.raise_()
        self.horizontalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 981, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.initialiseMembers();
        self.connectSignals()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
     
    def connectSignals(self):
        self.commandLinkButton_7.pressed.connect(self.addRow)
        self.commandLinkButton_8.pressed.connect(self.removeRow)
        self.commandLinkButton.pressed.connect(self.login)
        self.commandLinkButton_2.pressed.connect(self.logout)
        self.commandLinkButton_3.pressed.connect(self.save)
        self.commandLinkButton_5.pressed.connect(self.delete)
        self.commandLinkButton_9.pressed.connect(self.resetTable)
        self.tableWidget.cellChanged.connect(self.tableWidget.resizeColumnsToContents)
    
    def resetTable(self):
        self.tableWidget.clearContents();
        for i in range(self.tableWidget.rowCount()):
            self.createSlotComboBox(i)
            self.createTutorialComboBox(i)
    
    def initialiseMembers(self):
        home_dir = os.path.expanduser('./.data/')
        if not os.path.exists(home_dir):
            os.mkdir(home_dir)
            
        credential_dir = os.path.join(home_dir, '.credentials')
        data_path = os.path.join(home_dir, 'courses.csv')
        self.loggedIn = os.path.exists(credential_dir)        
        self.dataPresent = os.path.exists(data_path)
        
    def login(self):
        if (self.loggedIn):
            self.error_dialog = QtWidgets.QMessageBox()
            self.error_dialog.setIcon(QtWidgets.QMessageBox.Information)
            self.error_dialog.setText('Already Logged In')
            self.error_dialog.setWindowTitle('Information')
            self.error_dialog.setStandardButtons(QtWidgets.QMessageBox.Close)
            self.error_dialog.exec_()
        else:    
            home_dir = os.path.expanduser('./.data/')
            credential_dir = os.path.join(home_dir, '.credentials')
            os.makedirs(credential_dir)
            credential_path = os.path.join(credential_dir, 'IITB-course-calendar.json')

            store = Storage(credential_path)
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
                    
            self.credentials = credentials;
            self.error_dialog = QtWidgets.QMessageBox()
            self.error_dialog.setIcon(QtWidgets.QMessageBox.Information)
            self.error_dialog.setText('Logged In Successfully!')
            self.error_dialog.setWindowTitle('Information')
            self.error_dialog.setStandardButtons(QtWidgets.QMessageBox.Close)
            self.error_dialog.exec_()
            
        self.loggedIn = True;
    
    def logout(self):
        home_dir = os.path.expanduser('./.data')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not self.loggedIn:
            self.error_dialog = QtWidgets.QMessageBox()
            self.error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
            self.error_dialog.setText('Not Logged In')
            self.error_dialog.setWindowTitle('Error')
            self.error_dialog.setStandardButtons(QtWidgets.QMessageBox.Close)
            self.error_dialog.exec_()
        else:
            os.remove(os.path.join(credential_dir, 'IITB-course-calendar.json'))
            os.rmdir(credential_dir)
            self.error_dialog = QtWidgets.QMessageBox()
            self.error_dialog.setIcon(QtWidgets.QMessageBox.Information)
            self.error_dialog.setText('Successfully Logged Out')
            self.error_dialog.setWindowTitle('Information')
            self.error_dialog.setStandardButtons(QtWidgets.QMessageBox.Close)
            self.error_dialog.exec_()
            self.loggedIn = False
            
    def save(self):
        home_dir = os.path.expanduser('./.data/courses.csv')
        saveFile = open(home_dir, 'w')
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                if isinstance(self.tableWidget.cellWidget(i,j), QtWidgets.QComboBox):
                    saveFile.write(self.tableWidget.cellWidget(i, j).currentText() + ',')
                elif not (self.tableWidget.item(i, j) is None):
                    saveFile.write(self.tableWidget.item(i, j).text() + ',')
                else:
                    saveFile.write(',')
            saveFile.write('\n')
        
        self.error_dialog = QtWidgets.QMessageBox()
        self.error_dialog.setIcon(QtWidgets.QMessageBox.Information)
        self.error_dialog.setText('Course Data Stored!')
        self.error_dialog.setWindowTitle('Information')
        self.error_dialog.setStandardButtons(QtWidgets.QMessageBox.Close)
        self.error_dialog.exec_()
        self.dataPresent = True;
    
    def delete(self):
        if(self.dataPresent):
            home_dir = os.path.expanduser('./.data/courses.csv')
            os.remove(home_dir)
            self.error_dialog = QtWidgets.QMessageBox()
            self.error_dialog.setIcon(QtWidgets.QMessageBox.Information)
            self.error_dialog.setText('Previously stored data deleted successfully!')
            self.error_dialog.setWindowTitle('Information')
            self.error_dialog.setStandardButtons(QtWidgets.QMessageBox.Close)
            self.error_dialog.exec_()
            self.dataPresent = False

        else:
            self.error_dialog = QtWidgets.QMessageBox()
            self.error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
            self.error_dialog.setText('No data present.')
            self.error_dialog.setWindowTitle('Error')
            self.error_dialog.setStandardButtons(QtWidgets.QMessageBox.Close)
            self.error_dialog.exec_()
            
    def addRow(self):
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        self.createSlotComboBox(self.tableWidget.rowCount() - 1)
        self.createTutorialComboBox(self.tableWidget.rowCount() - 1)
        
    def removeRow(self):
        if (self.tableWidget.rowCount() == 1):
            self.error_dialog = QtWidgets.QMessageBox()
            self.error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
            self.error_dialog.setText('Only one row remaining. It cannot be deleted.')
            self.error_dialog.setWindowTitle('Error')
            self.error_dialog.setStandardButtons(QtWidgets.QMessageBox.Close)
            self.error_dialog.exec_()
        else:
            self.tableWidget.removeRow(self.tableWidget.currentRow())
    
    def createSlotComboBox(self, row):
        _translate = QtCore.QCoreApplication.translate
        comboBox = QtWidgets.QComboBox(self.centralWidget)
        comboBox.setGeometry(QtCore.QRect(30, 90, 101, 29))
        comboBox.setObjectName("comboBox")
        
        for i in range(0, 28):
            comboBox.addItem("")
            
        comboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select Slot</p></body></html>"))
        comboBox.setCurrentText(_translate("MainWindow", "1", "Select Slot"))
        comboBox.setItemText(0, _translate("MainWindow", "1"))
        comboBox.setItemText(1, _translate("MainWindow", "2"))
        comboBox.setItemText(2, _translate("MainWindow", "3"))
        comboBox.setItemText(3, _translate("MainWindow", "4"))
        comboBox.setItemText(4, _translate("MainWindow", "5"))
        comboBox.setItemText(5, _translate("MainWindow", "6"))
        comboBox.setItemText(6, _translate("MainWindow", "7"))
        comboBox.setItemText(7, _translate("MainWindow", "8"))
        comboBox.setItemText(8, _translate("MainWindow", "9"))
        comboBox.setItemText(9, _translate("MainWindow", "10"))
        comboBox.setItemText(10, _translate("MainWindow", "11"))
        comboBox.setItemText(11, _translate("MainWindow", "12"))
        comboBox.setItemText(12, _translate("MainWindow", "13"))
        comboBox.setItemText(13, _translate("MainWindow", "14"))
        comboBox.setItemText(14, _translate("MainWindow", "15"))
        comboBox.setItemText(15, _translate("MainWindow", "L1"))
        comboBox.setItemText(16, _translate("MainWindow", "L2"))
        comboBox.setItemText(17, _translate("MainWindow", "L3"))
        comboBox.setItemText(18, _translate("MainWindow", "L4"))
        comboBox.setItemText(19, _translate("MainWindow", "L5"))
        comboBox.setItemText(20, _translate("MainWindow", "L6"))
        comboBox.setItemText(21, _translate("MainWindow", "XA"))
        comboBox.setItemText(22, _translate("MainWindow", "XB"))
        comboBox.setItemText(23, _translate("MainWindow", "XC"))
        comboBox.setItemText(24, _translate("MainWindow", "XD"))
        comboBox.setItemText(25, _translate("MainWindow", "X1"))
        comboBox.setItemText(26, _translate("MainWindow", "X2"))
        comboBox.setItemText(27, _translate("MainWindow", "X3"))
        self.tableWidget.setCellWidget(row, 3, comboBox)
        
    def createTutorialComboBox(self, row):
        _translate = QtCore.QCoreApplication.translate
        comboBox = QtWidgets.QComboBox(self.centralWidget)
        comboBox.setGeometry(QtCore.QRect(30, 80, 101, 29))
        comboBox.setObjectName("comboBox_2")
        
        comboBox.addItem("")        
        comboBox.addItem("")

        comboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Is this a Tutorial Slot? (Y/N)</p></body></html>"))
        comboBox.setCurrentText(_translate("MainWindow", "1", "N"))
        comboBox.setItemText(0, _translate("MainWindow", "N"))
        comboBox.setItemText(1, _translate("MainWindow", "Y"))
        self.tableWidget.setCellWidget(row, 5, comboBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IITB Google Calendar Creator"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Course Code"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Course Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Professor\'s Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Slot"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Location"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Tutorial"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Notification Type"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Notification Time"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Invite"))
        self.commandLinkButton.setText(_translate("MainWindow", "Login"))
        self.commandLinkButton.setDescription(_translate("MainWindow", "Click to Login"))
        self.commandLinkButton_4.setText(_translate("MainWindow", "Add to Calendar"))
        self.commandLinkButton_4.setDescription(_translate("MainWindow", "Add the events to the Online Google Calendar"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "Logout"))
        self.commandLinkButton_2.setDescription(_translate("MainWindow", "Deletes Login Data. Calendar access is revoked."))
        self.commandLinkButton_3.setText(_translate("MainWindow", "Save"))
        self.commandLinkButton_3.setDescription(_translate("MainWindow", "Save Event data in CSV File"))
        self.commandLinkButton_6.setText(_translate("MainWindow", "Delete from Calendar"))
        self.commandLinkButton_6.setDescription(_translate("MainWindow", "Delete the events from the Online Google Calendar"))
        self.commandLinkButton_5.setText(_translate("MainWindow", "Delete"))
        self.commandLinkButton_5.setDescription(_translate("MainWindow", "Delete previously saved data"))
        self.lineEdit_4.setText(_translate("MainWindow", "MidSem End Date"))
        self.lineEdit.setText(_translate("MainWindow", "Sem Start Date"))
        self.dateEdit_4.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.dateEdit_3.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.dateEdit_6.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.lineEdit_3.setText(_translate("MainWindow", "MidSem Start Date"))
        self.dateEdit_5.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.lineEdit_2.setText(_translate("MainWindow", "Sem End Date"))
        self.label.setText(_translate("MainWindow", "Important Dates Details"))
        self.commandLinkButton_9.setText(_translate("MainWindow", "Clear"))
        self.commandLinkButton_9.setDescription(_translate("MainWindow", "Clears the table of its contents"))
        self.commandLinkButton_8.setText(_translate("MainWindow", "Delete Row"))
        self.commandLinkButton_8.setDescription(_translate("MainWindow", "Delete Selected Row"))
        self.commandLinkButton_7.setText(_translate("MainWindow", "Add Row"))
        self.commandLinkButton_7.setDescription(_translate("MainWindow", "At the end of the Table"))
        
        self.createSlotComboBox(0)
        self.createTutorialComboBox(0)
        self.tableWidget.resizeColumnsToContents()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

