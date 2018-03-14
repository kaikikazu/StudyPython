# -*- coding: utf-8 -*-

#requestsモジュールをインポート
import requests
from bs4 import BeautifulSoup

url = "http://ourmaps.jp"
#指定されたURLを読み込む
html_text = requests.get(url)
soup = BeautifulSoup(html_text.text,'html.parser')

print soup.title.text

test = content = soup.find(id = "Content3TopTextBox")
print test

#-----------Let's try Web scrayping!!-----------