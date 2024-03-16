st=input("请输入货币面值：").lower() #  输入货币 lower()全部换成小写
hl=input("请输入汇率：")

if len(st.split("usd")) >1:
    CNY=float(st.split("usd")[0])*float(hl)
    print("转化后的面值{}CNY".format(CNY))
elif len(st.split("cny")) > 1:
    USD = float(st.split("cny")[0]) * float(hl)
    print("转化后的面值{}USD".format(USD))
else:
    print("输入格式错误")
