#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from userdata import get_webinfo, get_userinfo, XlUserInfo
from log_module import Loginfo, Xlloginfo

def get_ele_times(driver, times, func):
    return WebDriverWait(driver, times).until(func)

def openBrower():
    '''
    :return: webdriver handle
    '''
    webdriver_handle = webdriver.Firefox()
    return webdriver_handle

# def openUrl(handle, url):
#     handle.get(url)
#     handle.maximize_window()

def openUrl(handle, arg):
    handle.get(arg['url'])
    handle.maximize_window()

def findElement(d, arg):
    '''
    1.test_id:
    2.USERID
    3.pwdid
    4.loginid
    :param d:
    :param arg:
    :return:
    '''
    if 'text_id' in arg:
        ele_login = get_ele_times(d, 10, lambda d: d.find_element_by_link_text(arg['text_id']))
        ele_login.click()
    userEle = d.find_element_by_id(arg['userid'])
    pwdEle = d.find_element_by_id(arg['pwdid'])
    loginEle = d.find_element_by_id(arg['loginid'])
    # sign_out
    # signOutEle = d.find_element_by_id(arg['signOutid'])
    # print(signOutEle)
    return userEle, pwdEle, loginEle

def findOutele(d, arg):
    try:
        signOutEle = d.find_element_by_id(arg['signOutid'])
        return signOutEle
    except:
        print("You are not login.")

def sendVal(eletuple, arg):
    '''

    :param eletuple:
    :param arg:
    :return:
    '''
    list_key = ['uname','pwd']
    i = 0
    for key in list_key:
        eletuple[i].send_keys('')
        eletuple[i].clear()
        # print(arg[key])
        eletuple[i].send_keys(arg[key])

        i += 1
    eletuple[2].click()

def checkResult(d, err_id, arg, log):
    result = False
    time.sleep(3)
    try:
        err = d.find_element_by_id(err_id)
        print("Account and pwd error")
        # msg = "account:{},password:{}==>error:{}".format(arg['uname'],arg['pwd'], err.text)
        log.log_write(arg['uname'], arg['pwd'], 'Error', err.text)
        print(err.text)
    except:
        print("Account and pwd Right")
        # msg = "Account:{},password:{}==>pass!".format(arg['uname'], arg['pwd'])
        log.log_write(arg['uname'], arg['pwd'], 'Pass')
        result = True
    return result

def logout(d, ele_dict):
    d.find_element_by_class_name(ele_dict['logout']).click()

def login_test(ele_dict,user_list):
    d = openBrower()
    # log = Loginfo()
    log = Xlloginfo()
    log.log_init('sheet1', 'uname', 'pwd','result', 'message')
    openUrl(d, ele_dict)
    ele_tuple = findElement(d, ele_dict)
    # print(user_list[0])
    for user_info in user_list:
        sendVal(ele_tuple, user_info)
        result = checkResult(d, ele_dict['errorid'], user_info, log)
        # sign_out
        # findOutele(d, ele_dict).click()
        if result:
            # logout
            logout(d, ele_dict)
            #login
            ele_tuple = findElement(d, ele_dict)
        else:
            ele_tuple = findElement(d, ele_dict)
    log.log_close()

if __name__ == '__main__':
    '''
    ele_dict = {
        'url': 'http://www.maiziedu.com',
        'uname':'maizi_test@139.com',
        'pwd': 'abc123456',
        'login_text':'Login',
        'text_id': login_text,
        'userid': 'id_account_l',
        'pwdid': 'id_password_l',
        'loginid': 'login_btn',
        'signOutid':'sign_out',
    }
    user_list = [{'uname':account,'pwd':pwd},]
    '''
    # file webinfo/userinfo get_webinfo(path),user_list = get
    ele_dict = get_webinfo(r'webinfo.txt')
    # user_list = get_userinfo(r'userinfo.txt')
    xinfo = XlUserInfo(r'userinfo.xlsx')
    user_list = xinfo.get_sheetinfo_by_index(0)
    login_test(ele_dict,user_list)


