#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time
import xlsxwriter
class Loginfo(object):
    def __init__(self, path = '', mode= 'a'):
        self.file_time = time.strftime('%Y-%m-%d', time.gmtime())
        self.log_time = time.strftime('%H-%M-%S')
        fname = "{}{}".format(path, self.file_time)
        self.log = open("{}{}.txt".format(path, fname), mode)

    def log_init(self, sheetname, *title):
        pass

    def log_write(self, msg):
        self.log.write("\n{}+{}".format(self.log_time, msg))

    def log_close(self):
        self.log.close()

class Xlloginfo(object):
    def __init__(self, path = ''):
        fname = '{}{}'.format(path,time.strftime('%Y-%m-%d', time.gmtime()))
        self.row = 0
        self.xl = xlsxwriter.Workbook(path+fname+'.xls')
        self.style = self.xl.add_format({'bg_color':'red'})

    def xl_write(self, *args):
        col = 0
        style = ''
        if 'Error' in args:
            style = self.style
        for val in args:
            self.sheet.write_string(self.row, col, val)
            col += 1
        self.row += 1

    def log_init(self, sheetname, *title):
        self.sheet = self.xl.add_worksheet(sheetname)
        self.sheet.set_column('A:E', 30)
        self.xl_write(*title)

    def log_write(self, *args):
        self.xl_write(*args)

    def log_close(self):
        self.xl.close()

if __name__ == '__main__':
    # log = Loginfo()
    # log.log_write('hahaha')
    # log.log_close()

    xinfo = Xlloginfo()
    xinfo.log_init('test12','uname','pwd', 'result', 'info')
    xinfo.log_close()