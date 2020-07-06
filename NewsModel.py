from collections.abc import Iterable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, Date
from Config import MySQLURI
from BbuNews import BbuNews


Base = declarative_base()


class News(Base):
    __tablename__ = 'bbu_news'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    link = Column(String(50), nullable=False)
    date = Column(Date, nullable=False)

    def __repr__(self):
        tpl = "新闻{nid}:{title} {date}".format(nid=self.nid, title=self.title, date=self.date)
        return tpl


class BbuNewsModel(object):
    def __init__(self) -> None:
        engine = create_engine(MySQLURI, echo=False, max_overflow=5)
        Session = sessionmaker(bind=engine)
        self._session = Session()

    def saveNews(self, news: list):
        """保存新闻"""
        for item in news:
            _news = News(title=item.title, link=item.link, date=item.date)
            self._session.add(_news)
        self._session.commit()


    def getNewsById(self, id: int):
        """通过id获取某条新闻"""
        return self._session.query(News).filter(News.nid == id).first()


    def getAllNews(self) -> list:
        """获取所有新闻"""
        return self._session.query(News).all()
    
