# 二维列表
arr = ['1', '2', '3', '4']

arr2 = [
    ['a', 'b', 'c', 'd'],
    (1, 2, 3, 4),
    arr
]

print(arr2)
arr2[-1][-2] = '-1'
print(arr2[-1], arr2[-1][-2])
print(arr2[0][2])

"""遍历二维列表中的元素"""
# 直接遍历元素
for row in arr2:
    print('row:\t', row)
    for col in row:
        print('col:\t', col)

# 使用索引遍历元素
for row_index in range(0, len(arr2)):
    # 获取行索引, 根据第几行获取内容
    print(f'arr[{row_index}]:\t', arr2[row_index])
    for col_index in range(0, len(arr2[row_index])):
        # 获取列索引,根据行列索引获取元素
        print(f'arr2[{row_index}][{col_index}]:\t',
              arr2[row_index][col_index])
