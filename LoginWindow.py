# -*- coding: utf-8 -*-

import time
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlQuery
from UI__LoginWindow import Ui_LoginWindow
from Def import *



class LoginWindow(QDialog, Ui_LoginWindow):
    # 自定义信号
    mySignal = pyqtSignal(str)
    def __init__(self, db, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.filePath = './res/ini/userinfo.ini'
        self.checkUserInfo()
        #点击确认提交

    #读取配置文件
    def checkUserInfo(self):
        res = readFromUserInfo(self.filePath)
        try:
            if res[2] == '1':
                self.username_LineEdit.setText(res[0])
                self.password_LineEdit.setText(res[1])
                self.keeppassword_Checkbox.setCheckState(2)
        except:
            pass

    def accept(self):
        if self.username_LineEdit.text() == "":
            QMessageBox.information(self, "提示", "用户名为空！")
        elif self.password_LineEdit.text() == "":
            QMessageBox.information(self, "提示", "密码为空！")
        else:
            username = self.username_LineEdit.text()
            password = self.password_LineEdit.text()

            #将用户密码写入配置文件，如果不选就将空值写入配置文件
            if self.keeppassword_Checkbox.isChecked():
                ischecked = '1'
                saveToUserInfo(username, password, ischecked, self.filePath)
            else:
                ischecked = '0'
                saveToUserInfo('none', 'none', ischecked, self.filePath)

            #查询数据库
            query = QSqlQuery()
            selectUser = "select * from user where username = '{}' and password = '{}'".format(username, password)
            #数据库返回插入成功还是失败
            r = query.exec(selectUser)
            res = query.next()
            # 判断如果数据库插入成功并且创建文件夹被勾选，截图没勾选，则创建文件夹
            if r and res :
                QMessageBox.information(self, "成功", "成功！")
                content = self.username_LineEdit.text()
                self.mySignal.emit(content)  # 发射信号
                self.close()
                return
                self.done(1)
            else:
                QMessageBox.information(self, "失败", "失败！")
            #self.db.close()





