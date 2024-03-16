import requests
import csv
from bs4 import BeautifulSoup
import  tqdm
# 设置列表，用以存储每本书籍的信息
data_list = []
#

# while 循环的条件设置为 page_number 的值是否小于 4
for t in tqdm.tqdm(range(0,3)):
    # 设置要请求的网页链接
    url = f'https://www.douban.com/doulist/5257286/?start={t*25}&sort=time&playable=0&sub_type='
    # 请求网页
    # books_list_res = requests.get(url)
    headers ={
    "User-Agent": "Mozilla/50 (Mindows NT 10.0; Min64; X64) AppleMebkit/53736 (KHTMl, like 6ecko) Chrome/58.0.3029110 5afari/537.3"

    }
    response = requests.get(url, headers=headers)
    # print(response.text)
    # 解析请求到的网页内容
    bs = BeautifulSoup(response.text, 'html.parser')
    # 搜索网页中所有包含书籍名和书籍链接的 Tag
    cards = bs.find_all(class_='doulist-subject')
    # 使用 for 循环遍历搜索结果
    for i,card in enumerate(cards):
        # print(card)
        info_dict = {}      # 创建字典，用以存储书籍信息
        title=card.find_all(class_="title")[-1]
        # 提取书籍名
        # print(title)
        bookname=title.find("a").text.strip()
        info_dict['电影名'] =bookname
        # print(bookname)
        # 提取书籍链接
        book_url = title.find("a")['href']
        # print(book_url)
        info_dict['链接'] =book_url

        #提取评分
        rating=card.find(class_="rating").find_all('span')
        if len(rating)==3:
            pf=f'{rating[1].text} {rating[2].text}'
        else:pf=rating[-1].text
        info_dict['评分'] =pf
        #提取影片信息
        info=card.find(class_="abstract").text
        info_list=info.split('\n')
        new_info=[item for item in info_list if item.strip() !='']
        # print(new_info)
        for message in new_info:
            # print(message.strip())
            msg=message.strip().split(':')
            info_dict[msg[0]]=msg[1]
        data_list.append(info_dict)
        # print(info)


# 新建 csv 文件存储书籍信息
with open('movies.csv', 'w',encoding="utf-8",newline='') as f:
    # 将文件对象转换成 DictWriter 对象
    head=['电影名', '链接', '评分', '导演','作者' ,'主演', '类型', '制片国家/地区', '年份', '出版社', '出版年']
    writer = csv.DictWriter(f, fieldnames=head)
    # 写入表头与数据
    writer.writeheader()
    writer.writerows(data_list)