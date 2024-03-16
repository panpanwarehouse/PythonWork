import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库
res =requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
# 返回一个response对象，赋值给res
html=res.text
# 把res解析为字符串
soup = BeautifulSoup( html,'html.parser')
# 把网页解析为BeautifulSoup对象
items = soup.find_all(class_='comment-body')   # 通过匹配属性class='books'提取出我们想要的元素
for item in items:                      # 遍历列表items

    name=item.find(class_="comment-meta").find(class_="comment-author").find("b").text #获取用户名称

    pl=item.find(class_="comment-content").find('p').text#获取评论内容
    datetime=item.find(class_="comment-metadata").find("a").find("time").text
    datetime=datetime.replace('\t','')

    print(f"{name}：{datetime}\n{pl}\n\n")


