import requests
from bs4 import BeautifulSoup

# 设置登录请求的请求网址
login_url = 'https://wp.forchange.cn/wp-admin/admin-ajax.php'
# 输入用户的账号密码
username = input('请输入用户名：')
password = input('请输入密码：')

# 设置登录请求的请求体数据
login_data = {
    'action': 'ajaxlogin',
    'username': username,
    'password': password,
    'remember': 'true'
}

# 请求登录网站
login_res = requests.post(login_url, data=login_data)

# 设置要请求的书籍评论页链接
comment_url = 'https://wp.forchange.cn/psychology/11069/comment-page-1/'
# 携带获取到的 Cookies 信息请求书籍网页
comment_res = requests.get(comment_url, cookies=login_res.cookies)
# 解析请求到的书籍网页内容
soup = BeautifulSoup(comment_res.text, 'html.parser')
# 搜索网页中所有包含评论的 Tag
comments_list = soup.find_all('div', class_='comment-txt')

# 使用 for 循环遍历搜索结果
for comment in comments_list:
    # 提取用户名
    comment_author = comment.find('cite', class_='fn').text[:-2]
    # 打印用户名
    print(comment_author)