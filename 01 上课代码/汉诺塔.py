#n:n个圆盘，src源柱子，dst目的柱子，mid是中间过渡的柱子
# def hanoi(n,src,dst,mid):
#     if n==1:
#         print("{}:{}->{}".format(1,src,dst))
#     else:
#         hanoi(n-1,src,mid,dst)
#         print("{}:{}->{}".format(n,src,dst))
#         hanoi(n-1,mid,dst,src)
def hanoi(n,src,dst,mid):
    if n==1:
        print("{}:{}->{}".format(1,src,dst))
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        hanoi(n-1,mid,dst,src)
