username='test'
password='123'
max_attempts=3
attempts=0
while attempts<max_attempts:
    input_username=input("请输入账号:")
    input_password=input("请输入密码:")
    if input_username==username and input_password==password:
        print("登录成功")
        break
    else:
        attempts+=1
        print("用户名或密码错误")
        if attempts==max_attempts:
            print("三次用户名或密码错误，退出程序")