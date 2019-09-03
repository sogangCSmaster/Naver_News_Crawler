from crawler import crawl_url, crawl_news
import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


crawledUrl = []
categoryList = [264, 265, 268, 266, 267, 269, 259, 258, 261, 771, 260, 262, 310, 263, 249, 250, 251, 254, 252, '59b', 255, 256, 276, 257, 241, 239, 240, 237, 238, 376, 242, 243, 244, 248, 245, 231, 232, 233, 234, 322, 731, 226, 227, 230, 732, 283, 229, 228]

for category in categoryList:
    startDate = 20190601
    endDate = 20190602
    page = 1
    crawledUrl = []
    while True:
        if startDate == endDate:
            break
        urlDatas = crawl_url(category, str(startDate), page)

        for urlData in urlDatas:
            ID = str(startDate) + randomString()
            try:
                url = urlData['url']
                if url in crawledUrl:
                    page = 20
                    break
                else:
                    crawledUrl.append(url)
                    newsData = crawl_news(url)
                    title = newsData['title']
                    content = newsData['content']
                    like = newsData['like']
                    angry = newsData['angry']
                    file_name = "./dataset/" + str(category) + "/" + str(ID) + ".txt"
                    f = open(file_name, 'w')
                    content = title + "\n"  + content
                    f.write(content)
                    f.close()
                    if like - angry > 10:
                        file_name2 = "./dataset/like/" + str(ID) + ".txt"
                        f = open(file_name2, 'w')
                        f.write(content)
                        f.close()
                    elif angry - like > 10:
                        file_name2 = "./dataset/angry/" + str(ID) + ".txt"
                        f = open(file_name2, 'w')
                        f.write(content)
                        f.close()
                    else:
                        file_name2 = "./dataset/neutral/" + str(ID) + ".txt"
                        f = open(file_name2, 'w')
                        f.write(content)
                        f.close()

            except Exception as e:
                print(e)

        page += 1
        if page >= 20:
            startDate += 1
            page = 1
