# -*- coding: utf-8 -*-

#requestsモジュールをインポート
import requests
#BeautifulSoupモジュールをインポート
from bs4 import BeautifulSoup

url = "http://ourmaps.jp"
#指定されたURLを読み込む
html_text = requests.get(url)
soup = BeautifulSoup(html_text.text,'html.parser')

print soup.find("html")