name=input("请输入姓名：")
months=int(input("请输入工作时长："))
def calculate_bonus(name,months):
    if months <6:
        return(name,5000)
    elif months <=12:
        return (name,1000*months)
    elif months <=36:
        return(name,1500*months)
    else:
        return(name,80000)
print(calculate_bonus(name,months))