from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import requests
import json
import os

import settings

USC = settings.USC
USP = settings.USP
WHU = settings.WHU

webdriver = webdriver.Chrome()
for i in range(1, 1000):
  webdriver.get("https://yoyaku-f.koyama.co.jp/scripts/mtr1010.asp")

  webdriver.find_element_by_xpath(
    "/html/body/div/form/table/tbody/tr[1]/td[2]/input").send_keys(USC)
  webdriver.find_element_by_xpath(
    "/html/body/div/form/table/tbody/tr[2]/td[2]/input").send_keys(USP)
  webdriver.find_element_by_name("login").click()
  time.sleep(2)
  webdriver.find_element_by_name("mtr1010").click()
  time.sleep(2)

  kushya1 = webdriver.find_elements_by_xpath(
    "//img[@src='ko2_kushya.gif']")

  webdriver.find_element_by_xpath(
      "/html/body/div[1]/form[1]/table[1]/tbody/tr[3]/td[3]/input").click()
  time.sleep(1)
  kushya2 = webdriver.find_elements_by_xpath(
    "//img[@src='ko2_kushya.gif']")

  webdriver.find_element_by_xpath(
      "/html/body/div[1]/form[1]/table[1]/tbody/tr[3]/td[3]/input").click()
  time.sleep(1)
  kushya3 = webdriver.find_elements_by_xpath(
      "//img[@src='ko2_kushya.gif']")

  webdriver.find_element_by_xpath(
    "/html/body/div[1]/form[2]/input").click()
  

  empty_number = len(kushya1) + len(kushya2) + len(kushya3)
  webhook_url = WHU
  text = '現在コヤマに空きが%d件あります。急げ！' % empty_number

  if empty_number > 0:
    requests.post(webhook_url, data=json.dumps({
        "username": "PAPARU君",
        "icon_url": "https://stickershop.line-scdn.net/stickershop/v1/product/1154602/LINEStorePC/main.png;compress=true",
        "text": text
    }))
  time.sleep(120) #だいたい2分半間隔にしよう

