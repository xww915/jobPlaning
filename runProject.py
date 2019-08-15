# -*- coding: utf-8 -*-
'''
pyinstaller -F -w -i res\LOGO.ico runProject.py
'''

import sys
from Def import *
from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtSql import QSqlDatabase

def connectDB():
    '''
    连接数据库
    '''
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("./res/db/jobplaning.db")
    # 数据库的路径
    if not db.open():
        QMessageBox.critical(None, "严重错误", "数据连接失败，程序无法使用，请按取消键退出", QMessageBox.Cancel)
        return False
    return db

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if database_download():
        db = connectDB()
        if db:
            MainWindow = MainWindow(db, offline=False)
            MainWindow.show()
            sys.exit(app.exec_())
    else:
        rr = QMessageBox.warning(None, "严重错误", "数据连接失败，是否启动离线模式？离线模式将无法同步数据！", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if rr == QMessageBox.Yes:
            db = connectDB()
            if db:
                MainWindow = MainWindow(db, offline=True)
                MainWindow.show()
                sys.exit(app.exec_())