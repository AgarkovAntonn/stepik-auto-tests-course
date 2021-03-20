from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

# адрес страницы
link = "http://suninjuly.github.io/selects1.html"

try: 
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать сумму заданных чисел
    summa = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)
    
    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(summa))

    # Нажать на кнопку Submit.
    browser.find_element_by_css_selector("button.btn").click()

    # 28.856294293545425
    print(browser.switch_to.alert.text.split()[-1])

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
