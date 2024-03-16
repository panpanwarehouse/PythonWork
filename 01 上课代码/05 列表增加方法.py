arr = ['正心', '丸子']

name = '山禾'

# append 追加,将元素添加到列表的末尾
arr.append(name)
# arr.append('自游')
# arr.append('巳月')

print('arr:\t', arr)

# insert 插入元素到指定位置
# arr.insert(0, '自游')
# arr.insert(1, '巳月')
# 把 '巳月' 插入到 '丸子' 前面去
# arr.insert(arr.index('丸子') + 1, '巳月')  # 插入到丸子后面去
# print('arr:\t', arr)


arr2 = ['自游', '巳月']
# arr.append(arr2) # append 是追加元素

# arr.extend(arr2)  # 将 arr2 合并拓展到 arr, 操作的是原有的列表
# + 返回的是一个新的列表
arr = arr + arr2  # 如果用 + 号实现 extend 功能,需要进行赋值
# print('arr + arr2:\t', arr + arr2, type(arr + arr2))
print('arr:\t', arr, type(arr))
