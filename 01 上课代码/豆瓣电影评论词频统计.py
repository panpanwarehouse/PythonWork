import pandas as pd
import jieba
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv('../01 上课代码/movie_comments.csv',encoding='gbk')

# 选择一部电影，假设电影ID为1
selected_movie = df[df['ID'] == 1449711]

# 将评论文本合并为一个字符串
comments_text = ' '.join(selected_movie['content'].astype(str))

# 使用jieba进行分词
words = jieba.cut(comments_text)

# 进行词频统计
word_freq = pd.Series(words).value_counts()

text_no_stop=' '.join([word for word in comments_text.split() if word.lower() not in STOPWORDS])

top_10_words=word_freq.head(10)
exclude={"了","的","人","!","是","我"}
# 创建词云对象
wordcloud = WordCloud(width=800, height=400, background_color='white',font_path=r'C:\Windows\Fonts\STZHONGS.TTF').generate_from_frequencies(top_10_words)

# 绘制词云图
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()