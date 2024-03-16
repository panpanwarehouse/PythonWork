def f(a,*b):
    for i in b:
        a+=i
        if i %3==0:
            continue
        print(a)
print(f(3,2,5,6,4))