# -*- coding: utf-8 -*-
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 400)
        Dialog.setWindowIcon(QIcon('./res/LOGO.ico'))#设置窗口图标
        Dialog.setWindowTitle("新增")#设置窗口主题

        # 定义保存按钮控件
        self.pushButton_ok = QPushButton('')
        self.pushButton_ok.setObjectName('pushButton_ok')
        self.pushButton_cancel = QPushButton('')
        self.pushButton_cancel.setObjectName('pushButton_cancel')

        # 定义说明标签系列控件
        # ********如修改字段，此处需修改，注意：此处修改的是每个字段的说明标签，不需要与字段数对应********
        # 优先级
        # 只能输入1-99整数
        self.priority_Label = QLabel('优先级')
        self.priority_LineEdit = QLineEdit('1')
        pIntValidator = QIntValidator(Dialog)
        pIntValidator.setRange(1, 99)
        self.priority_LineEdit.setValidator(pIntValidator)
        #工作名称
        self.jobName_Label = QLabel('工作名称')
        self.jobName_LineEdit = QLineEdit()
        #工作类型
        self.jobType_Label = QLabel('工作类型')
        self.jobType_LineEdit = QComboBox()
        self.jobType_LineEdit.addItem(QIcon("./res/jobtype/1.png"), "数据接入")
        self.jobType_LineEdit.addItem(QIcon("./res/jobtype/2.png"), "数据导出")
        self.jobType_LineEdit.addItem(QIcon("./res/jobtype/3.png"), "权限变更")
        self.jobType_LineEdit.addItem(QIcon("./res/jobtype/4.png"), "故障处理")
        self.jobType_LineEdit.addItem(QIcon("./res/jobtype/5.png"), "租户创建")
        self.jobType_LineEdit.addItem(QIcon("./res/jobtype/6.png"), "数据提取")
        self.jobType_LineEdit.addItem(QIcon("./res/jobtype/7.png"), "材料编写")
        self.jobType_LineEdit.addItem(QIcon("./res/jobtype/8.png"), "MPP故障处理")
        self.jobType_LineEdit.addItem(QIcon("./res/jobtype/8.png"), "其它")
        #工作数量
        self.jobCount_Label = QLabel('工作数量')
        self.jobCount_LineEdit = QLineEdit('1')
        pIntValidator = QIntValidator(Dialog)
        pIntValidator.setRange(1, 999)
        self.jobCount_LineEdit.setValidator(pIntValidator)
        #工作状态
        self.jobStaus_Label = QLabel('工作状态')
        self.jobStaus_LineEdit = QComboBox()
        self.jobStaus_LineEdit.addItem(QIcon("./res/jobstaus/1.png"), "排期中")
        self.jobStaus_LineEdit.addItem(QIcon("./res/jobstaus/2.png"), "进行中")
        self.jobStaus_LineEdit.addItem(QIcon("./res/jobstaus/3.png"), "待评估")
        #工作紧急程度
        self.jobEmergencyLevel_Label = QLabel('工作紧急程度')
        self.jobEmergencyLevel_LineEdit = QComboBox()
        self.jobEmergencyLevel_LineEdit.addItem(QIcon("./res/jobemergencylevel/1.png"), "普通需求")
        self.jobEmergencyLevel_LineEdit.addItem(QIcon("./res/jobemergencylevel/2.png"), "紧急需求")
        self.jobEmergencyLevel_LineEdit.addItem(QIcon("./res/jobemergencylevel/3.png"), "特殊通道")
        #排期完成时间
        self.planingFinishDate_Label = QLabel('排期完成时间')
        self.planingFinishDate_LineEdit = QDateTimeEdit(QDateTime.currentDateTime())
        self.planingFinishDate_LineEdit.setCalendarPopup(True)
        self.planingFinishDate_LineEdit.setDisplayFormat('yyyy/MM/dd')
        #self.planingFinishDate_LineEdit = QLineEdit('2099/12/12')
        #当前执行人
        self.operator_Label = QLabel('当前执行人')
        self.operator_LineEdit = QLineEdit()
        #工作负责人
        self.officer_Label = QLabel('工作负责人')
        self.officer_LineEdit = QLineEdit()
        #工作提出人
        self.order_Label = QLabel('工作提出人')
        self.order_LineEdit = QLineEdit()
        #工作提出途径
        self.orderWay_Label = QLabel('工作提出途径')
        self.orderWay_LineEdit = QComboBox()
        self.orderWay_LineEdit.addItem(QIcon("./res/orderway/1.png"), "公务")
        self.orderWay_LineEdit.addItem(QIcon("./res/orderway/2.png"), "需求管理系统")
        self.orderWay_LineEdit.addItem(QIcon("./res/orderway/3.png"), "邮件")
        self.orderWay_LineEdit.addItem(QIcon("./res/orderway/4.png"), "电话")
        #工作发起时间
        self.startDate_Label = QLabel('工作发起时间')
        self.startDate_LineEdit = QLineEdit(time.strftime("%Y/%m/%d", time.localtime()))
        self.startDate_LineEdit.setEnabled(False)
        #工作期望完成时间
        self.hopeFinshDate_Label = QLabel('工作期望完成时间')
        self.hopeFinshDate_LineEdit = QDateTimeEdit(QDateTime.currentDateTime())
        self.hopeFinshDate_LineEdit.setCalendarPopup(True)
        self.hopeFinshDate_LineEdit.setDisplayFormat('yyyy/MM/dd')
        #self.hopeFinshDate_LineEdit = QLineEdit(time.strftime('2099/12/12'))
        #工作实际完成时间
        self.realFinishDate_Label = QLabel('工作实际完成时间')
        self.realFinishDate_LineEdit = QLineEdit()
        self.realFinishDate_LineEdit.setEnabled(False)
        #需求编码
        self.RTMScode_Label = QLabel('需求编码')
        self.RTMScode_LineEdit = QLineEdit('待补充')
        #工作进展
        self.jobProgress_Label = QLabel('工作进展')
        self.jobProgress_TextEdit = QTextEdit()
        #工单流水号
        self.jobID_Label = QLabel('工单流水号')
        self.jobID_LineEdit = QLineEdit(time.strftime("%Y%m%d%H%M%S", time.localtime()))
        self.jobID_LineEdit.setEnabled(False)

        self.CreatePath = QCheckBox('创建文件夹')
        self.GrabScreen = QCheckBox('截图并保存')


        # 将表单的各个控件放入Line_Layout表格布局
        # ********如修改字段，此处需修改，注意：需要与字段数一致********
        Line_Layout = QGridLayout()
        Line_Layout.setSpacing(10)
        Line_Layout.addWidget(self.priority_Label, 0, 0)
        Line_Layout.addWidget(self.priority_LineEdit, 0, 1)
        Line_Layout.addWidget(self.jobType_Label, 0, 2)
        Line_Layout.addWidget(self.jobType_LineEdit, 0, 3)
        Line_Layout.addWidget(self.jobCount_Label, 0, 4)
        Line_Layout.addWidget(self.jobCount_LineEdit, 0, 5)

        Line_Layout.addWidget(self.jobName_Label, 1, 0)
        Line_Layout.addWidget(self.jobName_LineEdit, 1, 1, 1, 3)
        Line_Layout.addWidget(self.jobID_Label, 1, 4)
        Line_Layout.addWidget(self.jobID_LineEdit, 1, 5)

        Line_Layout.addWidget(self.jobStaus_Label, 2, 0)
        Line_Layout.addWidget(self.jobStaus_LineEdit, 2, 1)
        Line_Layout.addWidget(self.jobEmergencyLevel_Label, 2, 2)
        Line_Layout.addWidget(self.jobEmergencyLevel_LineEdit, 2, 3)
        Line_Layout.addWidget(self.planingFinishDate_Label, 2, 4)
        Line_Layout.addWidget(self.planingFinishDate_LineEdit, 2, 5)

        Line_Layout.addWidget(self.operator_Label, 3, 0)
        Line_Layout.addWidget(self.operator_LineEdit, 3, 1)
        Line_Layout.addWidget(self.officer_Label, 3, 2)
        Line_Layout.addWidget(self.officer_LineEdit, 3, 3)
        Line_Layout.addWidget(self.order_Label, 3, 4)
        Line_Layout.addWidget(self.order_LineEdit, 3, 5)

        Line_Layout.addWidget(self.orderWay_Label, 4, 0)
        Line_Layout.addWidget(self.orderWay_LineEdit, 4, 1)
        Line_Layout.addWidget(self.RTMScode_Label, 4, 2)
        Line_Layout.addWidget(self.RTMScode_LineEdit, 4, 3)
        Line_Layout.addWidget(self.CreatePath, 4, 4)
        Line_Layout.addWidget(self.GrabScreen, 4, 5)

        Line_Layout.addWidget(self.startDate_Label, 5, 0)
        Line_Layout.addWidget(self.startDate_LineEdit, 5, 1)
        Line_Layout.addWidget(self.hopeFinshDate_Label, 5, 2)
        Line_Layout.addWidget(self.hopeFinshDate_LineEdit, 5, 3)
        Line_Layout.addWidget(self.realFinishDate_Label, 5, 4)
        Line_Layout.addWidget(self.realFinishDate_LineEdit, 5, 5)

        Line_Layout.addWidget(self.jobProgress_Label, 6, 0)
        Line_Layout.addWidget(self.jobProgress_TextEdit, 6, 1, 1, 5)

        # 定义一个承载表单控件的子窗体
        Line_Widget = QWidget()
        # 用Line_Widget承载Line_Layout布局
        Line_Widget.setLayout(Line_Layout)

        # 定义一个承载按钮控件的布局
        PushButton_Layout = QHBoxLayout()
        PushButton_Layout.addStretch()
        PushButton_Layout.addWidget(self.pushButton_ok)
        PushButton_Layout.addStretch()
        PushButton_Layout.addWidget(self.pushButton_cancel)
        PushButton_Layout.addStretch()

        # 定义一个List_Layout垂直布局做完整体布局
        List_Layout = QVBoxLayout()
        # 将表单的子窗体控件和保存按钮控件放入List_Layout垂直布局
        List_Layout.addWidget(Line_Widget)
        List_Layout.addStretch()
        List_Layout.addLayout(PushButton_Layout)
        Dialog.setLayout(List_Layout)


        self.pushButton_ok.clicked.connect(Dialog.accept)
        self.pushButton_cancel.clicked.connect(Dialog.reject)
        QMetaObject.connectSlotsByName(Dialog)
        # 调用QSS样式文件
        with open('./res/QSS/NewJobWindow_style1.qss', 'r', encoding='utf-8') as f:
            Dialog.setStyleSheet(f.read())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

