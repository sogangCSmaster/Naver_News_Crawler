from bs4 import BeautifulSoup
import requests
import urllib.parse as urlparse
import json

url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=025&aid=0002934572#"
req = requests.get(url)

html = req.text
soup = BeautifulSoup(html, 'html.parser')
print(soup)

test = soup.find('span', {'class': 'lo_txt'})
print(test)
