import time
scale=10
print("-----执行开始-----")
for i in range(scale+1):
    a,b='**'*i,'..'*(scale-i)
    c=(i/scale)*100
    print("\r%{:^3.0f}[{}->{}]".format(c,a,b),end="")
    time.sleep(0.2)
print("")
print("-----执行结束-----")


