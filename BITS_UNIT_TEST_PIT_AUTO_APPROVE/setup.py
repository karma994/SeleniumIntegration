#title: Automate Testing For BITS
#Author: Tandin Wangchuk
#Discription : BITS Admin
import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
time.sleep(5)
stagingurl = "http://10.11.1.13/bits/"
productionurl = "https://bits.drc.gov.bt/bits/"
uaturl = "https://bitsuat.drc.gov.bt/bits/"

driver.get(uaturl)
