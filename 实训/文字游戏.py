def rescue(self):
        self.is_rescued = True

def main():
    survivor = Survivor()

    print("你与幸存者建立了联系，开始冒险吧！输入'结束'可以随时退出游戏。\n")

    while True:
        message = input("你：")
        if message == "结束":
            print("\n游戏结束。")
            break

        response = survivor.respond(message)
        print("幸存者：", response)

        # 根据具体情节编写触发故事线的选择逻辑
        if response == "幸存者：我已经获救了，感谢你的帮助！":
            print("\n你成功救出幸存者，获得一个游戏结局。")
            break

if __name__ == '__main__':
    main()


import random
import time

class Survivor:
    def __init__(self):
        self.delay = random.randint(1, 5)  # 延迟回答的随机时间
        self.is_rescued = False

    def respond(self, message):
        time.sleep(self.delay)  # 模拟延迟回答
        return self.generate_response(message)

    def generate_response(self, message):
        # 根据收到的消息生成回应
        if self.is_rescued:
            return "幸存者：我已经获救了，感谢你的帮助！"
        else:
            # 根据具体情节编写不同的对话逻辑
            if message == "你好":
                return "幸存者：你好，请问你是谁？"
            elif message == "你在哪里？":
                return "幸存者：我被困在一个孤岛上，周围都是海洋。"
            elif message == "有没有食物和水？":
                return "幸存者：我找到一些椰子和淡水，但恐怕不能维持太久。"
            elif message == "是否有其他幸存者？":
                return "幸存者：我目前还没有找到其他幸存者的踪迹。"
            elif message == "我们应该怎么办？":
                return "幸存者：我们可以尝试寻找信号或建造求救标志来引起注意。"
            # ... 根据需要继续编写其他对话逻辑

