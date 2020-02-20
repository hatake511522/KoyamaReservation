from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import requests
import json
import os
import settings

USC = settings.USC
USP = settings.USP
WHU = settings.WHU

driver = webdriver.Chrome()
for i in range(1, 1000):
  wait = WebDriverWait(driver, 20)
  url = "https://yoyaku-f.koyama.co.jp/scripts/mtr1010.asp"
  driver.get(url)
  time.sleep(3)
  
  wait.until(EC.element_to_be_clickable((By.NAME, 'login')))
  user_code_xpath = "/html/body/div/form/table/tbody/tr[1]/td[2]/input"
  user_password_xpath = "/html/body/div/form/table/tbody/tr[2]/td[2]/input"
  driver.find_element_by_xpath(user_code_xpath).send_keys(USC)
  driver.find_element_by_xpath(user_password_xpath).send_keys(USP)

  driver.find_element_by_name("login").click() #ログインボタン
  time.sleep(3)

  wait.until(EC.element_to_be_clickable((By.NAME, 'mtr1010')))
  driver.find_element_by_name("mtr1010").click() #技能予約を選択
  time.sleep(3)

  kushya1 = driver.find_elements_by_xpath(
    "//img[@src='ko2_kushya.gif']")

  next_display_path1 = "/html/body/div[1]/form[1]/table[1]/tbody/tr[3]/td[3]/input"
  wait.until(EC.element_to_be_clickable((By.XPATH, next_display_path1)))
  driver.find_element_by_xpath(next_display_path1).click() #次画面に遷移

  time.sleep(5)
  kushya2 = driver.find_elements_by_xpath(
    "//img[@src='ko2_kushya.gif']")

  next_display_path2 = "/html/body/div[1]/form[1]/table[1]/tbody/tr[3]/td[3]/input"
  wait.until(EC.element_to_be_clickable((By.XPATH, next_display_path2)))
  driver.find_element_by_xpath(next_display_path2).click() #次画面に遷移

  time.sleep(5)
  kushya3 = driver.find_elements_by_xpath(
    "//img[@src='ko2_kushya.gif']")

  logout_path = "/html/body/div[1]/form[2]/input"
  wait.until(EC.element_to_be_clickable((By.XPATH, logout_path)))
  driver.find_element_by_xpath(logout_path).click()
  time.sleep(5)
  

  empty_number = len(kushya1) + len(kushya2) + len(kushya3)
  webhook_url = WHU
  text = '現在コヤマに空きが%d件あります。急げ！' % empty_number
  if empty_number > 0:
    requests.post(webhook_url, data=json.dumps({
        "username": "PAPARU君",
        "icon_url": "https://stickershop.line-scdn.net/stickershop/v1/product/1154602/LINEStorePC/main.png;compress=true",
        "text": text
    }))
  time.sleep(180)

