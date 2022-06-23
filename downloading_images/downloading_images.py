import pandas as pd
import requests

df = pd.read_excel('./telegrams_to_download.xlsx')

"""
Файлы в нашей базе данных должны быть названы определённым образом - по ID (например, tg00001).
В рамках одного ID может быть несколько изображений: лицевая и обратная сторона телеграммы, несколько сторон телеграммы-открытки и др.
В таком случае название файла с лицевой стороной будет tg00001-1, а с обратной - tg00001-2.
"""

for index, row in df.iterrows():
  if row["Ссылка"] == "[]":
    continue
  links = row["Ссылка"].strip("\[\]").split(",")
  for i, link in enumerate(links):
    url = link.strip("\' ")
    r = requests.get(url, allow_redirects=True)
    filename = ''
    filepath = './telegram_images/'
    filename = f'{row["ID"]}-{i+1}.jpg' if len(links) > 1 else f'{row["ID"]}.jpg'
    with open(filepath + filename, 'wb') as f:
      f.write(r.content)