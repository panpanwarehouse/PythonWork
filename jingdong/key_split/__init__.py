import jieba

class split_Main_Keys:
    def __init__(self,file):
        self.file=file
        self.jieba=jieba
        self.split()
    def split(self):
        self.pplist = open(file=self.file, mode='r', encoding="utf-8").read().split('\n')
        print(self.pplist)
        for i in self.pplist:
            self.jieba.add_word(i)
        print("主品牌命名词填入成功")
    def getMain(self,data):
        data_list=self.jieba.lcut(data)
        for li in self.pplist:
            if li in data_list:
                return li
        return "未找到品牌名"
