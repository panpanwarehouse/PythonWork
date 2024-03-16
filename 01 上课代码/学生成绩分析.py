xuehao=tuple(input("请输入学生学号:"))
py=eval(input("请输入学生python语言成绩:"))
c=eval(input("请输入学生c语言成绩:"))
average1=sum(py)/len(py)
average2=sum(c)/len(c)
bj=(average1+average2)/2
for i in range(0,4):
    if i<4:
        average3=sum(py[i])/len(py[i])
        average4 = sum(py[i])/ len(py[i])
        gr=(average3+average4)/2
        ls=tuple(gr)
    else:
        break
a=max(ls)

print("班级的平均分为{}".format(bj))
print("个人的平均分为{}".format(gr))
print("平均分最高的学生学号为{},平均分为{}".format(xuehao,a))