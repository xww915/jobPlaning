from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests
from time import sleep
from PyQt5.QtSql import QSqlQuery

#从用户表查询需求管理系统用户名密码
def getRTMSUserInfo(username):
    query = QSqlQuery()
    selectRTMSUserinfo = "select RTMSusername,RTMSpassword from user where username = '{}'".format(username)
    # 数据库返回插入成功还是失败
    query.exec(selectRTMSUserinfo)
    while query.next():
        RTMSusername = query.value(0)
        RTMSpassword = query.value(1)
        return RTMSusername,RTMSpassword
#搜索对应需求的方法
def searchRequest(browser,username,password,RTMScode='',RTMSname='',loginURL='http://10.68.66.140:8880/demand/login.html'):
    #为了避免函数执行完自动关闭浏览器的情况，需要在函数外创建浏览器对象，然后传入进来使用，这样执行完浏览器对象会保留
    # 打开需求管理系统首页
    try:
        browser.get(loginURL)
        #print('打开需求管理系统首页')
    except:
        print('打开需求管理系统首页-失败！')
        return False
    # 输入用户名
    try:
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'loginBtn')))
        userNameInput = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'username')))
        userNameInput.send_keys(username)
        #print('输入用户名')
    except:
        print('输入用户名-失败！')
        return False

    # 输入密码
    try:
        passWordInput = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'password')))
        passWordInput.send_keys(password)
        #print('输入密码')
    except:
        print('输入密码-失败！')
        return False

    # 点击登录按钮
    try:
        loginButtonClick = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'loginBtn')))
        sleep(0.2)
        loginButtonClick.click()
        #print('点击登录按钮')
    except:
        print('点击登录按钮-失败！')
        return False

    # 等待主页面加载
    try:
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'ulb0591686d81b4c888fe4c0ead2c5f954')))
        #print('等待主页面加载')
    except:
        print('等待主页面加载-失败！')
        return False

    notFoundFlag = True
    #查找需求：如果传入了需求名称则先尝试在待办区搜索，如果待办区没有则在全量需求中搜索
    if RTMSname:
        try:
            browser.switch_to.frame('iframe0')
            xpath1 = "//*[contains(text(),'" + RTMSname + "')]"
            #print(xpath1)
            browser.find_element_by_xpath(xpath1).click()
            notFoundFlag = False
        except:
            browser.switch_to.parent_frame()

    if RTMScode !='待补充' and notFoundFlag:
        # 点击需求管理
        requestManagementList = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'ulb0591686d81b4c888fe4c0ead2c5f954')))
        sleep(0.2)
        requestManagementList.click()
        # 点击需求查询（全量）
        requestSeatchList = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'secad8446171b304d7dae28f8ea4d85f31e')))
        sleep(0.2)
        requestSeatchList.click()
        # 切换到右侧的需求查询窗口
        sleep(0.2)
        browser.switch_to.frame('iframe3')  # 通过ID切换到Frame
        # 输入需求编码
        requestCodeWait = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'recode')))
        sleep(0.2)
        requestCodeWait.send_keys(RTMScode)
        # 点击查询
        seatchButtonWait = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'queryBtn')))
        sleep(0.2)
        seatchButtonWait.click()

        table = browser.find_element_by_id('table')
        sleep(1)
        table.find_element_by_xpath('//input[@name="btSelectItem"]').click()

        # 点击查询
        try:
            seatchButtonWait = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, 'detail')))
            sleep(0.2)
            seatchButtonWait.click()
        except:
            return False

