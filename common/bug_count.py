# -*- coding: utf-8 -*- 
# 姓名：李万伦
# 时间：2023/1/3  15:10
# 文件名：xlrd_xlwt.py
# 完成Excel内容追加写入
import xlwt,xlrd
from xlutils.copy import copy
def clear_count():
    data = xlrd.open_workbook('D:\\uoffer\自动化脚本\\uoffer_api\\bug\\test.xls', formatting_info=True)
    excel = copy(wb=data) # 完成xlrd对象向xlwt对象转换
    excel_table = excel.get_sheet(0) # 获得要操作的页
    excel_table.write(1,0,0)
    excel_table.write(1,1,0)
    excel.save('D:\\uoffer\自动化脚本\\uoffer_api\\bug\\test.xls')
def fail_count():
    data = xlrd.open_workbook('D:\\uoffer\自动化脚本\\uoffer_api\\bug\\test.xls',formatting_info=True)
    excel = copy(wb=data) # 完成xlrd对象向xlwt对象转换
    excel_table = excel.get_sheet(0) # 获得要操作的页
    table = data.sheets()[0]
    nrows = table.nrows # 获得行数
    ncols = table.ncols # 获得列数
    pass_count=table.cell_value(rowx=1, colx=0)
    print(pass_count)
    fail_count=table.cell_value(rowx=1, colx=1)
    print(fail_count)
    # excel_table.write(1,0,pass_count+1) # 因为单元格从0开始算，所以row不需要加一
    excel_table.write(1,1,fail_count+1) # 因为单元格从0开始算，所以row不需要加一
    excel.save('D:\\uoffer\自动化脚本\\uoffer_api\\bug\\test.xls')
def pass_count():
    data = xlrd.open_workbook('D:\\uoffer\自动化脚本\\uoffer_api\\bug\\test.xls',formatting_info=True)
    excel = copy(wb=data) # 完成xlrd对象向xlwt对象转换
    excel_table = excel.get_sheet(0) # 获得要操作的页
    table = data.sheets()[0]
    nrows = table.nrows # 获得行数
    ncols = table.ncols # 获得列数
    pass_count=table.cell_value(rowx=1, colx=0)
    print(pass_count)
    fail_count=table.cell_value(rowx=1, colx=1)
    print(fail_count)
    excel_table.write(1,0,pass_count+1) # 因为单元格从0开始算，所以row不需要加一
    # excel_table.write(1,1,fail_count+1) # 因为单元格从0开始算，所以row不需要加一
    excel.save('D:\\uoffer\自动化脚本\\uoffer_api\\bug\\test.xls')
def last_count():
    data = xlrd.open_workbook('D:\\uoffer\自动化脚本\\uoffer_api\\bug\\test.xls', formatting_info=True)
    table = data.sheets()[0]
    pass_count=int(table.cell_value(rowx=1, colx=0))
    fail_count=int(table.cell_value(rowx=1, colx=1))
    return pass_count,fail_count

# if __name__ == '__main__':
#     list=last_count()
#     print(list)
#     print(list[0]+list[1])

