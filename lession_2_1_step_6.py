from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try: 
    # Открыть страницу http://suninjuly.github.io/math.html.    
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x.
    x_value = browser.find_element_by_id("input_value")
    x = x_value.text

    # Посчитать математическую функцию от x 
    y = calc(x)

    # Найдём элемент People rule
    people_radio = browser.find_element_by_id("peopleRule")

    # Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:
    people_checked = people_radio.get_attribute("checked")
    print("Value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    
    # Найдём элемент robotsRule и проверим значение его атрибута "checked"
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("Value of robots radio: ", robots_checked)
    assert robots_checked is None

    # Найдём и проверим аттрибут "disabled" у кнопки submit
    button_submit = browser.find_element_by_css_selector("button.btn")
    button_disabled = button_submit.get_attribute("disabled")
    print("Is button submit disabled: ", button_disabled)

    # Прорим аттрибут "disabled" у кнопки submit спустя 10 секунд
    time.sleep(10)
    button_disabled = button_submit.get_attribute("disabled")
    print("Is button submit disabled after 10 seconds: ", button_disabled)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
