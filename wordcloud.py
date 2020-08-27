import os
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# INCLUDE THE PATH TO THE PYTHON FILE
path_to_directory = ''

# ADD YOUR TEXT FILE NAME
text = open(path.join(path_to_directory, '<CHANGE-HERE>.txt')).read()

# CHANGE THE FONT FILE IF YOU'RE USING OTHER FONT FACE
font_path = path.join(path_to_directory, 'fonts/iskolapota.ttf')

# ADD A IMAGE FILE FOR THE MASK
# mask = np.array(Image.open(path.join(path_to_directory, '<CHANGE-HERE>.png')))

# ADD STOP WORDS
stopwords = ['වේ', 'ක්', 'ද', 'ලදී', 'ලදි', 'ලෙස']

wc = WordCloud(font_path=font_path,
               max_words=2000,
               mask=mask,
               stopwords=stopwords,
               width=1600,
               height=900,
               background_color="black",
               mode="RGBA",
               regexp=r"[ං-෴']+")

# GENERATE WORDCLOUD
wc.generate(text)

# STORE WORDCLOUD AS AN IMAGE
wc.to_file(path.join(path_to_directory, "wordcloud.png"))

# SHOW WORDCLOUD
plt.figure()
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()