# -*- coding: utf-8 -*-

import time
from PyQt5.QtCore import pyqtSlot,QDate
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog, QCalendarWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlQuery
from UI__NewJobWindow import Ui_Dialog
from Def import *



class NewJobWindow(QDialog, Ui_Dialog):
    def __init__(self, db, parent=None):
        super(NewJobWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        #点击确认提交

    def accept(self):
        if self.jobName_LineEdit.text() == "":
            QMessageBox.information(self, "提示", "需求名称为空！")
        elif self.operator_LineEdit.text() == "":
            QMessageBox.information(self, "提示", "执行人为空！")
        elif self.officer_LineEdit.text() == "":
            QMessageBox.information(self, "提示", "负责人为空！")
        elif self.order_Label.text() == "":
            QMessageBox.information(self, "提示", "提出人为空！")
        else:
            priority = int(self.priority_LineEdit.text())
            jobName = self.jobName_LineEdit.text().replace('\n', '').replace(',', '')
            jobType = self.jobType_LineEdit.currentText()
            jobCount = int(self.jobCount_LineEdit.text())
            jobStaus = self.jobStaus_LineEdit.currentText()
            jobEmergencyLevel = self.jobEmergencyLevel_LineEdit.currentText()
            planingFinishDate = self.planingFinishDate_LineEdit.text()
            operator = self.operator_LineEdit.text()
            officer = self.officer_LineEdit.text()
            order = self.order_LineEdit.text().replace('\n', '').replace(',', '')
            orderWay = self.orderWay_LineEdit.currentText()
            startDate = self.startDate_LineEdit.text()
            hopeFinshDate = self.hopeFinshDate_LineEdit.text()
            realFinishDate = self.realFinishDate_LineEdit.text()
            RTMScode_Label = self.RTMScode_LineEdit.text()
            jobProgress = self.jobProgress_TextEdit.toPlainText()
            jobID = self.jobID_LineEdit.text()
            #插入数据库
            query = QSqlQuery()
            insertNewJobInfo = "insert into jobs values(" \
                               "'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"\
                .format(
                priority, jobName, jobType, jobCount, jobStaus, jobEmergencyLevel, planingFinishDate, operator, officer,
                order, orderWay, startDate, hopeFinshDate, realFinishDate, RTMScode_Label, jobProgress, jobID)
            #数据库返回插入成功还是失败
            r = query.exec(insertNewJobInfo)
            # 判断如果数据库插入成功并且创建文件夹被勾选，截图没勾选，则创建文件夹
            if r and self.CreatePath.isChecked() and not self.GrabScreen.isChecked():
                #构造文件夹名称：D:\@\年\月\需求提出人-需求名称
                JobName = self.jobName_LineEdit.text().replace('\n', '').replace(',', '')
                OrderName = self.order_LineEdit.text().replace(',', '')
                DataList = self.startDate_LineEdit.text().split("/")
                Path = 'D:\\@\\work\\' + DataList[0] + '年\\' + DataList[1] + '月\\' + OrderName + '-' + JobName
                #如果文件夹已经存在了，则不创建文件夹了
                if os.path.exists(Path):
                    QMessageBox.information(self, "文件夹已存在", "文件夹已存在！不会重复创建了哟！可能是需求名称重复了呢！")
                    return
                try:
                    os.makedirs(Path)  # 如果不存在就创建文件夹
                except:
                    QMessageBox.information(self, "文件夹创建失败", "文件夹<%s>创建失败！" %(Path))
                    return
            #判断如果数据库插入成功并且截图被勾选，则调用截图方法
            elif r and self.GrabScreen.isChecked():
                if self.CreatePath.isChecked():
                    # 如果截图勾选了，并且创建文件夹也勾选了，则创建文件夹，然后截图
                    JobName = self.jobName_LineEdit.text().replace('\n', '').replace(',', '')
                    OrderName = self.order_LineEdit.text().replace(',', '')
                    DataList = self.startDate_LineEdit.text().split("/")
                    Path = 'D:\\@\\work\\' + DataList[0] + '年\\' + DataList[1] + '月\\' + OrderName + '-' + JobName
                    FileName = Path + '\\' + '截屏' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.BMP'
                    if os.path.exists(Path):
                        QMessageBox.information(self, "文件夹已存在", "文件夹已存在！不会重复创建了哟！可能是需求名称重复了呢！")
                        return
                    os.makedirs(Path)
                    Cut(FileName)#调用截图方法
                    QMessageBox.information(self, "截图完成", "截图完成！辛苦啦！这样就不会忘记了哟！")
                elif not self.CreatePath.isChecked():
                    QMessageBox.information(self, "文件夹不存在", "无法截图！需要先创建文件夹哟！")
                    return
            if r:
                self.done(1)
            else:
                QMessageBox.information(self, "提示", "新增失败，貌似已经有相同的工单流水号存在了！")
            self.db.close()


    def reject(self):
        """
        点击取消后
        """
        self.done(-1)

