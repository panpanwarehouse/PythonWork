try:
    TempStr=input("请输入带有符号的温度值:")
    if TempStr[-1] in ['F','f']:
        c=(eval(TempStr[0:-1])-32)/1.8
        print("转换后的温度是{:2f}C".format(c))
    elif TempStr[-1] in ['C','c']:
        F=1.8*eval(TempStr[0:-1])+32
        print("转换后的温度是{:2f}F".format(F))
    else:
        print("输入格式错误")
except:
    print("其他错误")
else:
    print("没有产生异常")
finally:
    print("程序运行完毕")