# 定义：元组是一种不可变的序列类型
# () tuple
tup1 = ('a', 'b', 'c')

print(tup1)
print(type(tup1))
# 元组可以转化其他的内容
print(tuple('hello world !'))

# 不可变
print(tup1[0])
# tup1[0] = 1  # 元组是不可变的类型,所以不可以修改


# 序列类型 序列可以进行切片取值
print(tup1[:-1])

# 元祖是不可变的,但是可以覆盖
# 修改元组的方法是 变成列表 修改后再变回来
tup1 = (1, 2, 3)

# 只有一个元素的元组,需要在后面加逗号
tup2 = ('a',)
print(tup2)
print(type(tup2))
