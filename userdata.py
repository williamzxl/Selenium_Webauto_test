#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import codecs
import xlrd, xlsxwriter

def get_webinfo(path):
    web_info = {}
    with codecs.open(path,'r','utf-8') as config:
        for line in config:
            result = [ele.strip() for ele in line.split('=')]
            # print("Result,",result)
            web_info.update(dict([result]))
    return web_info

def get_userinfo(path):
    user_info = []
    with codecs.open(path,'r','utf-8') as config:
        for line in config:
            user_dict = {}
            result = [ele.strip() for ele in line.split(';')]
            for info in result:
                account = [ele.strip() for ele in info.split('=')]
                # print(account)
                # print("Dict",dict([account]))
                user_dict.update(dict([account]))
            user_info.append(user_dict)
    return user_info

class XlUserInfo(object):
    def __init__(self, path= ''):
        self.xl = xlrd.open_workbook(path)

    def floattostr(self, val):
        if isinstance(val, float):
            val = str(int(val))
        return val

    def get_sheet_info(self):
        listkey = ['uname','pwd']
        infolist = []
        for row in range(1, self.sheet.nrows):
            info = [self.floattostr(val) for val in self.sheet.row_values(row)]
            temp = zip(listkey, info)
            infolist.append(dict(temp))
        return infolist

    def get_sheetinfo_by_name(self, name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheet_info()

    def get_sheetinfo_by_index(self, index):
        self.sheet = self.xl.sheet_by_index(index)
        return self.get_sheet_info()



if __name__ == '__main__':
    # userinfo = get_userinfo(r'userinfo.txt')
    # print(userinfo)
    # for user in userinfo:
    #     print(user)
    # webinfo = get_webinfo(r'webinfo.txt')
    # print(webinfo)
    xinfo = XlUserInfo(r'userinfo.xlsx')
    info = xinfo.get_sheetinfo_by_index(0)
    print(info)
    info = xinfo.get_sheetinfo_by_name('Sheet1')
    print(info)
