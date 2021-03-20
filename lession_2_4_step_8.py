from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin


# адрес страницы
link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(log(abs(12*sin(int(x)))))

try: 
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Нажать на кнопку
    browser.find_element_by_id("book").click()
    
    # Решить появившуюся капчу для роботов, чтобы получить число с ответом
    x = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "input_value")))
    browser.find_element_by_id("answer").send_keys(calc(x.text))

    # Нажать на кнопку Submit
    browser.find_element_by_id("solve").click()

    # ответ
    print(browser.switch_to.alert.text.split())

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
