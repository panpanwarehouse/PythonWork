N = int(input("请输入一个奇数N: "))
#if N % 2 == 0:
  #  print("N必须是奇数")
#else:
for i in range(1, N+1, 2):#2:步长
    spaces = (N - i) // 2
    stars = i
    line = ' ' * spaces + '*' * stars
    print(line)
