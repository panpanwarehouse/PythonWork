import jieba
import  wordcloud
from imageio import imread

mask=imread("fivestar.png")
f=open("三国演义.txt","r",encoding="utf-8")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt="".join(ls)
excludes={"的","是","在","和"}
w=wordcloud.WordCloud(width=1000,height=700,mask=mask,background_color="white",font_path="msyh.ttc",stopwords=excludes)
w.generate(txt)
w.to_file("gpvmap.png")

