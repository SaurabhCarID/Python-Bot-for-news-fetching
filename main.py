import driverdata
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium_ai import ElementFinder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import fincen
import occ
import sebi
import sec
import bis

global driver
driverdata.driver.maximize_window()


try:
    fincen.fincen()
except Exception as e:
    print(e)


try:
    occ.occ()
except Exception as e:
    print(e)

try:
    sebi.sebi()
except Exception as e:
    print(e)

try:
    sec.sec()
except Exception as e:
    print(e)

try:
    bis.bis()
except Exception as e:
    print(e)


driverdata.driver.quit()
