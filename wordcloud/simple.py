#coding:utf-8


from os import path
from wordcloud import WordCloud


d = path.dirname(__file__)
font=path.join(d, "DroidSansFallbackFull.ttf")

# Read the whole text.
text = open(path.join(d, 'idf.txt')).read().decode('utf-8')

# Generate a word cloud image
wordcloud = WordCloud(font_path=font).generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
#plt.imshow(wordcloud)
#plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(font_path=font,max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
