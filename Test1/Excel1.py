#'from contextlib import
import xlwings as xl
import sys
from win32com.client import Dispatch


xl = Dispatch("Excel.Application")
xl.visible = True

wb = xl.workbooks.add


@staticmethod
def funcname(parameter_list):
    pass

def funcname(self, parameter_list):
    pass

def funcname(self, parameter_list):
    raise NotImplementedError

@staticmethod
def CheckVariable(self, var):
    try:
        var
    except:
        var = None

def xl_CloseAllWorkbooks(wb1=None):
    try:
        wb1
    except NameError:
        wb1 = None

    wb1.api.close
    ##try:
        
    #except:
    #    pass#



path = r'C:\Users\secli\Downloads\Macro Bingure.xlsm'
wb = xl.Book(path)
xlApp = wb.api.parent


ws = wb.sheets('Sheet2')
rU = ws.used_range

xl_CloseAllWorkbooks(wb)
wb.api.close
rU.select