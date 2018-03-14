# -*- coding: utf-8 -*-

#requestsモジュールをインポート
import requests
#読み込みたいURLの指定
url = "https://www.jp.playstation.com/account/#friend"
#指定されたURLを読み込む
get_html = requests.get(url)
print get_html.text
print type(get_html.text)

test_string = "こんにちは"
print type( test_string )
print test_string
test_uni = test_string.decode( 'utf-8' )
print type(test_uni)
print test_uni