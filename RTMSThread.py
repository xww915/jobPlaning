
from PyQt5.QtCore import *
from DefRTMS import *
import time
import requests

class checkRTMSThread(QThread):
    #show_num = pyqtSignal(str)
    #定义信号
    show_time = pyqtSignal(str)
    def __init__(self, username, password, *args, **kwargs):
        super(checkRTMSThread, self).__init__(*args, **kwargs)
        self.requests = requests.Session()
        self.username = username
        self.password = password
        self.flag = 1

    def run(self, *args, **kwargs):
        while True:
            if self.flag ==1:
                #print(self.username,self.password)
                RTMSnum = getRequireTasksList(self.requests, self.username, self.password)
                #file_str = '需求管理系统当前待办数量：' RTMSnum
                #发送添加信号
                #self.show_num.emit(file_str)
                #获取当前时间
                date = QDateTime.currentDateTime()
                currtime = str(date.toString('yyyy-MM-dd hh:mm:ss'))
                res = '需求管理系统当前待办数量：' + RTMSnum + '，更新时间：' + currtime
                #print(res)
                #将信号发送出去
                self.show_time.emit(res)
                time.sleep(1)
            else:
                break

    def stop(self):
        self.flag = 0