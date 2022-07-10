from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# data = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(data.text)
# all_portals = driver.find_element(by=By.CSS_SELECTOR, value="#ca-viewsource a")
# all_portals.click()

# find_element_by_name = driver.find_element(by=By.NAME, value="search")
# find_element_by_name.send_keys("python")
# find_element_by_name.send_keys(Keys.ENTER)
# driver.quit()

driver.get("http://secure-retreat-92358.herokuapp.com/")
f_name = driver.find_element(by=By.NAME, value="fName")
f_name.send_keys("Hritik")

l_name = driver.find_element(by=By.NAME, value="lName")
l_name.send_keys("Solanki")

email = driver.find_element(by=By.NAME, value="email")
email.send_keys("hritiksolanki@gmail.com")

submit = driver.find_element(by=By.CLASS_NAME, value="btn")
submit.click()