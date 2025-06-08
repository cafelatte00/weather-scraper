import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import os

try:
    url = 'https://tenki.jp/forecast/9/43/8210/40130/'
    response = requests.get(url)
    response.raise_for_status() # HTTPエラーが発生した場合は例外を投げる

    soup = BeautifulSoup(response.text, 'html.parser')

    # 「今日の天気」セクションを取得
    today_section = soup.select_one('section.today-weather')
    if not today_section:
        print("今日の天気情報が見つかりませんでした。")
    else:
        # 今日の天気
        weather_text = ''
        weather = today_section.select_one('p.weather-telop')
        if weather:
            weather_text = weather.text.strip()
            print('今日の天気：', weather_text)
        else:
            print('天気情報が見つかりませんでした。')

        # 最高気温
        high_temp = ''
        high_temp_tag = today_section.select_one('dd.high-temp.temp > span.value')
        if high_temp_tag:
            high_temp = high_temp_tag.text.strip()
            print(f"最高気温： {high_temp_tag.text }℃")

        # 最低気温
        low_temp = ''
        low_temp_tag = today_section.select_one('dd.low-temp.temp > span.value')
        if low_temp_tag:
            low_temp = low_temp_tag.text.strip()
            print(f"最低気温： {low_temp }℃")

        # 降水確率
        rain_probs = [''] * 4
        rain_row = today_section.select_one('tr.rain-probability')
        if rain_row:
            rain_cells = rain_row.find_all('td')
            time_ranges = ['00-06', '06-12', '12-18', '18-24']
            print("降水確率：")
            for i, cell in enumerate(rain_cells):
                rain_probs[i] = cell.get_text(strip=True)
                print(f"{time_ranges[i]}: {rain_probs[i]}")
        else:
            print("降水確率情報が見つかりませんでした。")

        # CSV保存
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        today = datetime.now().strftime('%Y-%m-%d')
        filename = f"weather_{today}.csv"
        file_exists = os.path.isfile(filename)

        # データ保存
        row = [now, weather_text, high_temp, low_temp] + rain_probs

        with open(filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                header = ['取得日時', '天気', '最高気温', '最低気温', '00-06', '06-12', '12-18', '18-24']
                writer.writerow(header)
            writer.writerow(row)

        print(f"{now}: データを {filename} に保存しました。")
except requests.exceptions.RequestException as e:
    print(f"エラー： {e}")
else:
    print("正常に処理されました。")
