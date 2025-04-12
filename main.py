from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc

driver = uc.Chrome()

driver.get("https://google.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("dai hoc mo" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "TRƯỜNG ĐẠI HỌC MỞ TP HCM"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "TRƯỜNG ĐẠI HỌC MỞ TP HCM")
link.click()

link = driver.find_element(By.PARTIAL_LINK_TEXT, "LỊCH THI")
link.click()

time.sleep(10)

driver.quit()
