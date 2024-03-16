year, month = eval(input("请输入年份，月份（中间用逗号隔开）:"))
run = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
elif month in [4, 6, 9, 11]:
    days = 30
else:
    days = 29 if run else 28
print("{0}年{1}月有{2}天".format(year, month, days))