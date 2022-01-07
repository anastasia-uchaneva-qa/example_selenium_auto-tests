from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

link = "https://test-education.cirrusplatform.com/#saml"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    credentials_link = browser.find_element_by_css_selector(".form-group a")
    credentials_link.click()
    username = browser.find_element_by_id("login")
    username.send_keys("anastasiauch")
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value("en-GB")
    password = browser.find_element_by_id("view_password")
    password.send_keys("12345")
    
    button = browser.find_element_by_css_selector(".submitButton")
    button.click()
    time.sleep(2)
    author_link = browser.find_element(By.XPATH, "//a[@title = 'Author']")
    author_link.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла