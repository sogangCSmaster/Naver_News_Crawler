# Naver_News_Crawler
파이썬 네이버 뉴스 크롤러

문의사항은 cs20131575@u.sogang.ac.kr 로 메일 보내주세요.

<hr />

## Todo
1. 카테고리
2. 저자
3. 언론사
4. 출판?날짜
5. 본문
6. 요악문
7. 많이 본 성별
8. 많이 본 나이대


## Sample code (Python3)
```
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
```



## 네이버 뉴스 URL 분석

예시 : https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=310&sid1=101&date=20190707&page=2

1. mode : LSD와 LS2D가 있는데, LS2D로 해야 날짜기반 검색이 가능
2. sid1 : 대분류 카테고리 (정치, 경제, 사회, 생활/문화, 세계, IT/과학)
3. sid2 : 소분류 카테고리
4. date : 발행날짜 (포맷 : YYYYMMDD)
5. mid : shm, pho 두개가 있는데 shm는 신문, pho는 포토인것 같음 pho일경우 포토뉴스
6. page : pagination

sid2가 실질적인 뉴스가 나오는 query


## 카테고리 대분류 코드 (sid1)

- 100 : 정치
- 101 : 경제
- 102 : 사회
- 103 : 생활/문화
- 104 : 세계
- 105 : IT/과학


## 소분류 카테고리 (sid2)

### 정치 (100)
- 264 : 청와대
- 265 : 국회/정당
- 268 : 북한
- 266 : 행정
- 267 : 국방/외교
- 269 : 정치일반

### 경제 (101)
- 259 : 금융
- 258 : 증권
- 261 : 산업/재계
- 771 : 중기/벤처
- 260 : 부동산
- 262 : 글로벌 경제
- 310 : 생활경제
- 263 : 경제 일반

### 사회 (102)
- 249 : 사건사고
- 250 : 교육
- 251 : 노동
- 254 : 언론
- 252 : 환경
- 59b : 인권/복지
- 255 : 식품/의료
- 256 : 지역
- 276 : 인물
- 257 : 사회 일반

### 생활/문화 (103)
- 241 : 건강정보
- 239 : 자동차/시승기
- 240 : 도로교통
- 237 : 여행/레저
- 238 : 음식/맛집
- 376 : 패션/뷰티
- 242 : 공연/전시
- 243 : 책
- 244 : 종교
- 248 : 날씨
- 245 : 생활문화 일반

### 세계 (104)
- 231 : 아시아/호주
- 232 : 미국/중남미
- 233 : 유럽
- 234 : 중동/아프리카
- 322 : 세계 일반

### IT/과학 (105)
- 731 : 모바일
- 226 : 인터넷/SNS
- 227 : 통신/뉴미디어
- 230 : IT 일반
- 732 : 보안/해킹
- 283 : 컴퓨터
- 229 : 게임/리뷰
- 228 : 과학 일반



## 감성 추출 API

- 뉴스링크 : https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=025&aid=0002921348

```
https://news.like.naver.com/v1/search/contents?q=NEWS[ne_025_0002921348]

ne_025_0002921366
ne_[oid]_[aid]
```

## 요약문 API
- 뉴스링크 : https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=025&aid=0002921348
```
https://tts.news.naver.com/article/025/0002921348/summary
https://tts.news.naver.com/article/[oid]/[aid]/summary
```