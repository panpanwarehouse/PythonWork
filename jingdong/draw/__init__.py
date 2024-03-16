import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']

class Draw:
    def __init__(self):
        self.plt=plt
    def draw(self,df,xlabel,ylabel,title,x,y,rg,lables):
        #创建一个画布igsize=(20, 8) dpi分辨率
        self.plt.figure(figsize=(20, 8), dpi=100)
        # 绘制柱状图
        #处理y轴显示
        self.plt.yticks(rg, labels=lables)
        #绘制柱状图
        self.plt.bar(df[x], df[y])
        # 添加标签和标题
        #x轴标签
        self.plt.xlabel(xlabel)
        #y轴标签
        self.plt.ylabel(ylabel)
        #标题
        self.plt.title(title)
    def zhext(self):
        pass
