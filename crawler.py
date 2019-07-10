import requests
from bs4 import BeautifulSoup
import urllib.parse as urlparse
import json

def crawl_url(sid2, date, page):
    data = []
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=" + str(sid2) + "&date=" + str(date) + "&page=" + str(page)
    
    req = requests.get(url)
    status = req.status_code
    if status!= 200:
        return print("Error, status code :", status)

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
    
    return data

def crawl_news(url):
    data = {}
    req = requests.get(url)
    status = req.status_code
    if status!= 200:
        return print("Error, status code :", status)


    parsed = urlparse.urlparse(url)
    oid = urlparse.parse_qs(parsed.query)['oid'][0]
    aid = urlparse.parse_qs(parsed.query)['aid'][0]

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

    sentimentAPI = "https://news.like.naver.com/v1/search/contents?q=NEWS[ne_{}_{}]".format(oid, aid)
    print('sentimentAPI:', sentimentAPI)
    summaryAPI = "https://tts.news.naver.com/article/{}/{}/summary".format(oid, aid)
    print('summaryAPI:', summaryAPI)

    sentimentJson = requests.get(sentimentAPI).json()
    summaryJson = requests.get(summaryAPI).json()

    like = 0
    warm = 0
    sad = 0
    angry = 0
    want = 0
    reactions = sentimentJson['contents'][0]['reactions']
    for reaction in reactions:
        if reaction['reactionType']=='like':
            like = reaction['count']
        elif reaction['reactionType']=='warm':
            warm = reaction['count']
        elif reaction['reactionType']=='sad':
            sad = reaction['count']
        elif reaction['reactionType']=='angry':
            angry = reaction['count']
        elif reaction['reactionType']=='want':
            want = reaction['count']

    summary = summaryJson['summary']
    summary = summary.replace('<br/>', '\n')
    

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
    data['summary'] = summary
    data['like'] = like
    data['warm'] = warm
    data['sad'] = sad
    data['angry'] = angry
    data['want'] = want

    return data