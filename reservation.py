from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


import time
import slackweb
import requests
import json
import os
import settings

USC = settings.USC
USP = settings.USP
WHU = settings.WHU

class reservationClass:
    def main(self):
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        number = 0
        while number <  1000:
            wait = WebDriverWait(driver, 20)
            url = "https://yoyaku-f.koyama.co.jp/scripts/mtr1010.asp"
            driver.get(url)
            time.sleep(5) #この一行でエラー直りました

            login_element = wait.until(EC.element_to_be_clickable((By.NAME, 'login')))
            user_code_xpath     = "/html/body/div/form/table/tbody/tr[1]/td[2]/input"
            user_password_xpath = "/html/body/div/form/table/tbody/tr[2]/td[2]/input"
            driver.find_element_by_xpath(user_code_xpath).send_keys(USC)
            driver.find_element_by_xpath(user_password_xpath).send_keys(USP)

            login_element.click()  # ログインボタン

            reserve_element = wait.until(EC.element_to_be_clickable((By.NAME, 'mtr1010')))
            reserve_element.click()  # 技能予約を選択

            wait.until(EC.element_to_be_clickable((By.NAME, 'logout')))
            kushya1 = driver.find_elements_by_xpath(
                "//img[@src='ko2_kushya.gif']")

            next_display_path1 = "/html/body/div[1]/form[1]/table[1]/tbody/tr[3]/td[3]/input"
            next_display1_element = wait.until(EC.element_to_be_clickable((By.XPATH, next_display_path1)))
            next_display1_element.click()  # 次画面に遷移

            wait.until(EC.element_to_be_clickable((By.NAME, 'logout')))
            kushya2 = driver.find_elements_by_xpath(
                "//img[@src='ko2_kushya.gif']")

            next_display_path2 = "/html/body/div[1]/form[1]/table[1]/tbody/tr[3]/td[3]/input"
            next_display2_element = wait.until(EC.element_to_be_clickable((By.XPATH, next_display_path2)))
            next_display2_element.click()  # 次画面に遷移

            wait.until(EC.element_to_be_clickable((By.NAME, 'logout')))
            kushya3 = driver.find_elements_by_xpath(
                "//img[@src='ko2_kushya.gif']")

            logout_path = "/html/body/div[1]/form[2]/input"
            wait.until(EC.element_to_be_clickable((By.NAME, 'logout')))
            driver.find_element_by_xpath(logout_path).click()
            wait.until(EC.element_to_be_clickable((By.NAME, 'login')))

            empty_number = len(kushya1) + len(kushya2) + len(kushya3)
            webhook_url = WHU
            text = '現在コヤマに空きが%d件あります。急げ！' % empty_number
            if empty_number > 0:
                slack = slackweb.Slack(url=webhook_url)
                slack.notify(
                  username="PAPARU君",
                  icon_url="https://stickershop.line-scdn.net/stickershop/v1/product/1154602/LINEStorePC/main.png;compress=true",
                  text=text)
            else:
                print('空き無し')
            time.sleep(60)
            number += 1
        pass

    def shutdown_driver(self):
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.quit()
        time.sleep(10)
        pass

    def back_to_home(self):
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        url = "https://yoyaku-f.koyama.co.jp/scripts/mtr1010.asp"
        driver.get(url)
        time.sleep(10)
        pass

if __name__ == '__main__':
    while True:
        try:
            reservationClass().main()
        except TimeoutException as te: 
            reservationClass().shutdown_driver()
            reservationClass().back_to_home()
            reservationClass().main()


