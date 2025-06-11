# 天気情報スクレイピングツール（Python）

## 概要

福岡県（福岡市）の天気情報を [tenki.jp](https://tenki.jp/) からスクレイピングし、  
当日の天気・気温・降水確率を取得してCSVファイルに保存します。

- スクレイピング先： https://tenki.jp/forecast/9/43/8210/40130/
- CSVファイル： `weather_YYYY-MM-DD.csv` という形式で作成されます

---

## 使用技術

- Python 3
- requests
- BeautifulSoup4

---
## できること
実行すると、以下の情報が取得されます：

天気（例：晴れ、曇り）

最高気温・最低気温（℃）

時間帯ごとの降水確率（00-06, 06-12, 12-18, 18-24）

実行結果は、当日の日付を含むCSVファイルに追記されます（例：weather_2025-06-09.csv）。

---
## 出力例（CSV）
| 取得日時                | 天気 | 最高気温 | 最低気温 | 00-06 | 06-12 | 12-18 | 18-24 |
| ------------------- | -- | ---- | ---- | ----- | ----- | ----- | ----- |
| 2025-06-09 12:34:56 | 晴れ | 30   | 22   | 10%   | 20%   | 10%   | 0%    |



## 定期実行　cron（クーロン）の設定

毎日決まった時間にスクリプトを自動実行するために、以下のようなcron（クーロン）ジョブを設定しています。

```bash
0 1 * * * /Users/yourusername/python_scraping/run_scraping.sh >> /Users/yourusername/python_scraping/log.txt 2>&1
30 6 * * * /Users/yourusername/python_scraping/run_scraping.sh >> /Users/yourusername/python_scraping/log.txt 2>&1
```

- run_scraping.sh が仮想環境の有効化と scraping.py の実行を行います。
- 実行結果やエラーメッセージは log.txt に保存されます。
- ユーザー名が環境ごとに異なるため、適宜パスを書き換えてください。