from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

url = "https://www.q-net.or.kr/man001.do?gSite=Q"

driver.get(url)

btn_login = driver.find_element(By.CLASS_NAME , "btn_login")