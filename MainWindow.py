# -*- coding: utf-8 -*-
'''
pyinstaller -F -w -i res\LOGO.ico runProject.py
'''


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from NewJobWindow import NewJobWindow
from MainWindowSqltablemodel import MainWindowSqlTableModel
from MainWindowDelegate import TableDelegate
from UI__MainWindow import Ui_MainWindow
from LoginWindow import LoginWindow
from SendOrderWindow import SendOrderWindow
from DefRTMS import *
from Def import *
import os
import time
from RTMSThread import *



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, db, offline, parent=None):
        """
        一些初始设置
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = db#引用数据库对象
        self.initUi()
        self.offline_check(offline)
        self.RTMSThred()

    #离线状态校验
    def offline_check(self,offline):
        if offline:
            self.newJob_PushButton.setEnabled(False)
            self.refresh_PushButton.setEnabled(False)
            self.modification_PushButton.setEnabled(False)
        if self.username_Label.text() == '您好啊':
            self.newJob_PushButton.setEnabled(False)
            self.refresh_PushButton.setEnabled(False)
            self.modification_PushButton.setEnabled(False)
            self.searchUndo_PushButton.setEnabled(False)
            self.search_PushButton.setEnabled(False)


    def initUi(self):
        '''
        界面初始设置
        '''
        # QSplitter按窗口索引增加伸缩因子
        # self.splitter.setStretchFactor(0, 6)
        # self.splitter.setStretchFactor(1, 1)
        #self.splitter.setSizes([1000, 1000])

        # 下拉框增加索引关键字
        searchkey = ["工作名称", "工作类型", "当前执行人","工作提出人"]
        self.search_ComboBox.addItems(searchkey)

        self.search_PushButton.clicked.connect(self.on_search_PushButton_clicked)
        self.searchUndo_PushButton.clicked.connect(self.on_searchUndo_PushButton_clicked)
        self.newJob_PushButton.clicked.connect(self.on_newJob_PushButton_clicked)
        self.refresh_PushButton.clicked.connect(self.on_refresh_PushButton_clicked)
        self.modification_PushButton.clicked.connect(self.on_modification_PushButton_clicked)
        self.login_PushButton.clicked.connect(self.on_login_PushButton_clicked)
        self.jobProgress_PushButton.clicked.connect(self.on_jobProgress_PushButton_clicked)
        self.tableView_Left.clicked.connect(self.on_tableView_Left_clicked)

        #左侧数据表格设置
        self.tableView_Left.setIconSize(QSize(25, 25))
        # self.tableView_Left.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 设置点击表头可以排序
        self.tableView_Left.setSortingEnabled(True)

        delegate = TableDelegate()
        self.tableView_Left.setItemDelegate(delegate)
        # 调用我们自定义的代理

        self.setTableModel()
        #self.tableView_Left.setColumnWidth(1, 200)
        self.first_login()

    #初始化登录
    def first_login(self):
        #定义一个登录框的对象
        my = LoginWindow(self.db)
        # 在主窗口中连接信号和槽，把登录框的信号连接到MainWindow的username_Label上
        my.mySignal.connect(self.getDialogSignal)
        #激活登录窗口
        my.exec_()
        #完成后返回主窗口，对任务列表进行过滤
        self.setTableModel()
        self.setFilder()
    #修改工作进展按钮
    def on_jobProgress_PushButton_clicked(self):
        row = self.tableView_Left.currentIndex().row()
        jobProgress = self.jobProgress_TextEdit.toPlainText()
        jobID = self.tablemodel.record(row).value("jobID")
        # 插入数据库
        query = QSqlQuery()
        insertNewJobInfo = 'update jobs set jobProgress = "{}" where jobID = "{}"'.format(jobProgress, jobID)
        # 数据库返回插入成功还是失败
        r = query.exec(insertNewJobInfo)
        if r:
            self.setTableModel()
            self.setFilder()
            QMessageBox.information(self, "工作进展修改已完成", "修改完成了哟！记得提交保存哟！")
        else:
            QMessageBox.critical(self, "工作进展修改失败", "修改失败了哟！请重新试试！")
    #单击显示需求详细信息
    def on_tableView_Left_clicked(self, index):
        row = index.row()
        # 当我们单击表格的时候，取得行号。
        self.priority_LineEdit.setText(str(self.tablemodel.record(row).value("priority")))
        self.jobName_LineEdit.setText(str(self.tablemodel.record(row).value("jobName")))
        self.jobType_LineEdit.setText(str(self.tablemodel.record(row).value("jobType")))
        self.jobCount_LineEdit.setText(str(self.tablemodel.record(row).value("jobCount")))
        self.jobStaus_LineEdit.setText(str(self.tablemodel.record(row).value("jobStaus")))
        self.jobEmergencyLevel_LineEdit.setText(str(self.tablemodel.record(row).value("jobEmergencyLevel")))
        self.planingFinishDate_LineEdit.setText(str(self.tablemodel.record(row).value("planingFinishDate")))
        self.operator_LineEdit.setText(str(self.tablemodel.record(row).value("operator")))
        self.officer_LineEdit.setText(str(self.tablemodel.record(row).value("officer")))
        self.order_LineEdit.setText(str(self.tablemodel.record(row).value("orderName")))
        self.orderWay_LineEdit.setText(str(self.tablemodel.record(row).value("orderWay")))
        self.startDate_LineEdit.setText(str(self.tablemodel.record(row).value("startDate")))
        self.hopeFinshDate_LineEdit.setText(str(self.tablemodel.record(row).value("hopeFinshDate")))
        self.realFinishDate_LineEdit.setText(str(self.tablemodel.record(row).value("realFinishDate")))
        self.RTMScode_LineEdit.setText(str(self.tablemodel.record(row).value("RTMScode")))
        self.jobProgress_TextEdit.setText(str(self.tablemodel.record(row).value("jobProgress")))
        self.jobID_LineEdit.setText(str(self.tablemodel.record(row).value("jobID")))

        # imgPath = self.tablemodel.record(row).value("img")
        # # 图片路径
        # self.label.setPixmap(QPixmap(imgPath))

    #子线程获取当前用户的需求管理系统的用户名密码
    def RTMSThred(self):
        RTMSInfo = getRTMSUserInfo(self.username_Label.text())
        RTMSUsername = RTMSInfo[0]
        RTMSPassword = RTMSInfo[1]
        # 声明线程对象
        self.checkRTMSThread = checkRTMSThread(RTMSUsername, RTMSPassword)
        # 关联信号
        self.checkRTMSThread.show_time.connect(self.showRTMSinfo)
        #启动线程
        self.checkRTMSThread.start()
    def showRTMSinfo(self, file_str):
        self.RTMS_Label.setText(file_str)

    #点击登录功能
    def on_login_PushButton_clicked(self):
        #切换子线程
        self.checkRTMSThread.stop()
        #定义一个登录框的对象
        my = LoginWindow(self.db)
        # 在主窗口中连接信号和槽，把登录框的信号连接到MainWindow的username_Label上
        my.mySignal.connect(self.getDialogSignal)
        #激活登录窗口
        my.exec_()
        #完成后返回主窗口，对任务列表进行过滤
        self.setTableModel()
        self.setFilder()
        #激活子线程
        self.RTMSThred()
    def getDialogSignal(self, connect):
        self.username_Label.setText(connect)

    #过滤出当前登录用户的数据
    def setFilder(self):
        usernametext = self.username_Label.text()
        if usernametext == "您好啊":
            pass
        elif usernametext == "root":
            self.newJob_PushButton.setEnabled(True)
            self.refresh_PushButton.setEnabled(True)
            self.modification_PushButton.setEnabled(True)
            self.searchUndo_PushButton.setEnabled(True)
            self.search_PushButton.setEnabled(True)
            pass
        else:
            self.newJob_PushButton.setEnabled(True)
            self.refresh_PushButton.setEnabled(True)
            self.modification_PushButton.setEnabled(True)
            self.searchUndo_PushButton.setEnabled(True)
            self.search_PushButton.setEnabled(True)
            filter = "operator like '%{}%' or officer like '%{}%' or orderName like '%{}%'".format(usernametext,usernametext,usernametext)
            self.tablemodel.setFilter(filter)

    #@pyqtSlot()
    #查找功能
    def on_search_PushButton_clicked(self):
        #["工作名称", "工作类型", "工作状态","当前执行人","工作提出人"]
        searchtext = self.search_LineEdit.text()
        usernametext = self.username_Label.text()
        if searchtext and (usernametext != 'root' or usernametext != '肖惟'):
            print(1)
            if self.search_ComboBox.currentText() == "工作名称":
                queryjobName = "jobName like '%{}%' and (operator like '%{}%' or officer like '%{}%' or orderName like '%{}%')".format(searchtext,usernametext,usernametext,usernametext)
                self.tablemodel.setFilter(queryjobName)
                # 设置要过滤的当前过滤器。过滤器是不带关键字WHERE的SQL WHERE子句（例如，name =’Josephine’）。
            elif self.search_ComboBox.currentText() == "工作类型":
                queryjobType = "jobType like '%{}%' and (operator like '%{}%' or officer like '%{}%' or orderName like '%{}%')".format(searchtext,usernametext,usernametext,usernametext)
                self.tablemodel.setFilter(queryjobType)
            elif self.search_ComboBox.currentText() == "当前执行人":
                queryoperator = "operator like '%{}%' and (operator like '%{}%' or officer like '%{}%' or orderName like '%{}%')".format(searchtext,usernametext,usernametext,usernametext)
                self.tablemodel.setFilter(queryoperator)
            elif self.search_ComboBox.currentText() == "工作提出人":
                queryorder = "orderName like '%{}%' and (operator like '%{}%' or officer like '%{}%' or orderName like '%{}%')".format(searchtext,usernametext,usernametext,usernametext)
                self.tablemodel.setFilter(queryorder)
        elif searchtext and (usernametext == 'root' or usernametext == '肖惟'):
            print(2)
            if self.search_ComboBox.currentText() == "工作名称":
                queryjobName = "jobName like '%{}%'".format(searchtext)
                self.tablemodel.setFilter(queryjobName)
                # 设置要过滤的当前过滤器。过滤器是不带关键字WHERE的SQL WHERE子句（例如，name =’Josephine’）。
            elif self.search_ComboBox.currentText() == "工作类型":
                queryjobType = "jobType like '%{}%'".format(searchtext)
                self.tablemodel.setFilter(queryjobType)
            elif self.search_ComboBox.currentText() == "当前执行人":
                queryoperator = "operator like '%{}%'".format(searchtext)
                self.tablemodel.setFilter(queryoperator)
            elif self.search_ComboBox.currentText() == "工作提出人":
                queryorder = "orderName like '%{}%'".format(searchtext)
                self.tablemodel.setFilter(queryorder)
        else:
            print(3)
            self.setTableModel()
            self.setFilder()

    # 查找未完成需求功能
    def on_searchUndo_PushButton_clicked(self):
        #["工作名称", "工作类型", "工作状态","当前执行人","工作提出人"]
        searchtext = self.search_LineEdit.text()
        usernametext = self.username_Label.text()
        if searchtext and (usernametext != 'root' or usernametext != '肖惟'):
            if self.search_ComboBox.currentText() == "工作名称":
                queryjobName = "jobName like '%{}%' and jobStaus not like '已完成' and (operator like '%{}%' or officer like '%{}%' or orderName like '%{}%')".format(searchtext,usernametext,usernametext,usernametext)
                self.tablemodel.setFilter(queryjobName)
                # 设置要过滤的当前过滤器。过滤器是不带关键字WHERE的SQL WHERE子句（例如，name =’Josephine’）。
            elif self.search_ComboBox.currentText() == "工作类型":
                queryjobType = "jobType like '%{}%' and jobStaus not like '已完成' and (operator like '%{}%' or officer like '%{}%' or orderName like '%{}%')".format(searchtext,usernametext,usernametext,usernametext)
                self.tablemodel.setFilter(queryjobType)
            elif self.search_ComboBox.currentText() == "当前执行人":
                queryoperator = "operator like '%{}%' and jobStaus not like '已完成' and (operator like '%{}%' or officer like '%{}%' or orderName like '%{}%')".format(searchtext,usernametext,usernametext,usernametext)
                self.tablemodel.setFilter(queryoperator)
            elif self.search_ComboBox.currentText() == "工作提出人":
                queryorder = "orderName like '%{}%' and jobStaus not like '已完成' and (operator like '%{}%' or officer like '%{}%' or orderName like '%{}%')".format(searchtext,usernametext,usernametext,usernametext)
                self.tablemodel.setFilter(queryorder)
        elif searchtext and (usernametext == 'root' or usernametext == '肖惟'):
            if self.search_ComboBox.currentText() == "工作名称":
                queryjobName = "jobName like '%{}%' and jobStaus not like '已完成'".format(searchtext)
                self.tablemodel.setFilter(queryjobName)
                # 设置要过滤的当前过滤器。过滤器是不带关键字WHERE的SQL WHERE子句（例如，name =’Josephine’）。
            elif self.search_ComboBox.currentText() == "工作类型":
                queryjobType = "jobType like '%{}%' and jobStaus not like '已完成'".format(searchtext)
                self.tablemodel.setFilter(queryjobType)
            elif self.search_ComboBox.currentText() == "当前执行人":
                queryoperator = "operator like '%{}%' and jobStaus not like '已完成'".format(searchtext)
                self.tablemodel.setFilter(queryoperator)
            elif self.search_ComboBox.currentText() == "工作提出人":
                queryorder = "orderName like '%{}%' and jobStaus not like '已完成'".format(searchtext)
                self.tablemodel.setFilter(queryorder)
        else:
            queryjobName = "jobStaus not like '已完成'"
            self.tablemodel.setFilter(queryjobName)
            #self.setTableModel()
            #self.setFilder()

    #@pyqtSlot()
    #新增工作按钮
    def on_newJob_PushButton_clicked(self):
        jobinfo = NewJobWindow(self.db)
        r = jobinfo.exec_()
        if r > 0:
            if ftp_upload():
                QMessageBox.information(self, "新增工作已完成", "新增完成了哟！已经上传到服务器了哟！")
            else:
                QMessageBox.critical(self, "新增工作失败", "新增工作失败了哟！请重新刷新一下数据哟！")
            self.setTableModel()
            self.setFilder()

    # 刷新表格数据功能
    def on_refresh_PushButton_clicked(self):
        if database_download():
            self.db = QSqlDatabase.addDatabase("QSQLITE")
            self.db.setDatabaseName("./res/db/jobplaning.db")
            self.setTableModel()
            self.setFilder()
            self.status.showMessage('刷新完成了哟！', 5000)

    # 修改按钮
    def on_modification_PushButton_clicked(self):
        self.tablemodel.submitAll()
        if ftp_upload():
            QMessageBox.information(self, "修改已完成", "修改完成了哟！已经上传到服务器了哟！")
        else:
            QMessageBox.critical(self, "修改失败", "修改失败了哟！请重新刷新一下数据哟！")
        self.setTableModel()
        self.setFilder()

    #显示表格数据功能
    def setTableModel(self):
        """
        表格数据显示
        """
        self.tablemodel = MainWindowSqlTableModel()
        self.tableView_Left.setModel(self.tablemodel)
        # 设置要显示的视图的模型

        self.tablemodel.setEditStrategy(QSqlTableModel.OnManualSubmit)  # 所有变更立即更新到数据库中OnFieldChange、OnManualSubmit
        # 设置数据库中的值编辑策略，这里是更改即保存到数据库

        self.tablemodel.setTable("jobs")
        self.tablemodel.setSort(0, Qt.AscendingOrder)#排序，第0列，升序
        self.tablemodel.select()# 要使用表的数据填充模型，请调用select()

        # 设置表头内容
        self.tablemodel.setHeaderData(0, Qt.Horizontal, "优先级")
        self.tablemodel.setHeaderData(1, Qt.Horizontal, "工作名称")
        self.tablemodel.setHeaderData(2, Qt.Horizontal, "工作类型")
        self.tablemodel.setHeaderData(3, Qt.Horizontal, "数量")
        self.tablemodel.setHeaderData(4, Qt.Horizontal, "工作状态")
        self.tablemodel.setHeaderData(5, Qt.Horizontal, "工作紧急程度")
        self.tablemodel.setHeaderData(6, Qt.Horizontal, "排期完成时间")
        self.tablemodel.setHeaderData(7, Qt.Horizontal, "当前执行人")
        self.tablemodel.setHeaderData(8, Qt.Horizontal, "工作负责人")
        self.tablemodel.setHeaderData(9, Qt.Horizontal, "工作提出人")
        self.tablemodel.setHeaderData(10, Qt.Horizontal, "工作提出途径")
        self.tablemodel.setHeaderData(11, Qt.Horizontal, "工作发起时间")
        self.tablemodel.setHeaderData(12, Qt.Horizontal, "工作期望完成时间")
        self.tablemodel.setHeaderData(13, Qt.Horizontal, "工作实际完成时间")
        self.tablemodel.setHeaderData(14, Qt.Horizontal, "需求编码")
        self.tablemodel.setHeaderData(15, Qt.Horizontal, "工作进展")
        self.tablemodel.setHeaderData(16, Qt.Horizontal, "工单流水号")

        #设置列宽
        self.tableView_Left.setColumnWidth(0, 50)
        self.tableView_Left.setColumnWidth(1, 300)
        self.tableView_Left.setColumnWidth(2, 100)
        self.tableView_Left.setColumnWidth(3, 40)
        self.tableView_Left.setColumnWidth(4, 80)
        # self.tableView_Left.horizontalHeader().resizeSection(10, 80)  # 设置提出途径列的宽度
        # 隐藏不需要显示的数据
        # self.tableView.hideColumn(10)

    #关闭-提示
    def closeEvent(self, event):
        r = QMessageBox.warning(self, "退出", "确认要退出吗？修改都保存了吗？是否要最小化到托盘？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if r == QMessageBox.Yes:
            #os.system("taskkill /F /IM chromedriver.exe")
            event.accept()
        else:
            event.ignore()

    #右键菜单
    def contextMenuEvent(self, event):
        pmenu = QMenu(self)
        pOpenPathAct = QAction('打开文件夹', self.tableView_Left)
        pRTMSProcessAct = QAction('处理需求', self.tableView_Left)
        pRTMSCreateAct = QAction('新增需求', self.tableView_Left)
        pSendOrderAct = QAction('工作转派', self.tableView_Left)
        pCutAct = QAction('截屏', self.tableView_Left)
        pUploadZip = QAction('上传附件', self.tableView_Left)
        pDownloadZip = QAction('下载附件', self.tableView_Left)
        pDeleteAct = QAction('删除行', self.tableView_Left)
        pJobDoneAct = QAction('工作已完成', self.tableView_Left)
        if self.username_Label.text() != '您好啊':
            pmenu.addAction(pOpenPathAct)
            pmenu.addAction(pRTMSProcessAct)
            pmenu.addAction(pRTMSCreateAct)
            pmenu.addAction(pSendOrderAct)
            pmenu.addAction(pCutAct)
            pmenu.addAction(pUploadZip)
            pmenu.addAction(pDownloadZip)
            pmenu.addAction(pJobDoneAct)
        if self.username_Label.text() == 'root':
            pmenu.addAction(pDeleteAct)
        pmenu.popup(self.mapToGlobal(event.pos()))
        pOpenPathAct.triggered.connect(self.OpenPath)
        pRTMSProcessAct.triggered.connect(self.RTMSProcess)
        pRTMSCreateAct.triggered.connect(self.RTMSCreate)
        pSendOrderAct.triggered.connect(self.SendOrder)
        pCutAct.triggered.connect(self.Cut)
        pUploadZip.triggered.connect(self.UploadZip)
        pDownloadZip.triggered.connect(self.DownloadZip)
        pDeleteAct.triggered.connect(self.deleterows)
        pJobDoneAct.triggered.connect(self.JobDone)

    # 右键菜单-删除行用到的filter
    def filter(self, selectedIndexes):
        """
        过滤出选择的行
        """
        filtered = []
        for s in selectedIndexes:
            filtered.append(s.row())
        return list(set(filtered))
        # 根据返回的索引列表，去重一下，取得相应的行号。

    #右键菜单-删除行
    def deleterows(self):
        passwd, okPressed = QInputDialog.getText(self, "请输入安全码","安全码：", QLineEdit.Password, "")
        if okPressed and passwd =='Xww111!!!':
            selectedIndexes = self.tableView_Left.selectedIndexes()
            # 返回所有选定模型项索引的列表。
            selectedRows = self.filter(selectedIndexes)
            for row in reversed(selectedRows):
                print(row)
                self.tablemodel.removeRow(row)
                # 倒序删除
            self.tablemodel.submitAll()
            self.tablemodel.select()
            if ftp_upload():
                QMessageBox.information(self, "删除完成", "删除完成了哟！")
            else:
                QMessageBox.critical(self, "删除失败", "删除失败了哟！")

    #右键菜单-需求处理
    def RTMSProcess(self):
        selectedIndexes = self.tableView_Left.selectedIndexes()
        selectedRows = self.filter(selectedIndexes)
        if len(selectedRows)!= 1:
            QMessageBox.information(self, "选多了", "复选的时候无法进行需求系统的操作哟！")
        elif len(selectedRows)== 1:
            row = selectedRows[0]
            #获取当前需求的需求编号和需求名
            RTMScode = str(self.tablemodel.record(row).value("RTMScode"))
            jobName = str(self.tablemodel.record(row).value("jobName"))
            #获取当前用户的需求管理系统的用户名密码
            RTMSInfo = getRTMSUserInfo(self.username_Label.text())
            RTMSUsername = RTMSInfo[0]
            RTMSPassword = RTMSInfo[1]
            r = QMessageBox.warning(self, "提示", "此操作可能会引起系统异常，请慎重使用！", QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.Yes)
            if r == QMessageBox.Yes:
                #创建浏览器对象，并调用查询方法
                self.browser = webdriver.Chrome()
                searchRequest(self.browser, RTMSUsername, RTMSPassword, RTMScode, jobName)

    # 右键菜单-新增需求
    def RTMSCreate(self):
        selectedIndexes = self.tableView_Left.selectedIndexes()
        selectedRows = self.filter(selectedIndexes)
        if len(selectedRows) != 1:
            QMessageBox.information(self, "选多了", "复选的时候无法进行需求系统的操作哟！")
        elif len(selectedRows) == 1:
            row = selectedRows[0]
            # 获取当前需求的需求编号和需求名
            jobProgress = str(self.tablemodel.record(row).value("jobProgress"))
            jobName = str(self.tablemodel.record(row).value("jobName"))
            RTMScode = str(self.tablemodel.record(row).value("RTMScode"))
            # 获取当前用户的需求管理系统的用户名密码
            RTMSInfo = getRTMSUserInfo(self.username_Label.text())
            RTMSUsername = RTMSInfo[0]
            RTMSPassword = RTMSInfo[1]
            #print(RTMSUsername, RTMSPassword, jobName, jobProgress)
            if RTMScode =='待补充':
                QMessageBox.information(self, "提示", "此操作可能会引起系统异常，请慎重使用！")
                # 创建浏览器对象，并调用查询方法
                self.browser = webdriver.Chrome()
                createRequest(self.browser, RTMSUsername, RTMSPassword, jobName, jobProgress)
            else:
                r = QMessageBox.warning(self, "提示", "需求可能已存在，确认要继续新增吗？", QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.Yes)
                if r == QMessageBox.Yes:
                    QMessageBox.information(self, "提示", "此操作可能会引起系统异常，请慎重使用！")
                    self.browser = webdriver.Chrome()
                    createRequest(self.browser, RTMSUsername, RTMSPassword, jobName, jobProgress)
                else:
                    return

    #右键菜单-派单
    def SendOrder(self):
        selectedIndexes = self.tableView_Left.selectedIndexes()
        selectedRows = self.filter(selectedIndexes)
        # 定义一个登录框的对象
        sendorder = SendOrderWindow(self.db)
        # 在主窗口中连接信号和槽，把登录框的信号连接到MainWindow的username_Label上
        sendorder.mySignal.connect(self.getSendOrderSignal)
        # 激活登录窗口
        r = sendorder.exec_()
        if r > 0:
            for row in reversed(selectedRows):
                record = self.tablemodel.record(row)
                record.setValue("operator", self.operatorName)
                #记录日志
                record.setValue("jobProgress", str(record.value("jobProgress"))+'\n'+time.strftime("%Y/%m/%d", time.localtime())+'->由'+self.username_Label.text()+'转派给'+self.operatorName)
                self.tablemodel.setRecord(row, record)
                self.tablemodel.submitAll()
    def getSendOrderSignal(self, connect):
        self.operatorName = connect

    #右键菜单-工作已完成
    def JobDone(self):
        selectedIndexes = self.tableView_Left.selectedIndexes()
        selectedRows = self.filter(selectedIndexes)
        for row in reversed(selectedRows):
            record = self.tablemodel.record(row)
            record.setValue("priority","99")
            record.setValue("realFinishDate",str(time.strftime("%Y/%m/%d", time.localtime())))
            record.setValue("jobStaus","已完成")
            self.status.showMessage('工作<'+str(record.value("jobName"))+'>已完成！辛苦啦！', 5000)  # 5秒后消失
            self.tablemodel.setRecord(row, record)
            self.tablemodel.submitAll()
            #self.tablemodel.select()

    #右键菜单-打开文件夹
    def OpenPath(self):
        selectedIndexes = self.tableView_Left.selectedIndexes()
        selectedRows = self.filter(selectedIndexes)
        for row in reversed(selectedRows):
            JobName = str(self.tablemodel.record(row).value("jobName"))
            OrderName = str(self.tablemodel.record(row).value("orderName"))
            DataList = str(self.tablemodel.record(row).value("startDate")).split("/")
            Path = 'D:\\@\\work\\' + DataList[0] + '年\\' + DataList[1] + '月\\' + OrderName + '-' + JobName
            if not os.path.exists(Path):
                reply = QMessageBox.information(self, "没找到哟", "文件夹<" + Path + ">不存在，是否创建？", QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    os.makedirs(Path)
            if os.path.exists(Path):
                OpenFolder(Path)

    #右键菜单-截屏
    def Cut(self):
        print(11)
        selectedIndexes = self.tableView_Left.selectedIndexes()
        selectedRows = self.filter(selectedIndexes)
        print(selectedRows)
        if len(selectedRows)!= 1:
            QMessageBox.information(self, "选多了", "复选的时候无法进行截屏操作哟！要不然就不知道截图文件应该保存在哪了呢！")
        elif len(selectedRows)== 1:
            row = selectedRows[0]
            JobName = str(self.tablemodel.record(row).value("jobName")).replace(' ','')
            OrderName = str(self.tablemodel.record(row).value("orderName")).replace(' ','')
            DataList = str(self.tablemodel.record(row).value("startDate")).split("/")
            Path = 'D:\\@\\work\\' + DataList[0] + '年\\' + DataList[1] + '月\\' + OrderName + '-' + JobName
            FileName = Path + '\\' + '截屏' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.BMP'
            print(row)
            print(Path)
            print(FileName)
            Cut(FileName)  # 调用截图方法
            QMessageBox.information(self, "截图完成", "截图完成！已经保存到文件夹<" + Path + ">里啦！辛苦啦！这样就不会忘记了哟！")

    #右键菜单-上传附件
    def UploadZip(self):
        selectedIndexes = self.tableView_Left.selectedIndexes()
        selectedRows = self.filter(selectedIndexes)
        for row in reversed(selectedRows):
            JobName = str(self.tablemodel.record(row).value("jobName"))
            OrderName = str(self.tablemodel.record(row).value("orderName"))
            DataList = str(self.tablemodel.record(row).value("startDate")).split("/")
            Path = 'D:\\@\\work\\' + DataList[0] + '年\\' + DataList[1] + '月\\' + OrderName + '-' + JobName
            #output_filename为生成的压缩包的名，也是上传到服务器的文件名，此处使用工单流水号字段
            output_filename = str(self.tablemodel.record(row).value("jobID")) + '.zip'
            # 判断文件夹是否存在，如果不存在则提示无法压缩，如果存在则遍历文件夹并且压缩到一个名为文件夹名的压缩包中
            if not os.path.exists(Path):
                QMessageBox.information(self, "文件夹未找到", "没找到相关文件哟！所以就无法上传附件了哟！可是试试先创建文件夹哟！")
            elif os.path.exists(Path):
                res = uploadzip(Path, output_filename)
                if res:
                    QMessageBox.information(self, "上传成功", "文件<" + OrderName + '-' + JobName + ">上传成功了哟！")
                else:
                    QMessageBox.information(self, "上传失败", "文件<" + OrderName + '-' + JobName + ">上传失败了哟！")

    #右键菜单-下载附件
    def DownloadZip(self):
        selectedIndexes = self.tableView_Left.selectedIndexes()
        selectedRows = self.filter(selectedIndexes)
        save_path = QFileDialog.getExistingDirectory()
        for row in reversed(selectedRows):
            JobName = str(self.tablemodel.record(row).value("jobName"))
            OrderName = str(self.tablemodel.record(row).value("orderName"))
            # 获取要下载的文件名
            fileName = str(self.tablemodel.record(row).value("jobID")) + '.zip'
            # 选择压缩文件保存的位置
            # 获取下载到本地的文件名
            download_fileName = save_path + '/' + OrderName + '-' + JobName + '.zip'
            res = ftp_downloadzip(fileName, download_fileName)
            if res:
                QMessageBox.information(self, "下载成功", "文件<" + OrderName + '-' + JobName + ">下载成功了哟！")
            else:
                QMessageBox.information(self, "下载失败", "文件<" + OrderName + '-' + JobName + ">下载失败了哟！")

