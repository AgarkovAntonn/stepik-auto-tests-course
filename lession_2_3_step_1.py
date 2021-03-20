from selenium import webdriver
import time
from math import log, sin


# адрес страницы
link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(log(abs(12*sin(int(x)))))

try: 
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    browser.find_element_by_css_selector("button.btn").click()

    # Принять confirm
    browser.switch_to.alert.accept()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))

    # Нажать на кнопку Submit
    browser.find_element_by_css_selector("button.btn").click()

    # ответ
    print(browser.switch_to.alert.text.split())

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
