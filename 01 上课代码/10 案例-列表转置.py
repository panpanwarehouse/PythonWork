""""""
"""
案例展示用 python 实现古诗词横竖两种版本效果图

实现横向打印效果如下
千山鸟飞绝
万尽人踪灭
孤舟梭立翁
独钓寒江雪

实现竖向打印效果如下
千万孤独
山尽舟钓
鸟人梭寒
飞踪立江
绝灭翁雪
"""

# poetry = [
#     ['千', '山', '鸟', '飞', '绝'],
#     ['万', '尽', '人', '踪', '灭'],
#     ['孤', '舟', '梭', '立', '翁'],
#     ['独', '钓', '寒', '江', '雪'],
# ]
text = """红军不怕远征难
万水千山只等闲
五岭逶迤腾细浪
乌蒙磅礴走泥丸
金沙水拍云崖暖
大渡桥横铁索寒
更喜岷山千里雪
三军过后尽开颜"""
lines = text.split()
poetry = []
for line in lines:
    poetry.append(list(line))

import pprint
pprint.pprint(poetry)

# # 获取行索引
# for row_index in range(len(poetry)):
#     # 获取列索引
#     for col_index in range(len(poetry[row_index])):
#         # 然后根据 行 列 索引 打印汉字
#         print(poetry[row_index][col_index], end='')
#     print()

# 1. 先遍历列
for col_index in range(len(poetry[0])):
    # 2. 再遍历行
    for row_index in range(len(poetry)):
        # print(f'{col_index}-{row_index}')
        print(poetry[row_index][col_index], end='')
    print()
