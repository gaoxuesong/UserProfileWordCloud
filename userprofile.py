from os import path
from scipy.misc import imread
#import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'hot_key.txt')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = imread(path.join(d, "alice_mask.png"))

wc = WordCloud(font_path="simhei.ttf", background_color="white", max_words=2000, mask=alice_mask,
               stopwords=STOPWORDS.add("Qq"))
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "alice_Chinese.png"))

# show
# plt.imshow(wc)
# plt.axis("off")
# plt.figure()
# plt.imshow(alice_mask, cmap=plt.cm.gray)
# plt.axis("off")
# plt.show()
