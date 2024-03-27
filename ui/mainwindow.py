# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.acnExit = QAction(MainWindow)
        self.acnExit.setObjectName(u"acnExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btnClear = QPushButton(self.groupBox_2)
        self.btnClear.setObjectName(u"btnClear")

        self.gridLayout_4.addWidget(self.btnClear, 0, 1, 1, 1)

        self.btnRefresh = QPushButton(self.groupBox_2)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.gridLayout_4.addWidget(self.btnRefresh, 0, 0, 1, 1)

        self.tblData = QTableWidget(self.groupBox_2)
        if (self.tblData.columnCount() < 4):
            self.tblData.setColumnCount(4)
        self.tblData.setObjectName(u"tblData")
        self.tblData.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tblData.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblData.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblData.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblData.setWordWrap(True)
        self.tblData.setColumnCount(4)
        self.tblData.horizontalHeader().setVisible(True)
        self.tblData.horizontalHeader().setDefaultSectionSize(100)
        self.tblData.horizontalHeader().setHighlightSections(True)
        self.tblData.horizontalHeader().setStretchLastSection(True)
        self.tblData.verticalHeader().setVisible(False)

        self.gridLayout_4.addWidget(self.tblData, 1, 0, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblName_5 = QLabel(self.groupBox_3)
        self.lblName_5.setObjectName(u"lblName_5")

        self.gridLayout_2.addWidget(self.lblName_5, 0, 0, 1, 1)

        self.txtSearchID = QLineEdit(self.groupBox_3)
        self.txtSearchID.setObjectName(u"txtSearchID")

        self.gridLayout_2.addWidget(self.txtSearchID, 0, 1, 1, 1)

        self.lblName_2 = QLabel(self.groupBox_3)
        self.lblName_2.setObjectName(u"lblName_2")

        self.gridLayout_2.addWidget(self.lblName_2, 1, 0, 1, 1)

        self.txtSearchName = QLineEdit(self.groupBox_3)
        self.txtSearchName.setObjectName(u"txtSearchName")

        self.gridLayout_2.addWidget(self.txtSearchName, 1, 1, 1, 1)

        self.lblName_3 = QLabel(self.groupBox_3)
        self.lblName_3.setObjectName(u"lblName_3")

        self.gridLayout_2.addWidget(self.lblName_3, 2, 0, 1, 1)

        self.txtSearchLast = QLineEdit(self.groupBox_3)
        self.txtSearchLast.setObjectName(u"txtSearchLast")

        self.gridLayout_2.addWidget(self.txtSearchLast, 2, 1, 1, 1)

        self.lblName_4 = QLabel(self.groupBox_3)
        self.lblName_4.setObjectName(u"lblName_4")

        self.gridLayout_2.addWidget(self.lblName_4, 3, 0, 1, 1)

        self.txtSearchEmail = QLineEdit(self.groupBox_3)
        self.txtSearchEmail.setObjectName(u"txtSearchEmail")

        self.gridLayout_2.addWidget(self.txtSearchEmail, 3, 1, 1, 1)

        self.btnSearch = QPushButton(self.groupBox_3)
        self.btnSearch.setObjectName(u"btnSearch")

        self.gridLayout_2.addWidget(self.btnSearch, 4, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblName = QLabel(self.groupBox)
        self.lblName.setObjectName(u"lblName")

        self.gridLayout.addWidget(self.lblName, 0, 0, 1, 1)

        self.lblEmail = QLabel(self.groupBox)
        self.lblEmail.setObjectName(u"lblEmail")

        self.gridLayout.addWidget(self.lblEmail, 2, 0, 1, 1)

        self.txtName = QLineEdit(self.groupBox)
        self.txtName.setObjectName(u"txtName")

        self.gridLayout.addWidget(self.txtName, 0, 1, 1, 1)

        self.lblLast = QLabel(self.groupBox)
        self.lblLast.setObjectName(u"lblLast")

        self.gridLayout.addWidget(self.lblLast, 1, 0, 1, 1)

        self.txtLast = QLineEdit(self.groupBox)
        self.txtLast.setObjectName(u"txtLast")

        self.gridLayout.addWidget(self.txtLast, 1, 1, 1, 1)

        self.btnAdd = QPushButton(self.groupBox)
        self.btnAdd.setObjectName(u"btnAdd")

        self.gridLayout.addWidget(self.btnAdd, 3, 0, 1, 1)

        self.btnRemove = QPushButton(self.groupBox)
        self.btnRemove.setObjectName(u"btnRemove")

        self.gridLayout.addWidget(self.btnRemove, 3, 2, 1, 1)

        self.txtEmail = QLineEdit(self.groupBox)
        self.txtEmail.setObjectName(u"txtEmail")

        self.gridLayout.addWidget(self.txtEmail, 2, 1, 1, 1)

        self.btnUpdate = QPushButton(self.groupBox)
        self.btnUpdate.setObjectName(u"btnUpdate")

        self.gridLayout.addWidget(self.btnUpdate, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txtName, self.txtLast)
        QWidget.setTabOrder(self.txtLast, self.txtEmail)
        QWidget.setTabOrder(self.txtEmail, self.btnAdd)
        QWidget.setTabOrder(self.btnAdd, self.btnUpdate)
        QWidget.setTabOrder(self.btnUpdate, self.btnRemove)
        QWidget.setTabOrder(self.btnRemove, self.txtSearchID)
        QWidget.setTabOrder(self.txtSearchID, self.txtSearchName)
        QWidget.setTabOrder(self.txtSearchName, self.txtSearchLast)
        QWidget.setTabOrder(self.txtSearchLast, self.txtSearchEmail)
        QWidget.setTabOrder(self.txtSearchEmail, self.btnSearch)
        QWidget.setTabOrder(self.btnSearch, self.btnRefresh)
        QWidget.setTabOrder(self.btnRefresh, self.btnClear)
        QWidget.setTabOrder(self.btnClear, self.tblData)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.acnExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.acnExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btnRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Search", None))
        self.lblName_5.setText(QCoreApplication.translate("MainWindow", u"ID: ", None))
        self.lblName_2.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.lblName_3.setText(QCoreApplication.translate("MainWindow", u"Last Name: ", None))
        self.lblName_4.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.btnSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Details", None))
        self.lblName.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.lblEmail.setText(QCoreApplication.translate("MainWindow", u"Email: ", None))
        self.lblLast.setText(QCoreApplication.translate("MainWindow", u"Last Name: ", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btnRemove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.btnUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

