#整数转罗马数字
def int_to_roman():
    num=int(input("输入整数数字\n"))
    # 定义罗马数字符号和对应的数值
    romans = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
              5: 'V', 4: 'IV', 1: 'I'}

    # 从大到小遍历罗马数字符号，将数值逐渐减1
    result = ""
    for value, symbol in romans.items():
        while num >= value:
            result += symbol
            num -= value
    print(result)

#罗马数字转整数
def roman_to_int():
    s = input("罗马数字\n")
    # 定义罗马数字字符和对应的数值
    roman_mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # 初始化结果变量和上一个字符的值
    result = 0
    prev_value = 0

    # 遍历罗马数字字符串，从右向左处理
    for i in range(len(s) - 1, -1, -1):
        current_value = roman_mapping[s[i]]

        # 根据当前字符的值与上一个字符的值的大小关系，进行加减操作
        if current_value >= prev_value:
            result += current_value
        else:
            result -= current_value

        # 更新上一个字符的值
        prev_value = current_value
    print(result)
'''    第一提      '''
int_to_roman()
# roman_to_int()