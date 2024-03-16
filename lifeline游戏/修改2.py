import json
import random
import sys
import time
from inputt import *
import jieba
class MK:
    def __init__(self, screen_width=414, screen_height=700, window_name="Lifeline Game", background_images=[]):


        #初始化pygame
        pygame.init()
        #创建游戏窗口长宽大小使用默认
        self.screen_width = screen_width
        self.screen_height = screen_height

        #创建窗口命名
        pygame.display.set_caption(window_name)



        #定义初始化对户口移动速度
        self.animation_speed = 10

        #放弃底部两个按钮创建改成输入框（Input）输入
        # self.button_width = 150
        # self.button_height = 70

        #定义基础颜色Color
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        #RESETbutton
        self.ResertBtnW=50
        self.ResertBtnH=50
        self.ResertBtnPos=(350,70)
        self.Resert=False

        #实例化窗口对象
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        #设置中文字体
        self.font = pygame.font.Font("ruimeijiazhangqingpingyingbikaishu.ttf", 20)
        #加载背景音乐
        self.load_bg_music()

        #定义游戏窗口背景图->类型为list，获取背景图游戏对象实例
        self.bg_images = self.load_bg_images(background_images)

        #初始化对话框默认为5个
        self.dialogs = self.draw_border_and_text()

        #声明玩家发送的消息变量
        self.send = ''


        # 初始生命章节小段 以(章)-(节)读取数据 例如1-1 3-2 为 ->第一章第1节 第三章第2节
        self.next = "1-1"

        #定义轮到谁进行讲述默认为遇难者
        self.turn = 0

        #定义发送等待时间
        self.wait_time = 1

        #判断是否解析 默认不进行解析 当对象choose键不为空的时候进行解析数据
        self.can=False

        #读取数据   默认格式为JSON
        self.DataJson=self.loadJsonDate()

        #定义选择对象默认为第一项
        self.ChooseId=0

        #定义是否完成
        self.finish=False
    #判断用户输入是否含有语义的（表示肯定）或（不赞成）或者其他返回选择结果
    def is_yes_or_no(self,input_text):
        words = jieba.cut(input_text)
        # 判断是否包含关键词
        keywords = {"是","有", '1',"对","好","可以","可", "是的", "是啊", "是的呀", "是的是的", "好的", "嗯", "嗯嗯", "嗯嗯嗯"}
        for word in words:
            if word in keywords:
                return 0  # 表示是
            elif word == "不" or word == "不是" or word == "不对" or word == "没" or word == "没有" or word == "2":
                return 1  # 表示否
        return 1  # 表示无法确定

    #加载音乐相关模块
    def load_bg_music(self):
        #背景音乐
        pygame.mixer.music.load("ambience.mp3")
        #按钮声音
        self.button_sound = pygame.mixer.Sound("button_tap.mp3")
        #接受消息声音
        self.alex_send_sound = pygame.mixer.Sound("message_incoming_b.mp3")
        # 设置音量
        pygame.mixer.music.set_volume(0.5)
        #不解决音乐是否循环 -1表示循环
        pygame.mixer.music.play(-1)

    #实例背景音乐list
    def load_bg_images(self, list_bg_images):
        bg_images = [pygame.image.load(img) for img in list_bg_images]
        bg_images = [pygame.transform.scale(image_load, (self.screen_width, self.screen_height)) for image_load in bg_images]
        return bg_images
    #绘制对话框
    def draw_border_and_text(self, font=None):
        #数量
        self.num_dialogs = 5
        #高度
        self.dialog_height = 120
        #间隔      ！(根据计算得出->窗口高度/数量 -对话框高度 【700/5-120】 )
        self.spacing = 20

        #整体偏移实际值
        self.vertical_offset = self.dialog_height + self.spacing
        dialogs = [{"text": "", "y": i * (self.vertical_offset)} for i in range(self.num_dialogs)]

        return dialogs

     #定义键盘相关信息
    def handle_events(self, text_box):
        for event in pygame.event.get():
            #窗口关闭时
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.ResertBtnRect.collidepoint(event.pos):
                    print("Button Clicked!")
                    self.Resert=True
                    button_clicked = True
            elif event.type == pygame.MOUSEBUTTONUP:
                button_clicked = False
            #键盘点击时
            elif event.type == pygame.KEYDOWN:
                #播放键盘点击声音
                self.button_sound.play()
                #传输给（input）输入的键盘事件
                text_box.safe_key_down(event)
                #当键盘回车键点击
                if event.key == pygame.K_RETURN:
                    # 清空画面input输入的消息
                    text_box.text=''
                    #设置下一个轮到遇难者回复
                    self.turn=0

                    #设置发送消息对象发送到窗口
                    self.handle_return_key(self.send)

                    #获取玩家选择返回结果的ID索引实现选择触发不同剧情
                    self.ChooseId=self.is_yes_or_no(self.send)
                    #休眠时间
                    self.mkWaitTime()
                    time.sleep(self.wait_time)

                    #设置下一个章节位置
                    self.next = self.DataJson[self.next]["options"][self.ChooseId]["to"]
                    #下一句不进行选择解析
                    self.can=False

    #加载数据表
    def loadJsonDate(self):
        with open("pp2.json",mode="r",encoding="utf-8")as f:
            data=f.read()
        return json.loads(data)

    #文本框动画
    def handle_return_key(self, text_box):
        if self.turn == 1:
            self.animation_speed = 2
            self.wait_time = 0
        else:
            self.animation_speed = 10
            self.wait_time = 1
            self.alex_send_sound.play()
        self.dialogs = [self.dialogs[1], self.dialogs[2], self.dialogs[3], self.dialogs[4], self.dialogs[0]]
        self.mkWaitTime()
        time.sleep(self.wait_time)
        for i in range(self.animation_speed):
            self.animate_dialogs(text_box)
            self.screen.blit(self.bg_images[0], (0, 0))
            self.draw_dialogs()

            self.screen.blit(self.ResertBtn,(self.ResertBtnRect.centerx-self.ResertBtnW//2,self.ResertBtnRect.centery-self.ResertBtnH//2,))
            self.screen.blit(self.bg_images[1], (0, 0))
            self.screen.blit(self.bg_images[1], (0, 0))

            pygame.display.flip()
            pygame.time.Clock().tick(60)
    def mkWaitTime(self):
        time=random.random()*1+1
        self.wait_time=time
    # 文本框动画改变的位置消息
    def animate_dialogs(self,tex):
        for dialog in self.dialogs:
            dialog["y"] -= self.vertical_offset / self.animation_speed
            if dialog["y"] < -self.dialog_height - self.spacing:
                dialog["y"] = (self.num_dialogs - 1) * (self.dialog_height + self.spacing)
        self.dialogs[-2]['text'] = tex

    #用户输入回调函数获取输入的文字
    def mkv(self,text):
        self.send=text
    #绘制所有对话框信息
    def draw_dialogs(self):
        for dialog in self.dialogs:
            pygame.draw.rect(self.screen, (0, 128, 255),(25, dialog["y"], self.screen_width - 50, self.dialog_height), 2)
            text_surface = self.font.render(dialog["text"], True, self.white)
            text_rect = text_surface.get_rect(center=(self.screen_width // 2, dialog["y"] + self.dialog_height // 2))
            self.screen.blit(text_surface, text_rect)
    #执行主函数

    def pygame_main(self):

        text_box = TextBox(350, 125, 30, self.screen_height - 150, font="ruimeijiazhangqingpingyingbikaishu.ttf", callback=self.mkv)
        self.ResertBtn=pygame.image.load("resert.png")
        self.ResertBtn=pygame.transform.scale(self.ResertBtn, (self.ResertBtnW, self.ResertBtnH))
        self.ResertBtnRect=self.ResertBtn.get_rect()
        self.ResertBtnRect.center=self.ResertBtnPos
        while True:
            if self.Resert:
                self.Resert=False
                break
            #注册键盘操作信息和传入输入框对象信息
            self.handle_events(text_box)
            if self.can==False:
                if self.next=="10-2":
                    continue
                #面板查看
                print(self.DataJson[self.next]["text"])


                self.handle_return_key(self.DataJson[self.next]["text"])
                if self.DataJson[self.next]["options"]!=[]:
                    self.can=True
                    self.turn=1
                else:
                    self.turn=0
                    next=self.next.split('-')
                    self.next=f"{next[0]}-{int(next[-1])+1}"
                    # self.next += 1
                if self.next.split('-')[0]=="9":
                    print("最后")
                    self.next="10-1"
                    self.can=False


            self.screen.blit(self.bg_images[0], (0, 0))
            self.draw_dialogs()
            if self.can:
                text_box.draw(self.screen)
            self.screen.blit(self.ResertBtn,(self.ResertBtnRect.centerx-self.ResertBtnW//2,self.ResertBtnRect.centery-self.ResertBtnH//2,))
            self.screen.blit(self.bg_images[1], (0, 0))
            pygame.display.flip()
            pygame.time.Clock().tick(60)

while True:

    mk = MK(background_images=["background.png", "border.91.png"])
    if mk.Resert==False:
        mk.pygame_main()
    else:
        break

