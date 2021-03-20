from selenium import webdriver
import time
import os 

# адрес страницы
link = "http://suninjuly.github.io/file_input.html"

# получаем путь к директории текущего исполняемого файла 
current_dir = os.path.abspath(os.path.dirname(__file__))

# добавляем к этому пути имя файла 
file_path = os.path.join(current_dir, 'file.txt')

try: 
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    first_name = browser.find_element_by_css_selector("input.form-control:nth-child(2)")
    first_name.send_keys("First")
    second_name = browser.find_element_by_css_selector("input.form-control:nth-child(4)")
    second_name.send_keys("Second")
    second_name = browser.find_element_by_css_selector("input.form-control:nth-child(6)")
    second_name.send_keys("email@test.tst")

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    File = browser.find_element_by_css_selector("#file")
    File.send_keys(file_path)

    # Нажать на кнопку Submit
    browser.find_element_by_css_selector(".btn").click()

    # ответ
    print(browser.switch_to.alert.text.split())

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
