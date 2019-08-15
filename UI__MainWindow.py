# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_MainWindow(object):
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1256, 570)#初始化大小
        MainWindow.setWindowIcon(QIcon('./res/LOGO.ico'))#设置窗口图标
        MainWindow.setWindowTitle("欢迎使用")#设置窗口主题
        #MainWindow.setStyleSheet("QWidget{background: rgb(255, 255, 255);}")
        palette1 = QPalette()
        palette1.setColor(palette1.Background, QColor(255, 255, 255))
        MainWindow.setPalette(palette1)

        #定义MainWindow的中心窗口
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        #左侧-用户名
        self.username_Label = QLabel('您好啊')
        self.username_Label.setObjectName("username_Label")
        #左侧-欢迎词
        self.welcom_Label = QLabel(',欢迎使用！')
        self.welcom_Label.setObjectName("welcom_Label")
        #左侧-待办需求数量
        self.RTMS_Label = QLabel('需求管理系统待办：')
        self.RTMS_Label.setObjectName("RTMS_Label")
        #左侧-登录按钮
        self.login_PushButton = QPushButton('切换用户')
        self.login_PushButton.setObjectName("login_PushButton")
        self.login_PushButton.setStatusTip("点击登录按钮进行用户切换")
        #左侧-顶部布局1
        self.leftTop_Layout1 = QHBoxLayout()
        self.leftTop_Layout1.setObjectName("leftTop_Layout1")
        self.leftTop_Layout1.addWidget(self.username_Label)
        self.leftTop_Layout1.addWidget(self.welcom_Label)
        self.leftTop_Layout1.addStretch()
        self.leftTop_Layout1.addWidget(self.login_PushButton)
        self.leftTop_Layout1.addWidget(self.RTMS_Label)
        # 左侧-顶部窗体1
        self.leftTop_Widget1 = QWidget()
        self.leftTop_Widget1.setObjectName("leftTop_Widget1")
        self.leftTop_Widget1.setLayout(self.leftTop_Layout1)

        #左侧-搜索框
        self.search_LineEdit = QLineEdit()
        self.search_LineEdit.setClearButtonEnabled(True)
        self.search_LineEdit.setFocusPolicy(Qt.ClickFocus)
        self.search_LineEdit.setObjectName("search_LineEdit")
        self.search_LineEdit.setStatusTip("输入需要搜索的关键字")
        #左侧-搜索下拉框
        self.search_ComboBox = QComboBox()
        self.search_ComboBox.setFocusPolicy(Qt.ClickFocus)
        self.search_ComboBox.setObjectName("search_ComboBox")
        self.search_ComboBox.setStatusTip("选择关键字所在类别")
        #为下拉框定义一个ListView，用以加载样式
        self.search_ListView = QListView()
        self.search_ComboBox.setView(self.search_ListView)
        #self.search_ComboBox.setStyleSheet(" QComboBox:drop-down{background-color:red}")
        #左侧-搜索按钮
        self.search_PushButton = QPushButton('')
        self.search_PushButton.setObjectName("search_PushButton")
        self.search_PushButton.setStatusTip("点击搜索按钮进行搜索")
        #左侧-搜索未完成需求按钮
        self.searchUndo_PushButton = QPushButton('')
        self.searchUndo_PushButton.setObjectName("searchUndo_PushButton")
        self.searchUndo_PushButton.setStatusTip("点击搜索按钮搜索未完成需求")
        #左侧-顶部布局2
        self.leftTop_Layout2 = QHBoxLayout()
        self.leftTop_Layout2.setObjectName("leftTop_Layout")
        self.leftTop_Layout2.addWidget(self.search_LineEdit)
        self.leftTop_Layout2.addWidget(self.search_ComboBox)
        self.leftTop_Layout2.addWidget(self.search_PushButton)
        self.leftTop_Layout2.addWidget(self.searchUndo_PushButton)

        #左侧-新增按钮
        self.newJob_PushButton = QPushButton('')
        #self.newJob_PushButton.setFixedSize(78px,24px)
        self.newJob_PushButton.setObjectName("newJob_PushButton")
        self.newJob_PushButton.setStatusTip("点击新增按钮来创建新工作")
        #左侧-刷新按钮
        self.refresh_PushButton = QPushButton('')
        self.refresh_PushButton.setObjectName("refresh_PushButton")
        self.refresh_PushButton.setStatusTip("点击刷新按钮刷新数据")
        #左侧-修改按钮
        self.modification_PushButton = QPushButton('')
        self.modification_PushButton.setObjectName("modification_PushButton")
        self.modification_PushButton.setStatusTip("点击修改按钮保存修改的数据")
        #左侧-顶部布局3
        self.leftTop_Layout3 = QHBoxLayout()
        self.leftTop_Layout3.setObjectName("leftTop_Layout2")
        self.leftTop_Layout3.addWidget(self.newJob_PushButton)
        self.leftTop_Layout3.addWidget(self.refresh_PushButton)
        self.leftTop_Layout3.addWidget(self.modification_PushButton)
        self.leftTop_Layout3.addStretch()

        #左侧-数据展示表格
        self.tableView_Left = QTableView()
        self.tableView_Left.setObjectName("tableViewLeft")
        self.tableView_Left.setStatusTip("双击表格修改数据，菜单选项请点击右键")
        #左侧-布局
        self.left_Layout = QVBoxLayout()
        self.left_Layout.setObjectName("left_Layout")
        self.left_Layout.addWidget(self.leftTop_Widget1)
        self.left_Layout.addLayout(self.leftTop_Layout2)
        self.left_Layout.addLayout(self.leftTop_Layout3)
        self.left_Layout.addWidget(self.tableView_Left)
        self.left_Layout.setContentsMargins(5, 5, 0, 0)#设置左侧、顶部、右侧和底部边距，以便在布局周围使用。
        #左侧-窗体控件用来承载左侧布局
        self.left_Widget = QWidget()
        self.left_Widget.setLayout(self.left_Layout)

        #右侧-优先级
        self.priority_Label = QLabel('优先级：')
        self.priority_LineEdit = QLineEdit()
        self.priority_LineEdit.setFixedWidth(60)
        #self.priority_LineEdit.setEnabled(False)
        # 右侧-需求名称
        self.jobName_Label = QLabel('工作名称：')
        self.jobName_LineEdit = QLineEdit()
        # 右侧-工作类型
        self.jobType_Label = QLabel('工作类型：')
        self.jobType_LineEdit = QLineEdit()
        # 右侧-工作数量
        self.jobCount_Label = QLabel('工作数量：')
        self.jobCount_LineEdit = QLineEdit()
        # 右侧-工作状态
        self.jobStaus_Label = QLabel('工作状态：')
        self.jobStaus_LineEdit = QLineEdit()
        # 右侧-工作紧急程度
        self.jobEmergencyLevel_Label = QLabel('工作紧急程度：')
        self.jobEmergencyLevel_LineEdit = QLineEdit()
        # 右侧-排期完成时间
        self.planingFinishDate_Label = QLabel('排期完成时间：')
        self.planingFinishDate_LineEdit = QLineEdit()
        # 右侧-当前执行人
        self.operator_Label = QLabel('当前执行人：')
        self.operator_LineEdit = QLineEdit()
        # 右侧-工作负责人
        self.officer_Label = QLabel('工作负责人：')
        self.officer_LineEdit = QLineEdit()
        # 右侧-工作提出人
        self.order_Label = QLabel('工作提出人：')
        self.order_LineEdit = QLineEdit()
        self.order_LineEdit.setFixedWidth(60)
        # 右侧-工作提出途径
        self.orderWay_Label = QLabel('工作提出途径：')
        self.orderWay_LineEdit = QLineEdit()
        self.orderWay_LineEdit.setFixedWidth(60)
        # 右侧-工作发起时间
        self.startDate_Label = QLabel('工作发起时间：')
        self.startDate_LineEdit = QLineEdit()
        # 右侧-工作期望完成时间
        self.hopeFinshDate_Label = QLabel('工作期望完成时间：')
        self.hopeFinshDate_LineEdit = QLineEdit()
        # 右侧-工作实际完成时间
        self.realFinishDate_Label = QLabel('工作实际完成时间：')
        self.realFinishDate_LineEdit = QLineEdit()
        # 右侧-需求编码
        self.RTMScode_Label = QLabel('需求编码：')
        self.RTMScode_LineEdit = QLineEdit()
        # 右侧-工作进展
        self.jobProgress_Label = QLabel('工作进展：')
        self.jobProgress_TextEdit = QTextEdit()
        # 右侧-工作进展修改按钮
        self.jobProgress_PushButton = QPushButton('修改')
        self.jobProgress_PushButton.setObjectName("jobProgress_PushButton")
        self.jobProgress_PushButton.setStatusTip("点击修改按钮更新数据")
        # 右侧-工单流水号
        self.jobID_Label = QLabel('工单流水号：')
        self.jobID_LineEdit = QLineEdit()

        #右侧详细信息布局
        self.right_Layout = QGridLayout()
        self.right_Layout.setSpacing(15)
        self.right_Layout.setContentsMargins(20,40,20,40)
        self.right_Layout.addWidget(self.jobName_Label,0,0)
        self.right_Layout.addWidget(self.jobName_LineEdit,0,1,1,7)

        self.right_Layout.addWidget(self.priority_Label,1,0)
        self.right_Layout.addWidget(self.priority_LineEdit,1,1)
        self.right_Layout.addWidget(self.jobID_Label,1,2)
        self.right_Layout.addWidget(self.jobID_LineEdit,1,3,1,2)

        self.right_Layout.addWidget(self.jobStaus_Label,2,0)
        self.right_Layout.addWidget(self.jobStaus_LineEdit,2,1)
        self.right_Layout.addWidget(self.jobEmergencyLevel_Label,2,2)
        self.right_Layout.addWidget(self.jobEmergencyLevel_LineEdit,2,3)
        self.right_Layout.addWidget(self.RTMScode_Label,2,4)
        self.right_Layout.addWidget(self.RTMScode_LineEdit,2,5,1,2)

        self.right_Layout.addWidget(self.jobType_Label,3,0)
        self.right_Layout.addWidget(self.jobType_LineEdit,3,1,1,2)
        self.right_Layout.addWidget(self.jobCount_Label,3,4)
        self.right_Layout.addWidget(self.jobCount_LineEdit,3,5)

        self.right_Layout.addWidget(self.operator_Label,4,0)
        self.right_Layout.addWidget(self.operator_LineEdit,4,1)
        self.right_Layout.addWidget(self.officer_Label,4,2)
        self.right_Layout.addWidget(self.officer_LineEdit,4,3)
        self.right_Layout.addWidget(self.order_Label,4,4)
        self.right_Layout.addWidget(self.order_LineEdit,4,5)
        self.right_Layout.addWidget(self.orderWay_Label,4,6)
        self.right_Layout.addWidget(self.orderWay_LineEdit,4,7)

        self.right_Layout.addWidget(self.planingFinishDate_Label,5,0)
        self.right_Layout.addWidget(self.planingFinishDate_LineEdit,5,1,1,2)
        self.right_Layout.addWidget(self.realFinishDate_Label,5,3)
        self.right_Layout.addWidget(self.realFinishDate_LineEdit,5,4,1,2)

        self.right_Layout.addWidget(self.startDate_Label,6,0)
        self.right_Layout.addWidget(self.startDate_LineEdit,6,1,1,2)
        self.right_Layout.addWidget(self.hopeFinshDate_Label,6,3)
        self.right_Layout.addWidget(self.hopeFinshDate_LineEdit,6,4,1,2)
        #右侧工作新增新增了修改按钮，的布局
        self.jobProgress_Layout = QVBoxLayout()
        self.jobProgress_Layout.addWidget(self.jobProgress_Label)
        self.jobProgress_Layout.addWidget(self.jobProgress_PushButton)
        self.jobProgress_Widget = QWidget()
        self.jobProgress_Widget.setLayout(self.jobProgress_Layout)
        self.right_Layout.addWidget(self.jobProgress_Widget,7,0)
        self.right_Layout.addWidget(self.jobProgress_TextEdit,7,1,1,7)

        # #右侧-详细信息组件框
        # self.groupBox_Right = QGroupBox()
        # self.groupBox_Right.setObjectName("groupBox_Right")
        # self.groupBox_Right.setTitle('详细信息：')
        # self.groupBox_Right.setLayout(self.right_Layout)
        # self.groupBox_Right.setContentsMargins(10, 0, 0, 0)
        self.right_Widget = QWidget()
        self.right_Widget.setObjectName('right_Widget')
        self.right_Widget.setLayout(self.right_Layout)
        self.right_Widget.setFixedWidth(760)
        #self.right_Widget.setContentsMargins(10, 10, 10, 10)

        #设置分栏
        self.splitter = QSplitter()
        self.splitter.setOrientation(Qt.Horizontal)#纵向分割，左右分
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")

        self.splitter.addWidget(self.left_Widget)
        self.splitter.addWidget(self.right_Widget)
        self.splitter.setSizes([1000, 1000])#设置初始化分割比例，要在加载小部件之后做才行
        self.splitter.setContentsMargins(0, 0, 0, 0)

        #中心窗口的布局
        # self.centralLayout = QHBoxLayout()
        # self.centralLayout.setObjectName("centralLayout")
        #
        # self.centralLayout.addWidget(self.splitter)
        # self.centralWidget.setLayout(self.centralLayout)

        MainWindow.setCentralWidget(self.splitter)

        #状态栏
        self.status = MainWindow.statusBar()
        self.status.showMessage('敏于观察，勤于思考，善于综合，勇于创新',5000)#5秒后消失
        MainWindow.setStatusBar(self.status)
        #菜单栏
        self.menubar = MainWindow.menuBar()
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        #菜单栏的按钮动作清单
        self.newAction = QAction(QIcon('./res/LOGO.ico'), "新建", MainWindow)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.setStatusTip("点击新建工作任务")
        #self.newAction.triggered.connect(qApp.quit)


        self.reloginAction = QAction(QIcon('./res/LOGO.ico'), "切换用户", MainWindow)
        self.reloginAction.setShortcut("Ctrl+L")
        self.reloginAction.setStatusTip("切换登录用户")
        #self.newAction.triggered.connect(qApp.quit)

        self.exitAction = QAction(QIcon('./res/LOGO.ico'), "退出", MainWindow)
        self.exitAction.setShortcut("Ctrl+Q")
        self.exitAction.setStatusTip("点击退出")
        self.exitAction.triggered.connect(qApp.quit)

        self.firstAction = QAction(QIcon('./res/LOGO.ico'),"绩效模板", MainWindow)
        self.firstAction.setStatusTip("按绩效模板导出全部需求")

        self.secondAction = QAction(QIcon('./res/LOGO.ico'),"默认格式", MainWindow)
        self.secondAction.setStatusTip("默认格式导出全部需求列表")
        #菜单栏的菜单清单
        self.impMenu = QMenu("导出", MainWindow)
        self.impMenu.addAction(self.firstAction)
        self.impMenu.addSeparator()
        self.impMenu.addAction(self.secondAction)

        self.filemenu = QMenu("文件", MainWindow)
        self.filemenu.addAction(self.newAction)
        self.filemenu.addAction(self.reloginAction)
        self.filemenu.addMenu(self.impMenu)
        self.filemenu.addSeparator()
        self.filemenu.addAction(self.exitAction)

        #self.menubar.addMenu(self.filemenu)
        #self.menubar.addMenu(self.impMenu)
        #调用QSS样式文件
        with open('./res/QSS/MainWindow_style1.qss','r',encoding='utf-8') as f:
            MainWindow.setStyleSheet(f.read())



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

