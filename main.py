from BbuNews import BbuNews
from NewsModel import BbuNewsModel
import time


if __name__ == '__main__':
    totalPage = 397
    b = BbuNews()
    m = BbuNewsModel()
    for page in range(1, totalPage):
        news_list = b.getNews(pageNum=page)
        m.saveNews(news_list)
        time.sleep(1)
        tpl = "已保存蚌埠学院新闻{page}页，累计{count}条新闻.".format(page=page, count=page*14)
        print(tpl, end='\r')
    print("程序运行结束")
