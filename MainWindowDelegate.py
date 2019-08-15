# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QStyledItemDelegate, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

class TableDelegate(QStyledItemDelegate):
    '''
    自定义委托（代理）
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()

    def createEditor(self, parent, option, index):
        '''
        这个函数返回用于编辑index指定的项目以进行编辑的小部件。 父窗口小部件和样式选项用于控制编辑器窗口小部件的显示方式。

        parent：表示我们下面的小部件承载的位置。

        option：它是QStyleOptionViewItem对象。QStyleOptionViewItem类用于描述用于在视图窗口小部件中绘制Item的参数。
                QStyleOptionViewItem包含QStyle函数为Qt的模型/视图类绘制Item所需的所有信息。

        index：QModelIndex类对象，用于定位数据模型中的数据。
        '''
        editor = QComboBox(parent)
        editor.setIconSize(QSize(25, 25))
        # 首先创建一个下拉框，并设置它的图标大小。这里需要注意的是：parent，必须有

        if index.column() == 2:
            editor.addItem(QIcon("./res/jobtype/1.png"), "数据接入")
            editor.addItem(QIcon("./res/jobtype/2.png"), "数据导出")
            editor.addItem(QIcon("./res/jobtype/3.png"), "权限变更")
            editor.addItem(QIcon("./res/jobtype/4.png"), "故障处理")
            editor.addItem(QIcon("./res/jobtype/5.png"), "租户创建")
            editor.addItem(QIcon("./res/jobtype/6.png"), "数据提取")
            editor.addItem(QIcon("./res/jobtype/7.png"), "材料编写")
            editor.addItem(QIcon("./res/jobtype/8.png"), "MPP故障处理")
            editor.addItem(QIcon("./res/jobtype/8.png"), "其它")
            return editor
        elif index.column() == 4:
            editor.addItem(QIcon("./res/jobstaus/1.png"), "排期中")
            editor.addItem(QIcon("./res/jobstaus/2.png"), "进行中")
            editor.addItem(QIcon("./res/jobstaus/3.png"), "待评估")
            editor.addItem(QIcon("./res/jobstaus/4.png"), "已完成")
            return editor
        elif index.column() == 5:
            editor.addItem(QIcon("./res/jobemergencylevel/1.png"), "普通需求")
            editor.addItem(QIcon("./res/jobemergencylevel/2.png"), "紧急需求")
            editor.addItem(QIcon("./res/jobemergencylevel/3.png"), "特殊通道")
            return editor
        elif index.column() == 10:
            editor.addItem(QIcon("./res/orderway/1.png"), "公务")
            editor.addItem(QIcon("./res/orderway/2.png"), "需求管理系统")
            editor.addItem(QIcon("./res/orderway/3.png"), "邮件")
            editor.addItem(QIcon("./res/orderway/4.png"), "电话")
            editor.setEditable(True)
            return editor
        # elif index.column() == 10:
        #     classifications = ["", "公务", "需求管理系统", "邮件", "电话"]
        #     editor.addItems(classifications)
        #     editor.setEditable(True)
        #     return editor
            # 给第0列或者第5列的下拉框增加数据，并将这个下拉框返回
        else:
            return super().createEditor(parent, option, index)
            # 不是上面这种情况的话，调用父类默认的createEditor()函数
    
    def setEditorData(self, editor, index):
        '''
        从模型索引指定的数据模型项中通过编辑器显示和编辑的数据。
        当前表格里面是什么内容，我们双击显示下拉框里面的当前内容就是什么内容。
        '''
        if index.column() == 2 or index.column() == 4 or index.column() == 5 or index.column() == 10:
            text = index.model().data(index, Qt.EditRole)
            editor.setCurrentText(text)
        else:
            return super().setEditorData(editor, index)

    
    def setModelData(self, editor, model, index):
        '''
        从编辑器窗口小部件获取数据，并将其存储在项目索引处的指定模型中。
        默认实现从编辑器窗口小部件的用户属性获取要存储在数据模型中的值。
        '''
        if index.column() == 2 or index.column() == 4 or index.column() == 5 or index.column() == 10:
            strData = editor.currentText()
            model.setData(index, strData, Qt.EditRole)
        else:
            return super().setModelData(editor, model, index)

    def updateEditorGeometry(self, editor, option, index):
        '''
        重新绘制下拉框，你可以尝试注释看看效果
        '''
        editor.setGeometry(option.rect)