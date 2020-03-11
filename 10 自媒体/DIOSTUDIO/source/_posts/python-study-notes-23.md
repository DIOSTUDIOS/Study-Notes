---
title: Python 3 学习笔记：抓取猫眼热映口碑榜
tags: [python, 猫眼, 爬虫]
date: 2019-08-15 09:53:19
---

> 人生苦短，我用 Python

话不多说，直接上代码：

```python
import requests
import re
import os
from openpyxl import Workbook


url = r'https://maoyan.com/board/7'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
}

# 获取电影名称、主演人员、上映时间
def get_films_info():
    info = []
    response = requests.get(url=url, headers=headers)

    # 获取电影名单
    pattern = r'<a href="/films/\d{1,7}" title=".*?" data-act="boarditem-click" data-val="{movieId:\d{1,7}}">(.*?)</a>'
    film = re.findall(pattern=pattern, string=response.text, flags=re.I)
    info.append(film)

    # 获取主演名单
    pattern = r'<p class="star">\s+主演：(.*?)\s+</p>'
    imgs = re.findall(pattern=pattern, string=response.text, flags=re.S)
    info.append(imgs)

    # 获取上映时间
    pattern = r'<p class="releasetime">上映时间：(.*?)</p>'
    time = re.findall(pattern=pattern, string=response.text, flags=re.S)
    info.append(time)

    return info

# 获取电影海报图片的 url
def get_poster_urls():
    response = requests.get(url=url, headers=headers)
    pattern = r'<img data-src="(.*?)@160w_220h_1e_1c" alt=".*?" class="board-img" />'
    urls = re.findall(pattern=pattern, string=response.text, flags=re.I)

    return urls

# 下载海报
def download_films_poster():
    film = get_films_info()[0]
    urls = get_poster_urls()

    i = 0
    # 下载并保存海报，并以电影名称命名
    for url in urls:
        poster = requests.get(url=url, headers=headers).content
        with open(film[i] + '.jpg', 'wb') as file:
            file.write(poster)

        i = i + 1

# 创建一个 excel 文件用于保存获取的信息
def create_catalog():
    # 获取电影名称、主演人员、上映时间的列表
    film = get_films_info()[0]
    imgs = get_films_info()[1]
    time = get_films_info()[2]

    logs = Workbook()
    # 将上面的信息写入 excel 文件
    for row in range(1, (len(film) + 1)):
        logs['Sheet'].cell(row=row, column=1, value=film[(row-1)])
        logs['Sheet'].cell(row=row, column=2, value=imgs[(row-1)])
        logs['Sheet'].cell(row=row, column=3, value=time[(row-1)])

        path = os.path.join(os.getcwd() + '\\' + film[(row-1)] + '.jpg')
        link = os.path.join(os.getcwd() + '\\' + film[(row-1)] + '.jpg')
        # 设置海报超链接
        logs['Sheet'].cell(row=row, column=4, value=path).hyperlink = link

    logs.save(filename=r'猫眼热映榜.xlsx')

    pass


if __name__ == '__main__':
    download_films_poster()

    create_catalog()

```

以上代码用于练习爬虫及前面学到的内容，可以抓取猫眼电影网中榜单下的热映口碑网的相关信息，并使用 excel 文件记录。

![抓取结果展示.jpg](https://i.loli.net/2019/08/15/ORFISNCTwkWtvpo.jpg)



------

<script type="text/javascript" src="http://tajs.qq.com/stats?sId=59765948" charset="UTF-8"></script>