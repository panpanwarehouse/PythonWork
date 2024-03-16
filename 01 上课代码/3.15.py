dayup=1
a="0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.010"
N=a.split(',')
dayfactory=N
print("N为   {}时,".format(dayfactory))
print("年终值为 ",end="")
for t in N:
    for i in range(360):
        if i % 30 in (1,11):
            dayup = dayup * (1 + eval(t))
        else:
            dayup = dayup
    print("{:.2f}".format(dayup),end=",    ")