#新建需求的方法
def createRequest(browser, username, password, jobName='', jobProgress='', loginURL='http://10.68.66.140:8880/demand/login.html'):
    #为了避免函数执行完自动关闭浏览器的情况，需要在函数外创建浏览器对象，然后传入进来使用，这样执行完浏览器对象会保留
    # 打开需求管理系统首页
    try:
        browser.get(loginURL)
        print('打开需求管理系统首页')
    except:
        print('打开需求管理系统首页-失败！')
        return False
    # 输入用户名
    try:
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'loginBtn')))
        userNameInput = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'username')))
        userNameInput.send_keys(username)
        print('输入用户名')
    except:
        print('输入用户名-失败！')
        return False

    # 输入密码
    try:
        passWordInput = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'password')))
        passWordInput.send_keys(password)
        print('输入密码')
    except:
        print('输入密码-失败！')
        return False

    # 点击登录按钮
    try:
        loginButtonClick = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'loginBtn')))
        sleep(0.2)
        loginButtonClick.click()
        print('点击登录按钮')
    except:
        print('点击登录按钮-失败！')
        return False

    # 等待主页面加载
    try:
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'ulb0591686d81b4c888fe4c0ead2c5f954')))
        print('等待主页面加载')
    except:
        print('等待主页面加载-失败！')
        return False

    # 点击需求管理
    requestManagementList = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'ulb0591686d81b4c888fe4c0ead2c5f954')))
    sleep(0.2)
    requestManagementList.click()
    # 点击发起需求
    requestSeatchList = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'sec359ec20996a04de880e1ce1045868ca0')))
    sleep(0.2)
    requestSeatchList.click()
    # 切换到右侧的需求基本信息窗口
    sleep(0.2)
    browser.switch_to.frame('iframe1')  # 通过ID切换到Frame1
    # 输入需求名称
    requestCodeWait = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'reName')))
    sleep(0.2)
    requestCodeWait.send_keys(jobName)
    # 点选完成日期
    sleep(0.2)
    browser.find_element(By.CSS_SELECTOR, ".glyphicon-calendar").click()
    sleep(0.2)
    browser.find_element(By.CSS_SELECTOR, ".datetimepicker-days tfoot .today").click()
    #点选业务域
    sleep(0.2)
    dropdown = browser.find_element(By.ID, "reInvolveArea")
    dropdown.find_element(By.XPATH, "//option[. = 'D域(大数据需求)']").click()
    #点选产品线条
    sleep(0.2)
    dropdown = browser.find_element(By.ID, "reLine")
    dropdown.find_element(By.XPATH, "//option[. = '产品（市场）']").click()
    # 点选业务类型
    sleep(0.2)
    dropdown = browser.find_element(By.ID, "retype")
    dropdown.find_element(By.XPATH, "//option[. = '个人业务类']").click()
    # 输入业务背景
    sleep(0.2)
    browser.find_element(By.ID, "reBackGround").send_keys(jobProgress)
    # 输入业务背景
    sleep(0.2)
    browser.find_element(By.ID, "busFlow").send_keys(jobProgress)
    #点击审批人所在科室
    #sleep(0.2)
    #browser.find_element(By.CSS_SELECTOR, ".list-group-item").click()
    #点击审批人
    sleep(0.2)
    browser.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(2)").click()
    #点击>>按钮，添加审批人
    sleep(0.2)
    browser.find_element(By.ID, "rightButton").click()

def getRequireTasksList(requests, username, password, URLlogin='http://10.68.66.140:8890/userlogin/login',URLgetlist='http://10.68.66.140:8890/mainreflowapprove/listRequireTasks'):
    data = {'username': username, 'password': password}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
    }
    try:
        response = requests.post(URLlogin,data=data,headers=headers)
        #print(response.text)
    except:
        res = '连接中断'
        return res
    try:
        response = requests.get(URLgetlist,headers=headers)
        print(response.json())
    except:
        res = '鉴权失败'
        return res
    try:
        res = str(response.json()['data']['total'])
    except:
        res = 'Error'
    return res


if __name__ == '__main__':
    # browser = webdriver.Chrome()
    # if browser:
    #     print(createRequest(browser,'xiaoweis','77o0I093','【转大数据室】大数据平台DACP权限申请','【转大数据室】大数据平台DACP权限申请'))
    requests = requests.Session()
    print(getRequireTasksList(requests,'xiaoweis','77o0I093'))