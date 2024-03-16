import random
import string
def generate_password(length):
    # 创建一个包含所有大小写字母和数字的字符列表
    characters = string.ascii_letters + string.digits
    # 使用random.choices随机选择字符，确保每个字符被选中的概率相等
    password = ''.join(random.choices(characters, k=length))
    return password
print(generate_password(8))
