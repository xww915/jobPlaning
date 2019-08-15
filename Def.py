# -*- coding: utf-8 -*-

import os
import shutil
from subprocess import run#subprocess.run()函数会将本来打印到cmd上的内容打印到python执行界面上，所以避免了出现cmd弹出框的问题
from PIL import ImageGrab,Image
import ftplib
import zipfile
import hashlib

host = '10.68.81.147'
port = 2018
username = 'ftpuser'
password = 'Lnyd*132'
databaseFileName = 'jobplaning.db'

# 从剪贴板读取图片保存到文件
def grab(Path):
    im = ImageGrab.grabclipboard()
    # 判断如果从剪贴板获取的是图片格式则保存成文件
    if isinstance(im, Image.Image):
        im.save(Path)
    else:
        pass

#调用截图dll
def Cut(FileName):
    DllPath = os.getcwd() + "\CameraDll.dll"
    command2 = "Rundll32.exe " + DllPath + ", CameraSubArea"
    run(command2, shell=True)
    grab(FileName)  # 保存图片函数

#打开文件夹
def OpenFolder(Path):
    command1 = "start explorer " + Path
    run(command1, shell=True)

#测试FTP是否可以连通
def ftp_test():
    f = ftplib.FTP()
    try:
        f.connect(host, port, timeout = 1)
        f.login(username, password)
        return True
    except:
        return False

#下载附件
def ftp_downloadzip(fileName,download_fileName):
    f = ftplib.FTP()
    f.connect(host, port)
    f.login(username, password)  # 登录
    '''以二进制形式下载文件'''
    f.cwd('/home/ftpuser/zipfiles/')#切换到下载目录
    #print(f.dir())
    #print(f.nlst())
    file_list = f.nlst()#获取当前目录下的文件列表
    if fileName in file_list:
        bufsize = 1024  # 设置缓冲器大小
        fp = open(download_fileName, 'wb')
        f.retrbinary('RETR %s' % fileName, fp.write, bufsize)
        fp.close()
        return True
    else:
        return False

#上传附件-FTP连接
def ftp_uploadzip(output_filepath,fileName):
    f = ftplib.FTP()
    f.connect(host, port)
    f.login(username, password)  # 登录
    '''以二进制形式上传文件'''
    file_remote = '/home/ftpuser/zipfiles/' + fileName
    #print(file_remote)
    #file_remote = 'joblist.csv'
    #file_local = r'D:\joblist.csv'
    bufsize = 1024  # 设置缓冲器大小
    fp = open(output_filepath, 'rb')
    f.storbinary('STOR ' + file_remote, fp, bufsize)
    fp.close()
#上传附件
def uploadzip(Path,output_filename):
    output_filepath = os.getcwd() + '\\' + output_filename  # 选择压缩包临时存放位置
    z = zipfile.ZipFile(output_filepath, 'w', zipfile.ZIP_DEFLATED)  # 创建一个压缩文件，'w'为写的方式
    for dirpath, dirnames, filenames in os.walk(Path):  # 遍历需要压缩的文件夹
        fpath = dirpath.replace(Path, '')  # 这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''  # 实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:  # 将其中的每个文件添加到压缩文件中
            z.write(os.path.join(dirpath, filename), fpath + filename)
    z.close()  # 关闭压缩文件
    try:  # 尝试上传文件，调用文件上传函数
        ftp_uploadzip(output_filepath, output_filename)
        res = True
    except:
        res = False
    try:  # 上传之后删除打包文件
        os.remove(output_filepath)
        res = True
    except:
        res = False
    return res

#下载数据库主文件
def database_download():
    if ftp_test():
        saveFileName = os.getcwd() + '\\res\\db\\' + databaseFileName
        saveNeedCheckFileName = os.getcwd() + '\\res\\db\\needchack_' + databaseFileName
        f = ftplib.FTP()
        f.connect(host, port)
        f.login(username, password)  # 登录
        '''以二进制形式下载文件'''
        # file_remote = filepath.split('\\')[1]
        file_remote = '/home/ftpuser/datafile/' + databaseFileName
        bufsize = 1024  # 设置缓冲器大小
        fp = open(saveFileName, 'wb')
        f.retrbinary('RETR %s' % file_remote, fp.write, bufsize)
        fp.close()
        shutil.copyfile(saveFileName, saveNeedCheckFileName)
        return True
    else:
        return False

#下载校验数据库主文件
def checkdatabase_download():
    if ftp_test():
        saveFileName = os.getcwd() + '\\res\\db\\' + 'check_' + databaseFileName
        f = ftplib.FTP()
        f.connect(host, port)
        f.login(username, password)  # 登录
        '''以二进制形式下载文件'''
        # file_remote = filepath.split('\\')[1]
        file_remote = '/home/ftpuser/datafile/' + databaseFileName
        bufsize = 1024  # 设置缓冲器大小
        fp = open(saveFileName, 'wb')
        f.retrbinary('RETR %s' % file_remote, fp.write, bufsize)
        fp.close()
        return True
    else:
        return False

#校验MD5
def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        # 必须是rb形式打开的，否则的两次出来的结果不一致
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    return hash.hexdigest()

#上传数据库主文件
def ftp_upload():
    if ftp_test():
        if checkdatabase_download():
            checkFile = os.getcwd() + '\\res\\db\\check_' + databaseFileName
            needCheckFile = os.getcwd() + '\\res\\db\\needchack_' + databaseFileName
            if md5sum(checkFile) == md5sum(needCheckFile):
                filepath = os.getcwd() + '\\res\\db\\' + databaseFileName
                f = ftplib.FTP()
                f.connect(host, port)
                f.login(username, password)  # 登录
                '''以二进制形式上传文件'''
                # file_remote = filepath.split('\\')[1]
                file_remote = '/home/ftpuser/datafile/' + databaseFileName
                # file_remote = 'joblist.csv'
                # file_local = r'D:\joblist.csv'
                bufsize = 1024  # 设置缓冲器大小
                fp = open(filepath, 'rb')
                f.storbinary('STOR ' + file_remote, fp, bufsize)
                fp.close()
                saveFileName = os.getcwd() + '\\res\\db\\' + databaseFileName
                saveNeedCheckFileName = os.getcwd() + '\\res\\db\\needchack_' + databaseFileName
                shutil.copyfile(saveFileName, saveNeedCheckFileName)
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def saveToUserInfo(username,password,ischecked,filePath):
    with open(filePath, 'w', encoding='utf-8') as f:
        f.write(username + '\n')
        f.write(password + '\n')
        f.write(ischecked + '\n')

def readFromUserInfo(filePath):
    res = []
    with open(filePath, 'r', encoding='utf-8') as f:
        for item in f.readlines():
            res.append(item.replace('\n',''))
    return res


if __name__ == '__main__':
    print(ftp_upload())