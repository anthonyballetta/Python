from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time;

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:/Users/Aballetta20/AppData/Local/Google/Chrome/User Data/Default") #Path to your chrome profile
options.add_argument("--start-maximized")
options.add_argument("disable-infobars"); 
w = webdriver.Chrome(executable_path="C:/Users/Aballetta20/Desktop/Python/chromedriver.exe", chrome_options=options)

w.get('https://www.paycomonline.net/v4/ee/ee-login.php')
username = w.find_element_by_id("txtlogin")
password = w.find_element_by_id("txtpass")
ssn = w.find_element_by_id("userpinid")

username.send_keys("example@example.com")

password.send_keys("password")

ssn.send_keys("1337")

loginbutton = w.find_element_by_id("btnSubmit").click()

time = w.find_element_by_id("arrowtime").click()
webtime = w.find_element_by_id("liNav1").click()