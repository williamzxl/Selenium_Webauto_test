#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import xlrd, xlsxwriter
xls = xlrd.open_workbook(r'userinfo.xlsx')
print(xls)
print(xls.sheets())
sheet0 = xls.sheets()[0]
print(sheet0.nrows)
print(sheet0.ncols)

print(sheet0.row_values(0))
print(sheet0.row_values(1))
print(sheet0.col_values(0))
print(sheet0.col_values(1))

print(sheet0.cell(0,0).value)

new_xl = xlsxwriter.Workbook('newsheet.xls')
sheet0 = new_xl.add_worksheet('Maizi')
sheet0.write_string(0, 0, 'name')
sheet0.write_string(0, 1, 'pwd')
sheet0.set_column('A:B', 30)
new_xl.close()