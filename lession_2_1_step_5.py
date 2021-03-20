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

    # Ввести ответ в текстовое поле.
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Отметить checkbox "I'm the robot"
    checkbox_robot = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox_robot.click()

    # Выбрать radiobutton "Robots rule!"
    radiobutton_robot = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton_robot.click()

    # Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
