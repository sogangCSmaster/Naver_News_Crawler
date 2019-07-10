# Naver_News_Crawler
파이썬 네이버 뉴스 크롤러

## Todo
1. 카테고리
2. 저자
3. 언론사
4. 출판?날짜
5. 본문
6. 요악문
7. 많이 본 성별
8. 많이 본 나이대



## 네이버 뉴스 URL 분석

예시 : https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=310&sid1=101&date=20190707
1. mode : LSD와 LS2D가 있는데, LS2D로 해야 날짜기반 검색이 가능
2. sid1 : 대분류 카테고리 (정치, 경제, 사회, 생활/문화, 세계, IT/과학)
3. sid2 : 소분류 카테고리
4. date : 발행날짜 (포맷 : YYYYMMDD)