import numpy as np
def f(x):
    return x**2
n = int(input('任意输入投点次数:'))
x = np.random.uniform(0, 1, n)
y = np.random.uniform(0, 1, n)
hits = sum(np.where(y < f(x), 1, 0))
integral = hits / n
print('x^2在[0,1]的定积分: ', integral)

import random
n=1000*1000
hits=0
for i in range(1,n+1):
    x,y=random.random(),random.random()
    if x**2>y:
        hits+=1
s=hits/n
print(s)