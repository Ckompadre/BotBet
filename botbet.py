# Import library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Greeting
print("Приветствую!")
print("Программа разработана для автоматических ставок на сайте csgetto.win")
print("Программу разратотал: Ckompadre")

# Variables
bet = int(input("\nВведите величину ставки: "))
print("Выберите режим работы:")
print("1. Бесконечно (пока не закроете программу или окно браузера)")
print("2. Количественно (столько, сколько зохотите раз)")
user_input = int(input("Ответ: "))
if user_input == 2:
    numbet = int(input("Введите количестко повторений: "))
    numbet += 1

# Select color  
print("\nНа что ставим?")
print("1. Красное")
print("2. Чёрное")
print("3. Зелёное")
print("После ответа - бот начнёт свою работу")
color = int(input("Ответ: "))

print("\nБот начнет работу через 5 секунд ...")
time.sleep(5)
driver = webdriver.Chrome()

# Functions
def BotClickButtom():
    if color == 1:
        btn = driver.find_element_by_class_name('red')
        btn.click()
    elif color == 2:
        btn = driver.find_element_by_class_name('black')
        btn.click()
    elif color == 3:
        btn = driver.find_element_by_class_name('green')
        btn.click()

def BotActions():
    print("Настраиваю драйвер Chrome ...")
    print("Перехожу на сайт csgetto.win ...")
    driver.get("https://csgetto.win/")

    print("Закрываю всплывающий баннер ...")
    btn_close = driver.find_element_by_class_name('modal-start-cross')
    btn_close.click()

    print("Ввожу сумму ставки ...")
    betnum = driver.find_element_by_id("doubleInputBet")
    betnum.send_keys(bet)

    print("Запускаю ставку в игру ...")
    i = 1
    if user_input == 1:
        while True:
            print("Делаю " , i , " ставку")
            BotClickButtom()
            i += 1
            time.sleep(40)
    else:
        while i < numbet:
            print("Делаю " , i , " ставку")
            BotClickButtom()
            i += 1
            time.sleep(40)
        print("Бот выполнил задачу")
        
# Start bot            
BotActions()
