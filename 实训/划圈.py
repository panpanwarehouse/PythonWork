import random
list1=['石头','剪刀','布']
def play_game():
    computer_choice=str(random.choice(list1))
    print("电脑出拳了轮到你了")
    user_choice=""
    while True:
        user_choice = input("请出拳（输入：石头/剪刀/布：\n")
        if user_choice not in list1:
            print("输入错误重新输入")
        else:
            break
    print(f"电脑出拳{computer_choice}------------")
    if computer_choice ==user_choice :
        print("平局")
        return

    if computer_choice=="石头" and user_choice =="剪刀" or computer_choice=="剪刀" and user_choice =="布"or computer_choice=="布" and user_choice =="石头":
        print("你输了")
    elif computer_choice==user_choice:
        print("平局")
    else:
        print("你输了")
play_game()



