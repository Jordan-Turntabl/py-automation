# Log in to semlr, then bob, then try and open lecture link
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

l1 = "https://turntabl.semlr.com/login/signin?app=hub"
l2 = "https://app.hibob.com/time-attendance/my-attendance"

driver = webdriver.Chrome('C:\\Users\\TURNTABL\\AppData\\Local\\Programs\\Python\\Python39\\chromedriver.exe')


def open_link(url):
    if url.endswith("hub"):
        driver.get(url)
        wait(15)
        return
    else:
        driver.get(url)
        wait(15)
    return


def new_tab():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])


def wait(s):
    driver.implicitly_wait(s)


open_link(l1)
if driver.title != '':
    print('Running l1: Semlr')
    p = open("p.txt", "r")
    txtBoxes = driver.find_elements_by_css_selector("input")
    txtBoxes[0].send_keys("jordan.adjei@turntabl.io")
    txtBoxes[1].send_keys(p.read() + Keys.ENTER)
    p.close()
    wait(10)
    print("Done!")
    new_tab()
else:
    print("Something happened along the way!!")

open_link(l2)
if driver.title != '':
    print('Running l2: Bob')
    wait(10)
    driver.find_element(By.CLASS_NAME, "googleIcon__3ihFp").click()
    driver.find_element(By.ID, "identifierId").send_keys("jordan.adjei@turntabl.io" + Keys.ENTER)
    wait(7)
    driver.find_element(By.NAME, "password").send_keys("" + Keys.ENTER)
    wait(30)
    
    try:
        elements = driver.find_elements(By.TAG_NAME, 'button')
        # print(elements[3].text)
        elements[3].click()
    finally:
        print("Done here!")
