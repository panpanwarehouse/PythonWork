import wordcloud
from imageio import imread
fo = open ('E:\\PYTHON\\movie_comments.csv','r')
ls = []
for line in fo:
    line = line.replace('\n','')
    ls.append(line.split(','))
# print(ls[1][1])
comment_list = []
i = 1
for i in range(len(ls)-1):
    if ls[i][0] == '1309050':#选择第一部电影
        comment_list.append(ls[i][1]) #筛选电影评论放进列表
# print(comment_list)
fo.close()
f1 = open('comment.txt','w',encoding='utf-8')#将第一部评论保存为comment.txt
f1 .write(','.join(comment_list) + '\n')
f1.close()
# 电影词频统计
import jieba
txt = open('comment.txt','r',encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse = True)
for i in range(15):
    word , count = items[i]
    print('{0} {1}'.format(word,count))
# 电影评论词云
f = open('comment.txt','r',encoding='utf-8')
mask = imread('E:\\PYTHON\\chinamap.jpg')
txt = f.read()
f.close()
ls = jieba.lcut(txt)
txt = ''.join(ls)
excludes = {'这个','属于','真的'}
w = wordcloud.WordCloud(width=1000,height=700,mask=mask,
                        background_color='white',
                        font_path='Deng.ttf',
                        stopwords=excludes,max_words=15)
w.generate(txt)
w.to_file('E:\\PYTHON\\评论.png')