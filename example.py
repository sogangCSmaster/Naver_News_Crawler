from crawler import crawl_url, crawl_news

# 금융(259) 카테고리 2019년 07월 03일 1페이지 url 수집
urlDatas = crawl_url(259, '20190703', 1)
print('작성 언론사 : ' + urlDatas[1]['press'])
print('url : ' + urlDatas[1]['url'])
url = urlDatas[1]['url']

contentData = crawl_news(url)
print(contentData['title'])
print(contentData['publishedAt'])
print(contentData['thumbnail'])