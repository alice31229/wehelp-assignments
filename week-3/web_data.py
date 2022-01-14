# standard library: https://docs.python.org/zh-tw/3/library/index.html

import csv
import json
from urllib.request import urlopen
url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
response = urlopen(url)
data = json.loads(response.read())
data = data['result']['results']


# 開啟輸出的 CSV 檔案
with open('data.csv', 'w', newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)

    # 景點名稱，區域，經度，緯度，第一張圖檔網址
    for d in data:
        photo=[p for p in d['file'].split('https:')]
        main_photo='https:'+photo[1]
        main_photo=main_photo.replace('\\','')

        # 寫入幾列資料
        writer.writerow([d['stitle'], d['address'][5:8], d['longitude'], d['latitude'], main_photo])

