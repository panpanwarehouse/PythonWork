dayup=1
a="0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.010"
N=a.split(',')
dayfactory=N
print("N为{}时,".format(dayfactory))
for t in N:
    for i in range(365):
        if i % 7 in [5,6, 0]:
            dayup = dayup
        else:
            dayup = dayup * (1 + eval(t))
    print("年终值为{:.2f}".format(dayup),end=",")
