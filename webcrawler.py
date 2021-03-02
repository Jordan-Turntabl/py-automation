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
        driver.implicitly_wait(10)
        return
    else:
        print('Here.......')
        new_tab()
        driver.get(url)
        driver.implicitly_wait(10)
    return


def new_tab():
    driver.execute_script("window.open('');")
    # driver.switch_to.window(driver.window_handles[1])


open_link(l1)
if driver.title != '':
    print('Running l1: Semlr')
    p = open("p.txt", "r")
    txtBoxes = driver.find_elements_by_css_selector("input")
    txtBoxes[0].send_keys("jordan.adjei@turntabl.io")
    txtBoxes[1].send_keys(p.read() + Keys.ENTER)
    p.close()
    print("Done!")
else:
    print("Something happened along the way!!")

open_link(l2)
if driver.title != '':
    print('Running l2: Bob')
    driver.find_element(By.CLASS_NAME, "googleIcon__3ihFp").click()
