numbers=input("请输入一串数字用逗号隔开:").split(",")
def tongji(number):
    set1=set(numbers)
    if len(set1)<len(numbers):
        return True
    else:
        return False
print(tongji(numbers))
def tongji(number):
    return len(number)<len(set(numbers))
numbers=input("请输入一串数字用逗号隔开:").split(",")
print(tongji(numbers))
