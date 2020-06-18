# このアプリについて :car:

コヤマドライビングスクールの予約に空きがあるかどうか確認し
空きがある場合Slackの通知としてお知らせするアプリケーションです。



# 使い方 :book:

ローカルにPython 3の環境があることが前提となります。

1. `$ pip install dotenv selenium slackweb`

2. [こちら](https://sites.google.com/a/chromium.org/chromedriver/downloads)から自分のchromeと同じバージョンのdriverをダウンロードしてください

3. `$ brew cask install chromedriver`


4. `koyama_resevation/` 内で `.env` ファイルを作成してください。
`$ touch .env`

5. 作成した `.env` ファイルに以下のような記述をしてください。
```(.env)
USER_CODE=あなたの教習生コード
USER_PASSWORD=あなたのコヤマ予約サイトのパスワード

WEBHOOK_URL=通知を送りたいSlackのwebhook_url
```

webhook_urlの取得に関しては[こちら](https://qiita.com/vmmhypervisor/items/18c99624a84df8b31008)を参考にしてください。

6. `settings.py` を動かしてローカルに `.env` で設定した変数を反映させます。
`$ python3 settings.py`

7. `reservation.py` を動かします。
`$ python3 reservation.py`

8. Slack に通知が来たら予約を確保しに行きましょう！！ :+1:
