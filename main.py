from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


driver.get('https://online.deu.edu.tr/')


username_input = driver.find_element(By.ID, 'eid')
username_input.send_keys('Write Your Email')
password_input = driver.find_element(By.ID, 'pw')
password_input.send_keys('Write Your Password')


submit_button = driver.find_element(By.ID, 'submit')
submit_button.click()


driver.get('https://online.deu.edu.tr/portal/site/64ccac85-e2d4-4d4e-804e-e17d1b36e98c/tool/28ffdda7-9b6b-43a0-9387-fe70bb4d4424')


# td_element = driver.find_element(By.CLASS_NAME, 'bbb_status_joinable_available')
# link = td_element.find_element(By.TAG_NAME, 'a')
# link.click()
