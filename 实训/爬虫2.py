import csv
import json

import requests

old_date=[]
def page_date(num):
    for i in range(1,num+1):
        url = f"https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page={i}&num=80&sort=symbol&asc=1&node=hs_a&symbol=&_s_r_a=setlen"
        response = requests.get(url=url)
        print(response.text)
        date = json.loads(response.text)
        old_date.extend(date)

data_list=[]
lst = {'代码': "symbol",
           '名称': "name",
           '最新价': "trade",
           '涨跌额': "pricechange",
           '涨跌幅': "changepercent",
           '买入': "buy",
           '卖出': "sell",
           '昨收': "settlement",
           '今开': "open",
           '最高': "high",
           '最低': "low",
           '成交量/手': "volume",
           '成交额/万': "amount",
           }
page_date(5)
# print(old_date)
for k in old_date:
    dict_k={}
    for key,value in lst.items():
        dict_k[key] = k[lst[key]]
    data_list.append(dict_k)
print(data_list)
with open("股票数据.csv",mode='w',newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=lst.keys())
    # 写入表头与数据
    writer.writeheader()
    writer.writerows(data_list)