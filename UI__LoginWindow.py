from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_LoginWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 100)
        Dialog.setWindowTitle("登录")  # 设置窗口主题
        Dialog.setWindowIcon(QIcon('./res/LOGO.ico'))  # 设置窗口图标

        self.username_Label = QLabel('用户名：')
        self.username_Label.setObjectName("username_Label")

        self.password_Label = QLabel('密码：')
        self.password_Label.setObjectName("password_Label")

        self.username_LineEdit = QLineEdit()
        self.username_LineEdit.setClearButtonEnabled(True)
        #self.username_LineEdit.setFocusPolicy(Qt.ClickFocus)
        self.username_LineEdit.setObjectName("username_LineEdit")

        self.password_LineEdit = QLineEdit()
        self.password_LineEdit.setClearButtonEnabled(True)
        #self.password_LineEdit.setFocusPolicy(Qt.ClickFocus)
        self.password_LineEdit.setObjectName("password_LineEdit")
        self.password_LineEdit.setEchoMode(QLineEdit.Password)

        self.keeppassword_Checkbox = QCheckBox('保存密码')

        self.ok_PushButton = QPushButton('登录')
        self.ok_PushButton.setObjectName("ok_PushButton")

        # 定义一个List_Layout垂直布局
        List_Layout = QGridLayout()
        # 将表单的子窗体控件和保存按钮控件放入List_Layout垂直布局
        List_Layout.setSpacing(10)
        List_Layout.addWidget(self.username_Label, 0, 0)
        List_Layout.addWidget(self.username_LineEdit, 0, 1)
        List_Layout.addWidget(self.password_Label, 1, 0)
        List_Layout.addWidget(self.password_LineEdit, 1, 1)
        List_Layout.addWidget(self.keeppassword_Checkbox, 2, 1)
        List_Layout.addWidget(self.ok_PushButton, 3, 1)
        Dialog.setLayout(List_Layout)

        self.ok_PushButton.clicked.connect(Dialog.accept)
        QMetaObject.connectSlotsByName(Dialog)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_LoginWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

