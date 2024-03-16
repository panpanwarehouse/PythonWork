import time
print("-----执行开始-----")
P="Starting ··· Done!"
c=''
for i in P:
    time.sleep(0.2)
    c+=i
    print("\r{}".format(c),end='')
print()
print("-----执行结束-----")
