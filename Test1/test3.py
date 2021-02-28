



import xlwings as xl
import sys

#path = r'C:\Users\secli\Documents\jongchan.lee\Workspace\Dev\Macro Code test1.xlsm'#
path = r'C:\Users\secli\Downloads\Macro Bingure.xlsm'
wb = xl.Book(path)

ws = wb.sheets('Sheet2')
rU = ws.used_range

if ws.api.filtermode == False:
    rU.api.autofilter

FilterRange = ws.api.AutoFilter.Range
FilterHeader = FilterRange.Rows(1)



for h in FilterHeader:
    if ws.api.filtermode:
        ws.api.ShowAllData

#sys.stdout = 'a'#
print(wb.name)
sh1 = wb.sheets(1)
print(sh1.name)
