from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_SendOrderWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 100)
        Dialog.setWindowTitle("选择转派人")  # 设置窗口主题
        Dialog.setWindowIcon(QIcon('./res/LOGO.ico'))  # 设置窗口图标

        self.sendOrder_Label = QLabel('请选择转派人')
        self.sendOrder_LineEdit = QComboBox()

        self.name_Label = QLabel('姓名：')
        self.name_LineEdit = QLabel()
        self.name_LineEdit.setStyleSheet("background:transparent;border-width:1;border-style:outset")

        self.credits_Label = QLabel('积分：')
        self.credits_LineEdit = QLabel()
        self.credits_LineEdit.setStyleSheet("background:transparent;border-width:1;border-style:outset")

        self.introduc_Label = QLabel('介绍：')
        self.introduc_LineEdit = QLabel()
        self.introduc_LineEdit.setStyleSheet("background:transparent;border-width:1;border-style:outset")

        self.chooseOrders_Label = QLabel('已选择：')
        self.chooseOrders_LineEdit = QLineEdit()

        self.ok_PushButton = QPushButton('确定')
        self.ok_PushButton.setObjectName("ok_PushButton")

        self.choose_PushButton = QPushButton('↓添加↓')
        self.choose_PushButton.setObjectName("choose_PushButton")

        self.clear_PushButton = QPushButton('↓清空↓')
        self.clear_PushButton.setObjectName("choose_PushButton")

        # 定义一个List_Layout垂直布局
        List_Layout = QGridLayout()
        # 将表单的子窗体控件和保存按钮控件放入List_Layout垂直布局
        List_Layout.setSpacing(10)
        List_Layout.addWidget(self.sendOrder_Label, 0, 0)
        List_Layout.addWidget(self.sendOrder_LineEdit, 0, 1)
        List_Layout.addWidget(self.name_Label, 1, 0)
        List_Layout.addWidget(self.name_LineEdit, 1, 1)
        List_Layout.addWidget(self.credits_Label, 1, 2)
        List_Layout.addWidget(self.credits_LineEdit, 1, 3)
        List_Layout.addWidget(self.introduc_Label, 2, 0)
        List_Layout.addWidget(self.introduc_LineEdit, 2, 1, 1, 3)
        List_Layout.addWidget(self.choose_PushButton, 3, 1)
        List_Layout.addWidget(self.clear_PushButton, 3, 2, 1, 2)
        List_Layout.addWidget(self.chooseOrders_Label, 4, 0)
        List_Layout.addWidget(self.chooseOrders_LineEdit, 4, 1, 1, 3)
        List_Layout.addWidget(self.ok_PushButton, 5, 1)
        Dialog.setLayout(List_Layout)

        self.ok_PushButton.clicked.connect(Dialog.accept)
        QMetaObject.connectSlotsByName(Dialog)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_SendOrderWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

