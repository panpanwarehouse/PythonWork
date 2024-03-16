arr = ['4', '2', '1', '0', '6', '2', '1', '1']
arr2 = []  # arr2 用来统计重复的元素值
for index in range(len(arr)):  # 变量 arr 所有数据的索引值
    if arr[index] not in arr2:
        arr2.append(arr[index])
    else:
        print('重复的数据:\r', arr[index], index)
