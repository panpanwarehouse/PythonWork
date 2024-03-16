import learn as learn
import wordcloud
from imageio import imread
fo = open ('..\\01 上课代码\\movie_comments.csv','r')
ls = []
for line in fo:
    line = line.replace('\n','')
    ls.append(line.split(','))

comment_list = []
i = 1
for i in range(len(ls)-1):
    if ls[i][0] == '1309050':
        comment_list.append(ls[i][1])

fo.close()
f1 = open('comment.txt','w',encoding='utf-8')
f1 .write(','.join(comment_list) + '\n')
f1.close()

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

f = open('comment.txt','r',encoding='utf-8')
mask = imread('..\\01 上课代码\\fivestar.png')
txt = f.read()
f.close()
ls = jieba.lcut(txt)
txt = ''.join(ls)
excludes = {'这个','属于','真的'}
w = wordcloud.WordCloud(width=1000,height=700,mask=mask,
                        background_color='white',
                        font_path='C:\\Windows\\Fonts\\STZHONGS.TTF',
                        stopwords=excludes,max_words=15)
w.generate(txt)
w.to_file('..\\01 上课代码\\评论.png')
