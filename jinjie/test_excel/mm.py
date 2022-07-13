

'''import xlrd

# 打开
wb = xlrd.open_workbook('test.xlsx')
print( 'sheet名称:', wb.sheet_names())
print( 'sheet数量:', wb.nsheets)
# 根据 sheet 索引获取 sheet
sh = wb.sheet_by_index(0)
# 根据 sheet 名称获取 sheet
# sh = wb.sheet_by_name('test')
print( u'sheet %s 有 %d 行' % (sh.name, sh.nrows))
print( u'sheet %s 有 %d 列' % (sh.name, sh.ncols))
print('第二行内容:', sh.row_values(1))
print('第三列内容:', sh.col_values(2))
print('第二行第三列的值为:', sh.cell_value(1, 2))
print('第二行第三列值的类型为:', type(sh.cell_value(1, 2)))'''

import xlrd, xlwt
from xlutils.copy import copy

def avg(list):
    sumv = 0
    for i in range(len(list)):
        sumv += list[i]
    return int(sumv / len(list))
# formatting_info 为 True 表示保留原格式
wb = xlrd.open_workbook('test.xls', formatting_info=True)
# 复制
wbc = copy(wb)
sh = wb.sheet_by_index(0)
age_list = sh.col_values(2)
age_list = age_list[1:len(age_list)-1]
avg_age = avg(age_list)
sh = wbc.get_sheet(0)
# 设置左对齐
alm = xlwt.Alignment()
alm.horz = 0x01
style = xlwt.XFStyle()
style.alignment = alm
sh.write(5, 2, avg_age, style)
wbc.save('test3.xls')