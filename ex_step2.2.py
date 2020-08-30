from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element_by_id("num1")
    x = num1.text
    
    num2 = browser.find_element_by_id("num2")
    y = num2.text
    
    sum_numbers = int(x) + int(y)
    
    select = Select(browser.find_element_by_tag_name("select"))
    answer = select.select_by_value(str(sum_numbers)) # ищем элемент с правильным ответом
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
