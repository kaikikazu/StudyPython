# -*- coding: utf-8 -*-

#requestsモジュールをインポート
import requests
from bs4 import BeautifulSoup

html_text = open('sample.html','r')
soup = BeautifulSoup(html_text.read(),'html.parser')

print "---------------first_link_output---------------"
print soup.find("a")

link = soup.find_all("a")

print "---------------link_list_output---------------"
print link

print "---------------all_link_output---------------"
for i in link:
	print i

print "---------------all_link_text_output---------------"
for i in range(len(link)):
	print link[i].text

print "---------------title_text_output---------------"
print soup.title.text