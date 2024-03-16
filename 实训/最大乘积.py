def MaxMulity():
    p = input("输入所有数字以','隔开\n").split(',')
    p=list(map(int, p))
    p.sort()
    print(p)

    maxM = int(p[-2]) * int(p[-1])
    print(f"最大乘积为{p[-2]}*{p[-1]}={maxM}")
MaxMulity()