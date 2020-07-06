from configparser import ConfigParser
from collections import namedtuple
from bs4 import BeautifulSoup
import requests


News = namedtuple('News', ['title', 'link', 'date'])


class BbuNews(object):
    """获取蚌埠学院综合新闻的类"""

    def __init__(self) -> None:
        """初始化：读取配置文件"""
        self.cfg = ConfigParser()
        self.cfg.read('config.ini')
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Host': 'www.bbc.edu.cn',
            'Referer': 'http://www.bbc.edu.cn/'
            }
    
    def getNews(self, pageNum: int = 1) -> list:
        """获取新闻"""
        _url = self.cfg.get('bbu', 'start') + str(pageNum) + self.cfg.get('bbu', 'start_end')
        response = requests.get(_url, headers=self.headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        td = soup.find_all('td', height='24')
        news_list = []
        for tr in td:
            title = tr.td.a.get_text()
            date = tr.div.get_text()
            link = tr.td.a['href']
            full_link = self.cfg.get('bbu', 'base') + link
            n = News(title=title, link=full_link, date=date)
            news_list.append(n)
        return news_list
