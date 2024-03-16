from math import sqrt
def getNum( ): #获取用户输入
    nums = []
    iNumStr = input("请输入数字(直接输入回车退出):")
    while iNumStr != "":
        nums .append(eval (iNumStr))
        iNumStr = input("请输入数字(直接输入回车退出):")
    return nums
def mean (numbers):#计算平均值
    s=0.0
    for num in numbers:
        s=s+ num
    return s / len (numbers)
def dev (numbers,mean):#计算标准差
    sdev =0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return sqrt(sdev / (len (numbers)-1))
def median (numbers):#计算中位数
    new = sorted(numbers)
    size = len (numbers)
    if size % 2==0:
       med = (new [size//2-1] + new [size//2])/2
    else:
       med = new[size//2]
    return med

#用python在基本统计值计算中增加函数，实现最大值，最小值，众数的计算和输出
def maxs(numbers):
    # 计算最大值
    return max(numbers)

def mins(numbers):
    # 计算最小值
    return min(numbers)

def counts(numbers):
    # 计算众数
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return [k for k, v in counts.items() if v == max(counts.values())]


n = getNum()#主体函数
m = mean(n)
print("平均值:{},标准差:{:.2},中位数:{},最大值:{}，最小值:{}，众数:{}.".format(m,dev (n,m) ,median (n),maxs(n),mins(n),counts(n)))
