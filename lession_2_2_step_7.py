from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os 

# адрес страницы
link = "http://SunInJuly.github.io/execute_script.html"

# получаем путь к директории текущего исполняемого файла 
current_dir = os.path.abspath(os.path.dirname(__file__))

# добавляем к этому пути имя файла 
file_path = os.path.join(current_dir, 'file.txt')

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    x = browser.find_element_by_id("input_value").text

    # Посчитать математическую функцию от x.
    result = calc(x)

    # Ввести ответ в текстовое поле.
    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)

    # Проскроллить страницу вниз
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    # Выбрать checkbox "I'm the robot"
    browser.find_element_by_id("robotCheckbox").click()

    # Переключить radiobutton "Robots rule!"
    browser.find_element_by_id("robotsRule").click()

    # Нажать на кнопку Submit.
    button.click()

    # 28.856294293545425
    print(browser.switch_to.alert.text.split())

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
