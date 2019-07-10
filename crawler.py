import requests
from bs4 import BeautifulSoup


def crawl_url(sid2, date, page):
    data = []
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=" + str(sid2) + "&date=" + str(date) + "&page=" + str(page)
    
    req = requests.get(url)
    status = req.status_code
    if status!= 200:
        return print("Error, status code :", status)

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

def crawl_news(url):
    data = {}
    req = requests.get(url)
    status = req.status_code
    if status!= 200:
        return print("Error, status code :", status)

    print("url fetched!")
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    
    for useless in soup(['script', 'style']):
        useless.extract()

    
    thumbnail = soup.find('meta', property='og:image')
    thumbnail = thumbnail['content']
    title = soup.find('meta', property='og:title')
    title = title['content']
    publishedAt = soup.find('span', {'class': 't11'})
    publishedAt = publishedAt.text
    content = soup.find('div', id='articleBodyContents')


    for imgTag in content.find_all('span', {'class': 'end_photo_org'}):
        imgTag.decompose()
    for aTag in content.find_all('a'):
        aTag.decompose()
    
    content = content.text.strip()
    data['title'] = title
    data['content'] = content
    data['thumbnail'] = thumbnail
    data['publishedAt'] = publishedAt


    return data