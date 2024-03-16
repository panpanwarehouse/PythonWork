import csv
import os
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

import key_split


class JD():
    def __init__(self):
        #初始化
        self.drive = webdriver.Chrome()
        self.url = 'https://passport.jd.com/new/login.aspx?/'
        self.key_split=key_split
    # 先手动登录，让程序获取到cookie，保存下来
    def getcookie(self):
        # 首先直接访问登录的页面 passport.jd.com
        self.drive.get(self.url)
        # 扫码登录
        # 登录之后的页面会跳转到这里，让浏览器等待，直到url完全匹配
        url = 'https://www.jd.com/'
        WebDriverWait(self.drive, 20).until(EC.url_to_be(url))
        # 登录之后停2秒
        time.sleep(2)
        # 获取到的cookies是列表
        cookieList = self.drive.get_cookies()
        # 转成字符串
        cookieStr = json.dumps(cookieList)
        # print(cookieStr)
        with open('../Jdcookie.txt', 'w') as f:
            f.write(cookieStr)
        print('cookie已写入')
        print(self.drive.current_url)
        self.drive.close()

    # 读取cookie
    def readcookie(self):
        self.drive.get('https://www.jd.com/')
        with open('../Jdcookie.txt', mode='r', encoding='utf-8') as f:
            cookie = f.read()
        # 读取到的是字符串类型，loads之后就变成了python中的字典类型
        cookie = json.loads(cookie)
        # 先把所有的cookie全部删掉
        self.drive.delete_all_cookies()
        for item in cookie:
            print(type(item))
            print(item)
            self.drive.add_cookie(item)
        # 是一个列表内套字典的形式

        self.drive.refresh()

        time.sleep(2)
        # input()
        # self.drive.close()
        self.drive.find_element(By.CSS_SELECTOR,'.form>input').send_keys("笔记本电脑")
        self.drive.find_element(By.CSS_SELECTOR,'.form>button').click()
        self.parse_data()

    def write(self):
        keys = self.key_split.split_Main_Keys("../电脑品牌.txt")
        with open('../京东数据1.csv', mode='r', encoding='utf-8') as f:
            data = f.read()
        list_data = data.split('\n')
        fieldnames = ["品牌", "商品名称", "价格", "评价数量", "店铺名称"]  # 品牌 商品名称 价格 评价数量 店铺名称
        all_data = []
        for li in list_data:
            da = li.split(',')
            pp = keys.getMain(da[1])  # 品牌
            ad_title = da[1]
            # 处理//todo 商品为空
            sku_price = da[0]  # 价格
            commentnum = da[2]  # 总评价数量
            dp = da[3]
            one_data = {"品牌": pp, "商品名称": ad_title, "价格": sku_price, "评价数量": commentnum, "店铺名称": dp}
            all_data.append(one_data)
        # 使用with语句确保文件在使用后正确关闭
        with open('../京东数据_fliter1.csv', 'w', newline='', encoding='utf-8') as csv_file:
            # 创建DictWriter对象，指定表头字段和文件
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            # 使用writeheader方法写入表头
            csv_writer.writeheader()
            # 使用writerow方法逐行写入数据
            csv_writer.writerows(all_data)
        print(f'CSV文件已成功写入')
    def parse_data(self):
        time.sleep(3)
        #判断页面是否有重新加载
        try:
             reload=self.drive.find_element(By.CSS_SELECTOR, ".nf-l-wrap>span>a")
             if reload:
                 reload.click()
                 self.parse_data()
        except:
            pass
        # self.drive.implicitly_wait(10)
        for i in range(1,10):
            rate=i/10
            js_script = f"document.documentElement.scrollTop=document.documentElement.scrollHeight*{rate}"
            self.drive.execute_script(js_script)
            time.sleep(1)
        """解析数据"""
        lis=self.drive.find_elements(By.CSS_SELECTOR,".gl-item")
        print(len(lis))
        try:
            for li in lis:
                title = li.find_element(By.CSS_SELECTOR, "div.p-name>a>em").text.replace('\n','').strip()
                price = li.find_element(By.CSS_SELECTOR, "div.p-price>strong").text
                pl = li.find_element(By.CSS_SELECTOR, "div.p-commit>strong").text
                dianpu = li.find_element(By.CSS_SELECTOR, "div.p-shop>span").text
                print(price,title,pl,dianpu)
                with open("京东数据.csv",mode='a',encoding='utf-8',newline="")as f:
                    csv_write=csv.writer(f)
                    csv_write.writerow([price,title,pl,dianpu])
        except:
            pass
        try:
            self.drive.find_element(By.CSS_SELECTOR, ".pn-next").click()
        except:
            #TOdo写入数据退出
            return
        self.parse_data()

if __name__ == '__main__':
    login = JD()
    #首次需要进行cookies写入后方可使用cookies登录
    if os.path.exists("../Jdcookie.txt"):
        print("读取文件")
        login.readcookie()
    else:
        print("首次需要进行cookies写入后方可使用cookies登录")
        login.getcookie()
    #数据二次处理
    login.write()


