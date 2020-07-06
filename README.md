# 蚌埠学院 综合新闻爬取爬虫

## 技术栈
- 发送请求：[Requests](https://requests.readthedocs.io/zh_CN/latest/)
- 解析提取HTML：[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)
- 数据库ORM：[SQLAlchemy](https://www.sqlalchemy.org/)
- 数据库：[MySQL](https://www.mysql.com/cn/)

## 目标网站
蚌埠学院综合新闻
![alt 蚌埠学院综合新闻](https://s1.ax1x.com/2020/07/06/UiztMQ.jpg "蚌埠学院综合新闻")

## 运行截图
![alt 终端运行截图](https://s1.ax1x.com/2020/07/06/UFPZB4.jpg "终端运行截图")

![alt 数据截图](https://s1.ax1x.com/2020/07/06/UFpsu4.jpg "数据截图")


## 使用说明
1. 需要修改``config.ini``配置文件，填写自己的MySQL数据库地址、数据库名、账号和密码即可。

2. 依赖安装：
```shell
pip install requirements.txt
```

3. 首次需运行``init_database.py``文件连库建表.


4. 运行脚本：
```shell
python main.py
```
