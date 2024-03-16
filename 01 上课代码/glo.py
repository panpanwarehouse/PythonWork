s=1
def fun(num):
    global s
    s+=num
print(s,fun(2),s)