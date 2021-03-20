from selenium import webdriver
from PIL import Image
from io import BytesIO
import telebot

token = '1028506821:AAEh3n2vSObHkSuL4bsal5xlXcvUtDjma4o'

myBot = telebot.TeleBot(token)

Chr = webdriver.Chrome()
Chr.get('https://www.coindesk.com/')

# now that we have the preliminary stuff out of the way time to get that image :D
#element = Chr.find_element_by_id('hlogo') # find part of the page you want image of
#location = element.location
#size = element.size
png = Chr.get_screenshot_as_png() # saves screenshot of entire page
Chr.quit()

im = Image.open(BytesIO(png)) # uses PIL library to open image in memory

left = 5
top = 5
right = 240
bottom = 130

im = im.crop((left, top, right, bottom)) # defines crop points
im.save('coin.png') # saves new cropped image

text = 'blablabla' 
myBot.send_message(658063845, f'{text}\n{im}')

#myBot.send_photo(658063845, im)