import sys
import logging
from selenium import webdriver
import time
 
#chromedriver = r"C:\Users\Connor\Downloads\chromedriver_win32\chromedriver.exe"
chromedriver = r"C:\Users\Connor\Downloads\chromedriver_win32 (79)\chromedriver.exe"
iedriverServer = r"C:\Users\Connor\Downloads\IEDriverServer_x64_3.150.1\IEDriverServer.exe"

IeDriver = iedriverServer
#driver = webdriver.Chrome(chromedriver)%
driver = webdriver.Ie(IeDriver)
#driver.get('http:google.com')
#driver.get('http://www.google.com')
driver.get('http://www.naver.com')

#btn_Login = driver.find_element_by_xpath('//*[@id="account"]/div/a/i')
btn_Login = driver.find_elements_by_xpath("//input[@id='id']")
#driver.find_elements_by_xpath("//input[@id='id']").click()

#a = driver.findElement(By.xpath("//input[@id='id']"))
a = driver.find_elements(By.xpath("//input[@id='id']"))
id = driver.find_element_by_xpath("//input[@id='id']")
pw = driver.find_element_by_xpath("//input[@id='pw']")
btn_SignIn = driver.find_element_by_xpath("//input[@id='log.login']")
btn_SignIn2 = driver.find_element_by_xpath("//*[@id='frmNIDLogin']/fieldset/input").click()

id.send_keys('yue89')
pw.send_keys('qweasdzxc11!!')
btn_SignIn.click()

print('stop')
print('end')
