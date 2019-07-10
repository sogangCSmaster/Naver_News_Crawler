from crawler import crawl_url, crawl_news

# 금융(259) 카테고리 2019년 07월 03일 1페이지 url 수집
urlDatas = crawl_url(259, '20190701', 1)
print('작성 언론사 : ' + urlDatas[1]['press'])
print('url : ' + urlDatas[1]['url'])
url = urlDatas[3]['url']

newsData = crawl_news(url)

# 뉴스 제목
title = newsData['title']
print(title)
print("\n")

# 출판 날짜
publishedAt = newsData['publishedAt']

# 썸네일 URL
thumbnail = newsData['thumbnail']

# 뉴스 본문
content = newsData['content']

# 네이버 뉴스 요약문 베타
summary = newsData['summary']

# 좋아요, 훈훈해요, 슬퍼요, 화나요, 후속기사 원해요
like = newsData['like']
warm = newsData['warm']
sad = newsData['sad']
angry = newsData['angry']
warm = newsData['warm']

print(summary)
print("\n")
print(like, warm, sad, angry, warm)