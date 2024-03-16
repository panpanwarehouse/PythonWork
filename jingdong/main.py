import pandas as pd
from draw import Draw


class sj:
    def __init__(self):
        # 声明类变量pd = pandas
        self.pd = pd
        # 声明类变量 draw = matpliotlib 封装的绘图类
        self.draw = Draw()

    def get_price(self, value: str):
        return float(value.replace('￥', ""))

    def get_pl_num(self, value: str):
        if '+' in value:
            num = value.split('+')[0]
            if '万' in num:
                # 提取数字部分
                num_part = num.split('万')[0]
                # 转换成浮点数，并乘以10000
                return float(num_part) * 10000
            else:
                return float(num)
        else:
            # 处理 '(/d+)条评价'的问题
            return value.split('条')[0]

    def get_name(self, value):
        value = self.replace_eng_name(value)

        return f"{value[0:5]}..{value[-4:-1]}"

    def replace_eng_name(self, value):
        value = value.replace("京东国际", "").replace("ThinkPad", "联想").replace("Apple", "苹果").replace("HUWIA",
                                                                                                   "华为").replace("HUAV",
                                                                                                                 "华为")
        return value

    def get_wan(self, value):
        if int(value) >= 10000:
            num_part = value / 10000
            num = f"{num_part}万+"
            return num
        else:
            return f"{value}+"

    # 获取商品价格排行
    def get_price_filter(self):
        data = pd.read_csv("京东数据_fliter.csv", sep=",", usecols=["商品名称", "价格"], engine="python")
        data = data.drop_duplicates()  # 数据去重
        data["价格"] = data['价格'].apply(self.get_price).astype(int)
        data = data.sort_values(by="价格", ascending=True)
        data["商品名称"] = data["商品名称"].apply(self.get_name)
        df_sorted = data.tail(10)
        rg = range(0, df_sorted['价格'].values[-1] + 1, df_sorted['价格'].values[-1] // 3)
        lables = [self.get_wan(i) for i in rg]
        draw = Draw()
        draw.draw(df_sorted, "商品名称", "商品价格", "商品价格最大10位", "商品名称", "价格", rg, lables)
        print(data)
    #获取商品评论排行
    def get_pl_fliter(self):
        data = pd.read_csv("京东数据_fliter.csv", sep=",", usecols=["商品名称", "评价数量"], engine="python")
        data = data.drop_duplicates()  # 数据去重
        data["商品名称"] = data["商品名称"].apply(self.get_name)
        data["评价数量"] = data["评价数量"].apply(self.get_pl_num).astype(int)
        # 排序
        df_sorted = data.sort_values(by="评价数量", ascending=True).tail(10)
        rg = range(0, df_sorted['评价数量'].values[-1] + 1, df_sorted['评价数量'].values[-1] // 3)
        lables = [self.get_wan(i) for i in rg]
        draw = Draw()
        draw.draw(df_sorted, "商品名称", "评价数量", "商品评价数量最大10位", "商品名称", "评价数量", rg, lables)
        print(data)

    # 获取品牌和店铺出现次数
    def get_sum_pp(self, name):
        data = pd.read_csv("京东数据_fliter.csv", sep=",", usecols=[name, "商品名称"], engine="python")
        # 去除品牌为"未找到品牌"的数据行
        if name == "品牌":
            data = data[data['品牌'] != '未找到品牌名']
        # 数据去重
        data = data.drop_duplicates()
        data[name] = data[name].apply(self.replace_eng_name)
        brand_counts = data[name].value_counts()
        data = brand_counts.reset_index()
        df_sorted = data.sort_values(by="count", ascending=True)
        if name == "店铺名称":
            df_sorted = df_sorted.tail(8)
        rg = range(0, df_sorted['count'].values[-1] + 1, df_sorted['count'].values[-1] // 3)
        lables = [self.get_wan(i) for i in rg]
        draw = Draw()
        draw.draw(df_sorted, name, f"{name}出现次数", f"{name}出现次数数据", name, "count", rg, lables)
    # 获取品牌和店铺总评价数
    def pp_sum_pl(self, name):
        data = pd.read_csv("京东数据_fliter.csv", sep=",", usecols=[name, "评价数量"], engine="python")
        if name == "品牌":
            data = data[data['品牌'] != '未找到品牌名']
        data = data.drop_duplicates()
        data[name] = data[name].apply(self.replace_eng_name)
        data["评价数量"] = data["评价数量"].apply(self.get_pl_num).astype(int)
        data = data.groupby(by=name).sum()
        data = data.reset_index()
        df_sorted = data.sort_values(by="评价数量", ascending=True)
        # 打印排序后的结果
        if name == "店铺名称":
            df_sorted = df_sorted.tail(8)
        rg = range(0, df_sorted['评价数量'].values[-1] + 1, df_sorted['评价数量'].values[-1] // 3)
        lables = [self.get_wan(i) for i in rg]
        draw = Draw()
        draw.draw(df_sorted, name, f"{name}出现合计评价数量", f"{name}出现合计评价数量", name, "评价数量", rg, lables)


s = sj()
s.get_price_filter()
s.get_pl_fliter()
s.get_sum_pp("品牌")
s.get_sum_pp("店铺名称")
s.pp_sum_pl("店铺名称")
s.pp_sum_pl("品牌")
s.draw.plt.show()