from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, Date
from Config import MySQLURI

engine = create_engine(MySQLURI, echo=True, max_overflow=5)
Base = declarative_base()


class News(Base):
    __tablename__ = 'bbu_news'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    link = Column(String(50), nullable=False)
    date = Column(Date, nullable=False)

    def __repr__(self):
        return "<新闻[{nid}]> {title}".format(self.nid, self.title)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
