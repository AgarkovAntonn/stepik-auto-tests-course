from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# адрес страницы
link = "http://suninjuly.github.io/get_attribute.html"

try: 
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    treasure_image = browser.find_element_by_id("treasure")
    
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.    
    x = treasure_image.get_attribute("valuex")
    
    # Посчитать математическую функцию от x 
    y = calc(x)

    # Ввести ответ в текстовое поле.
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Отметить checkbox "I'm the robot"
    checkbox_robot = browser.find_element_by_id("robotCheckbox")
    checkbox_robot.click()

    # Выбрать radiobutton "Robots rule!"
    radiobutton_robot = browser.find_element_by_id("robotsRule")
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
