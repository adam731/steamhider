from selenium import webdriver
import time
import random
import string

letters = string.ascii_lowercase
name = (''.join(random.choice(letters) for i in range(10)))


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

print("Welcome to Adam's name changer")
print('To stop the script from running just close out the program')
print('If you select a low amount of seconds it could create errors with steam server.')
print('Any issues please contact me on discord at Adem#6377')

def steam():
    username = input('Enter username for steam account: ')
    password = input('Enter password for steam account: ')
    driver.get('https://steamcommunity.com/login/home/?goto=')
    driver.find_element_by_id("input_username").send_keys(username)
    driver.find_element_by_id("input_password").send_keys(password)
    driver.find_element_by_class_name('login_btn').click()
    print('30 seconds to enter your AUTH code')
    time.sleep(30)
    driver.find_element_by_class_name('btn_medium').click()
    driver.find_element_by_class_name('DialogTextInputBase').clear()
    driver.find_element_by_class_name('DialogTextInputBase').send_keys('test')
    driver.find_element_by_xpath('//*[@id="application_root"]/div[2]/div[2]/form/div[7]/button[1]').click()
steam()


def name_change_loop():

    f_name = ('John', 'Andy', 'Joe', 'Jaden', 'Leanna', 'Kyan', 'Jaylee', 'Owen', 'Ellis','Kevin','Jared')
    l_name = ('Johnson', 'Smith', 'Williams', 'Sanai', 'Hammond', 'Riggs', 'Bonilla', 'Graham','Lewis','Pittman')
    completed_name = " ".join(random.choice(f_name) + " " + random.choice(l_name) for _ in range(1))


    driver.back()
    driver.find_element_by_class_name('btn_medium').click()
    driver.find_element_by_class_name('DialogTextInputBase').clear()
    driver.find_element_by_class_name('DialogTextInputBase').send_keys(completed_name)
    driver.find_element_by_xpath('//*[@id="application_root"]/div[2]/div[2]/form/div[7]/button[1]').click()
    print('your changed name is ',completed_name)


wait_time = float(input('Enter how many seconds for your name change: '))

while True:
  name_change_loop()
  time.sleep(wait_time)
