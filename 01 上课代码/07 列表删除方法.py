arr = ['正心', '丸子', '山禾', '自游', '巳月', '木子']

# pop 默认弹出最后一个元素,可以传递一个 索引 ,弹出指定值
# item = arr.pop()  # 默认弹出最后一个
# item = arr.pop(0)  # 指定索引弹出
muzi_index = arr.index('木子')
item = arr.pop(muzi_index)  # 指定索引弹出
print('arr:\t', arr)
print('item', item)

# remove  指定 内容 删除列表中的数据
item2 = arr.remove('自游')  # remove 是直接操作列表删除元素,没有返回值
print('arr:\t', arr)
print('item2:\t', item2)

# 列表的大多数方法是没有返回值的,直接修改列表本身
