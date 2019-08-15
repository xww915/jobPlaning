# -*- coding: utf-8 -*-

import time
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlQuery
from UI__SendOrderWindow import Ui_SendOrderWindow
from Def import *



class SendOrderWindow(QDialog, Ui_SendOrderWindow):
    # 自定义信号
    mySignal = pyqtSignal(str)
    def __init__(self, db, parent=None):
        super(SendOrderWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.readUserInfo()
        self.sendOrder_LineEdit.currentTextChanged.connect(self.showInfo)
        self.choose_PushButton.clicked.connect(self.addOperators)
        self.clear_PushButton.clicked.connect(self.chooseOrders_LineEdit.clear)

    #读取用户积分介绍等详细信息
    def showInfo(self):
        query = QSqlQuery()
        selectUserinfo = "select username,credit,introduction from user where username = '{}'".format(self.sendOrder_LineEdit.currentText())
        # 数据库返回插入成功还是失败
        query.exec(selectUserinfo)
        while query.next():
            self.name_LineEdit.setText(query.value(0))
            self.credits_LineEdit.setText(query.value(1))
            self.introduc_LineEdit.setText(query.value(2))

    # 添加用户
    def addOperators(self):
        if not self.chooseOrders_LineEdit.text():
            self.chooseOrders_LineEdit.setText(self.name_LineEdit.text())
        else:
            self.chooseOrders_LineEdit.setText(self.chooseOrders_LineEdit.text() + ' '+ self.name_LineEdit.text())

    #读取用户列表
    def readUserInfo(self):
        # 查询数据库
        query = QSqlQuery()
        selectUsers = "select username from user"
        # 数据库返回插入成功还是失败
        query.exec(selectUsers)
        while query.next():
            self.sendOrder_LineEdit.addItem(query.value(0))

    # 点击确认提交
    def accept(self):
        if self.chooseOrders_LineEdit.text():
            self.mySignal.emit(self.chooseOrders_LineEdit.text())
            self.done(1)
        else:
            self.done(-1)


    def reject(self):
        """
        点击取消后
        """
        self.done(-1)


