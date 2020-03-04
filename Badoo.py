from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


def hz(login, password, count):
    options = Options()
    options.binary_location = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    driver = webdriver.Chrome(chrome_options= options, executable_path=r'C:\\Users\\Melissa\\Desktop\\Tinder_Badoo\\chromedriver.exe')
    driver.get('https://badoo.com/signin/?f=top')
    login_field = driver.find_element_by_css_selector('.js-signin-login')
    login_field.send_keys('')
    pasword_field = driver.find_element_by_css_selector('.js-signin-password')
    pasword_field.send_keys('')
    btn_log = driver.find_element_by_css_selector('.btn--block')
    btn_log.click()
    time.sleep(10)
    try:
        like_btn = driver.find_element_by_css_selector('.js-profile-header-vote-yes')
        like_btn.click()
        time.sleep(2)
        deny_btn = driver.find_element_by_css_selector('.js-chrome-pushes-deny')
        deny_btn.click()
        time.sleep(2)
    except:
        driver.quit()

    for i in range(1000):
        try:
            like_btn = driver.find_element_by_css_selector('.js-profile-header-vote-yes')
            like_btn.click()
            time.sleep(0.5)
        except:
            try:
                deny1_btn = driver.find_element_by_css_selector('.js-ovl-close')
                deny1_btn.click()
                time.sleep(0.5)
            except:
                time.sleep(100)
                break

    driver.quit()


def main():
    login = str(input('Введи логин\n'))
    password = str(input('Введи пароль\n'))
    count = int(input('Введи сколько лайкать\n'))
    hz(login, password, count)


if __name__ == '__main__':
    main()
