# Data Processing
import numpy as np
import pandas as pd
import os

# Basic Visualization tools
import matplotlib.pyplot as plt
from matplotlib import style

style.use("seaborn-muted")
import seaborn as sns
# Special Visualization
# from bokeh.plotting import figure
from wordcloud import WordCloud
import missingno as msno

# Bokeh (interactive visualisation)
from bokeh.io import show, output_notebook

# from bokeh.plotting import figure
# output_notebook()

plt.style.use('ggplot')
sns.set_palette('husl')

data_path = './17k-apple-games-dataset/'
data = pd.read_csv(data_path + 'appstore_games.csv')
data_description = data.describe()
# todo save description as image
# ./figures/data_description

data_cleaned = data.drop(["URL", "ID"], axis=1)
fig2 = msno.bar(data_cleaned, inline=False)

plt.title("null values", fontsize=24)
plt.savefig("./figures/null_values.png")

word_cloud = WordCloud(background_color='white', width=800, height=800)

fig1 = plt.figure(figsize=(16, 32))
ax1 = plt.subplot2grid((2, 1), (0, 0), rowspan=1)
ax2 = plt.subplot2grid((2, 1), (1, 0), rowspan=1)

ax1.imshow(word_cloud.generate(' '.join(data['Name'])))
ax1.axis('off')
ax1.set_title("Names", fontsize=32)
ax2.imshow(word_cloud.generate(' '.join(data['Subtitle'].dropna().astype(str))))
ax2.axis('off')
ax2.set_title('Subtitles', fontsize=32)

plt.savefig("./figures/word_clouds.png")

# plt.show()
