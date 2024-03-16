
#判断是否叠词
def repeatedSubString():
    s=input("输入字符串判断是否叠词\n")

    # 遍历字符串的长度范围
    for i in range(1, len(s)//2 + 1):
        # 如果字符串长度不是子串长度的倍数，则跳过
        if len(s) % i != 0:
            # print(i)
            continue
        # 获取当前子串并重复多次
        sub_str = s[:i]
        # print(sub_str)
        if sub_str * (len(s) // i) == s:
            print("True")
            return
    print("False")
repeatedSubString()