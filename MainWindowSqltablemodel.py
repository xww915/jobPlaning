# -*- coding: utf-8 -*-

from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt, QVariant
from PyQt5.QtGui import QIcon

class MainWindowSqlTableModel(QSqlTableModel):
    '''
    数据模型
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()

    def data(self, index, role):
        '''
        在模型索引存在的情况下，我们表格中数据排列是垂直、水平居中；
        同时在指定列的数据中，需要返回一个图标。这个图标是根据指定列数据来选择的。
        其他情况使用父类QSqlTableModel的默认数据。
        '''
        if index.isValid():
            if role == Qt.TextAlignmentRole:
                return QVariant(Qt.AlignHCenter | Qt.AlignVCenter)
            if role == Qt.DecorationRole and index.column() == 2:
                jobType = index.data()
                IconPath = self.getJobTypeIco(jobType)
                return QVariant(IconPath)
            if role == Qt.DecorationRole and index.column() == 4:
                jobStaus = index.data()
                IconPath = self.getJobStausIco(jobStaus)
                return QVariant(IconPath)
            if role == Qt.DecorationRole and index.column() == 5:
                jobEmergencyLevel = index.data()
                IconPath = self.getjobEmergencyLevelIco(jobEmergencyLevel)
                return QVariant(IconPath)
            if role == Qt.DecorationRole and index.column() == 10:
                orderWay = index.data()
                IconPath = self.getorderWayIco(orderWay)
                return QVariant(IconPath)
            else:
                return super().data(index, role)

    def getJobTypeIco(self, jobType):
        '''
        根据需求类型名称返回对应的图标
        '''
        if jobType == "数据接入":
            jobTypeIcon = QIcon("./res/jobtype/1.png")
        elif jobType == "数据导出":
            jobTypeIcon = QIcon("./res/jobtype/2.png")
        elif jobType == "权限变更":
            jobTypeIcon = QIcon("./res/jobtype/3.png")
        elif jobType == "故障处理":
            jobTypeIcon = QIcon("./res/jobtype/4.png")
        elif jobType == "租户创建":
            jobTypeIcon = QIcon("./res/jobtype/5.png")
        elif jobType == "数据提取":
            jobTypeIcon = QIcon("./res/jobtype/6.png")
        elif jobType == "材料编写":
            jobTypeIcon = QIcon("./res/jobtype/7.png")
        elif jobType == "MPP故障处理":
            jobTypeIcon = QIcon("./res/jobtype/8.png")
        elif jobType == "其它":
            jobTypeIcon = QIcon("./res/jobtype/8.png")
        else:
            jobTypeIcon = QIcon("./res/jobtype/8.png")
        return jobTypeIcon

    def getJobStausIco(self, jobStaus):
        '''
        根据需求类型名称返回对应的图标
        '''
        if jobStaus == "排期中":
            jobStausIcon = QIcon("./res/jobstaus/1.png")
        elif jobStaus == "进行中":
            jobStausIcon = QIcon("./res/jobstaus/2.png")
        elif jobStaus == "待评估":
            jobStausIcon = QIcon("./res/jobstaus/3.png")
        elif jobStaus == "已完成":
            jobStausIcon = QIcon("./res/jobstaus/4.png")
        else:
            jobStausIcon = QIcon("./res/jobstaus/4.png")
        return jobStausIcon

    def getjobEmergencyLevelIco(self, jobEmergencyLevel):
        '''
        根据需求类型名称返回对应的图标
        '''
        if jobEmergencyLevel == "普通需求":
            jobEmergencyLevelIcon = QIcon("./res/jobemergencylevel/1.png")
        elif jobEmergencyLevel == "紧急需求":
            jobEmergencyLevelIcon = QIcon("./res/jobemergencylevel/2.png")
        elif jobEmergencyLevel == "特殊通道":
            jobEmergencyLevelIcon = QIcon("./res/jobemergencylevel/3.png")
        else:
            jobEmergencyLevelIcon = QIcon("./res/jobemergencylevel/3.png")
        return jobEmergencyLevelIcon

    def getorderWayIco(self, orderWay):
        '''
        根据需求类型名称返回对应的图标
        '''
        if orderWay == "公务":
            orderWayIcon = QIcon("./res/orderway/1.png")
        elif orderWay == "需求管理系统":
            orderWayIcon = QIcon("./res/orderway/2.png")
        elif orderWay == "邮件":
            orderWayIcon = QIcon("./res/orderway/3.png")
        elif orderWay == "电话":
            orderWayIcon = QIcon("./res/orderway/4.png")
        else:
            orderWayIcon = QIcon("./res/orderway/1.png")
        return orderWayIcon
