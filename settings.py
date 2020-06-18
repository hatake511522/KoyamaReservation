# coding: utf-8
# 実行すると .env ファイルに期日した認証情報を環境変数へ記述してくれる
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USC = os.environ.get("USER_CODE")
USP = os.environ.get("USER_PASSWORD")
WHU = os.environ.get("WEBHOOK_URL")

#NOTE: 直接 .env から変数を取得できないのか
