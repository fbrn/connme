# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainDialog.ui'
#
# Created: Tue Apr 16 17:39:58 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName(_fromUtf8("MainDialog"))
        MainDialog.resize(265, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("/usr/share/pixmaps/connme.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainDialog.setWindowIcon(icon)

        self.setFixedSize(self.size())
        self.tabWidget = QtGui.QTabWidget(MainDialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 241, 275))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.setting = QtGui.QWidget()
        self.setting.setObjectName(_fromUtf8("setting"))
        self.gridLayout = QtGui.QGridLayout(self.setting)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_4 = QtGui.QLabel(self.setting)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_8.addWidget(self.label_4)
        self.label_2 = QtGui.QLabel(self.setting)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_8.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.setting)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_8.addWidget(self.label_3)
        self.label_5 = QtGui.QLabel(self.setting)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_8.addWidget(self.label_5)
        self.label = QtGui.QLabel(self.setting)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_8.addWidget(self.label)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.lineEdit_2 = QtGui.QLineEdit(self.setting)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_7.addWidget(self.lineEdit_2)
        self.comboBox_2 = QtGui.QComboBox(self.setting)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.verticalLayout_7.addWidget(self.comboBox_2)
        self.comboBox = QtGui.QComboBox(self.setting)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout_7.addWidget(self.comboBox)
        self.comboBox_3 = QtGui.QComboBox(self.setting)
        self.comboBox_3.setMaxVisibleItems(3)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.verticalLayout_7.addWidget(self.comboBox_3)
        self.lineEdit = QtGui.QLineEdit(self.setting)
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_7.addWidget(self.lineEdit)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.lineEdit_3 = QtGui.QLineEdit(self.setting)
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.verticalLayout_9.addWidget(self.lineEdit_3)
        self.pushButton = QtGui.QPushButton(self.setting)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_9.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout_9, 1, 0, 1, 1)
        self.tabWidget.addTab(self.setting, _fromUtf8(""))
        self.client = QtGui.QWidget()
        self.client.setObjectName(_fromUtf8("client"))
        self.tableWidget = QtGui.QTableWidget(self.client)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 221, 231))
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setResizeMode(0,QtGui.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setResizeMode(0,QtGui.QHeaderView.Interactive)
        self.tableWidget.horizontalHeader().resizeSection(0, 150);
        self.tableWidget.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.client, _fromUtf8(""))

        self.retranslateUi(MainDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)
        MainDialog.setTabOrder(self.lineEdit_2, self.comboBox_2)
        MainDialog.setTabOrder(self.comboBox_2, self.comboBox)
        MainDialog.setTabOrder(self.comboBox, self.comboBox_3)
        MainDialog.setTabOrder(self.comboBox_3, self.lineEdit)
        MainDialog.setTabOrder(self.lineEdit, self.tabWidget)
        MainDialog.setTabOrder(self.tabWidget, self.pushButton)
        MainDialog.setTabOrder(self.pushButton, self.lineEdit_3)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(QtGui.QApplication.translate("MainDialog", "Connme", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainDialog", "Hotspot Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainDialog", "Internet to share", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainDialog", "Share over", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainDialog", "Sharing Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainDialog", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(0, QtGui.QApplication.translate("MainDialog", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(1, QtGui.QApplication.translate("MainDialog", "Encrypted (WPA)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(2, QtGui.QApplication.translate("MainDialog", "Encryptred (WPA2)", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setText(QtGui.QApplication.translate("MainDialog", "Hotspot Stopped", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainDialog", "Start Hotspot", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting), QtGui.QApplication.translate("MainDialog", "Setting", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainDialog", "Hostname", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainDialog", "Internet", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.client), QtGui.QApplication.translate("MainDialog", "Client", None, QtGui.QApplication.UnicodeUTF8))
