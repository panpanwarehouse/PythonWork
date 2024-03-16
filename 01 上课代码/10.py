ls=[]
def func(a,b):
    ls.append(b)
    return a*b #字符乘数相当于把字符打印n遍
s=func("hello!",2)
print(s,ls)