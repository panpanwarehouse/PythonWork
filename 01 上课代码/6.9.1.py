numbers=input("请输入一串数字（用逗号隔开）：").split(",")

def calculate_statistics(numbers):
    # 计算最大值
    max_num = max(numbers)
    print("最大值为：", max_num)

    # 计算最小值
    min_num = min(numbers)
    print("最小值为：", min_num)

    # 计算众数
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    mode = [k for k, v in counts.items() if v == max(counts.values())]
    print("众数为：", mode)

calculate_statistics(numbers)