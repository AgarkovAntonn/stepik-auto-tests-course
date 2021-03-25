from selenium import webdriver
import time
import unittest

class test_my_class_name(unittest.TestCase):
	def test_url1(self):
		try: 
			link = "http://suninjuly.github.io/registration1.html"
			browser = webdriver.Chrome()
			browser.get(link)

			# Ваш код, который заполняет обязательные поля
			# First Name Field
			first_name = browser.find_element_by_css_selector('.first_block input.first')
			first_name.send_keys("First name")

			# Second Name Field
			second_name = browser.find_element_by_css_selector('.first_block input.second')
			second_name.send_keys("Second name")

			# Email Name Field
			email = browser.find_element_by_css_selector('.first_block input.third')
			email.send_keys("Email")

			# Отправляем заполненную форму
			button = browser.find_element_by_css_selector("button.btn")
			button.click()

			# Проверяем, что смогли зарегистрироваться
			# ждем загрузки страницы
			time.sleep(1)

			# находим элемент, содержащий текст
			welcome_text_elt = browser.find_element_by_tag_name("h1")
			# записываем в переменную welcome_text текст из элемента welcome_text_elt
			welcome_text = welcome_text_elt.text

			# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
			self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "URL1. Not Regitered")
			#assert "Congratulations! You have successfully registered!" == welcome_text

		finally:
			# ожидание чтобы визуально оценить результаты прохождения скрипта
			time.sleep(1)
			# закрываем браузер после всех манипуляций
			browser.quit()
			
		
        
	def test_url2(self):
		try: 
			link = "http://suninjuly.github.io/registration2.html"
			browser = webdriver.Chrome()
			browser.get(link)

			# Ваш код, который заполняет обязательные поля
			# First Name Field
			first_name = browser.find_element_by_css_selector('.first_block input.first')
			first_name.send_keys("First name")

			# Second Name Field
			second_name = browser.find_element_by_css_selector('.first_block input.second')
			second_name.send_keys("Second name")

			# Email Name Field
			email = browser.find_element_by_css_selector('.first_block input.third')
			email.send_keys("Email")

			# Отправляем заполненную форму
			button = browser.find_element_by_css_selector("button.btn")
			button.click()

			# Проверяем, что смогли зарегистрироваться
			# ждем загрузки страницы
			time.sleep(1)

			# находим элемент, содержащий текст
			welcome_text_elt = browser.find_element_by_tag_name("h1")
			# записываем в переменную welcome_text текст из элемента welcome_text_elt
			welcome_text = welcome_text_elt.text

			# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
			self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "URL2. Not Regitered")
			#assert "Congratulations! You have successfully registered!" == welcome_text

		finally:
			# ожидание чтобы визуально оценить результаты прохождения скрипта
			time.sleep(1)
			# закрываем браузер после всех манипуляций
			browser.quit()        

if __name__ == "__main__":   
	unittest.main()
	


# не забываем оставить пустую строку в конце файла