import jieba


def is_yes_or_no(input_text):
    words = jieba.cut(input_text)

    # 判断是否包含关键词
    keywords = ["是", "有", "对", "好", "可以", "可", "是的", "是啊", "是的呀", "是的是的", "好的", "嗯", "嗯嗯", "嗯嗯嗯"]

    for word in words:
        if word in keywords:
            return 0  # 表示是
        elif word == "不" or word == "不是" or word == "不对" or word == "没" or word == "没有":
            return 1  # 表示否

    return 1  # 表示无法确定

# 测试
input_text = input("请输入中文：")
result = is_yes_or_no(input_text)
if result == 1:
    print("是")
elif result == 0:
    print("否")
else:
    print("无法确定")
