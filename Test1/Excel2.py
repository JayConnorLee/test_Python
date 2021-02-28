#'from contextlib import
import psutil
import xlwings as xl
import psutil
import sys
import subprocess as sp
import win32gui

from win32com.client import Dispatch


xlPIDs = []

for proc in psutil.process_iter():
    if proc.name == "EXCEL.EXE": xlPIDs.append(proc.pid)

winPIDsAndTitle = []
win32gui.EnumWindows(lambda hwnd, resultList: resultList.append((win32gui.GetWindowThreadProcessId(hwnd), win32gui.GetWindowText(hwnd))),winPIDsAndTitle)

for PID, Title in winPIDsAndTitle:
    if PID in xlPIDs:
        vTitle = Title
        break

xl = win32com.client.GetObject(None, "Excel.Application")


sp.call(["taskkill", "/f", "/im", "EXCEL.EXE"])
sp.call(["taskkill", "/f", "/im", "excel.exe"])

xl = Dispatch("Excel.Application",)
xl.visible = True

vPath = r'C:\Users\secli\Downloads\Macro Bingure.xlsm'
wb1 = xl.workbooks.open(vPath)





