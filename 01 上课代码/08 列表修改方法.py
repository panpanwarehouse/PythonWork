arr = ['正心', '丸子', '山禾', '自游']
arr[-1] = '木子'
print('arr:\t', arr)
#
# arr[1:-1] = ['巳月', '巳月', '巳月']
# print('arr:\t', arr)

arr.reverse()

print('arr:\t', arr)
arr.sort()
# sort 排序方法
arr2 = [5, 8, 4, 6, 2, 9]
item = arr2.sort(reverse=True)
# print('item:\t', item)
print('arr2:\t', arr2)
print('arr:\t', arr)
