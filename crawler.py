import requests
from bs4 import BeautifulSoup


# 카테고리 리스트 출력
def crawl_url(sid2, date, page):
    data = []
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=" + str(sid2) + "&date=" + str(date) + "&page=" + str(page)
    
    req = requests.get(url)
    status = req.status_code
    if status!= 200:
        return print("status code :", status)

    print("url fetched!")
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    urlList = soup.find('div', {'class': 'list_body newsflash_body'})
    liList = urlList.find_all('li')
    for li in liList:
        aTag = li.find('a', href=True)
        url = aTag.attrs['href']
        press = li.find('span', {'class': 'writing'})
        press = press.text
        data.append({'press': press, 'url': url})
    
    print("returned url datas!")
    return data
