st=input("请输入货币面值：")
hl=input("请输入汇率：")
if st[-3::]in['USD','usd']:
    CNY=(eval(st[0:-3])*eval(hl))
    print("转化后的面值{}CNY".format(int(CNY)))
elif st[-3::]in['CNY','cny']:
    USD=(eval(st[0:-3])*eval(hl))
    print("转化后的面值{}USD".format(int(USD)))
else:
    print("输入格式错误")