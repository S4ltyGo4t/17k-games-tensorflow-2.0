# Data Processing
import pandas as pd

# Basic Visualization tools
import matplotlib.pyplot as plt
from bokeh.plotting import figure
from matplotlib import style
from pandas.plotting import table

style.use("seaborn-muted")
import seaborn as sns
# Special Visualization
from wordcloud import WordCloud
import missingno as msno

# Bokeh (interactive visualisation)
from bokeh.io import show, output_notebook

plt.style.use('ggplot')
sns.set_palette('husl')

data_path = './17k-apple-games-dataset/'
data = pd.read_csv(data_path + 'appstore_games.csv')

data_description = data.describe()
ax = plt.subplot(211, frame_on=False)
plt.title("data description", fontsize=24)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
table(ax, data_description)
plt.savefig("figures/data_description.png")
plt.clf()

# todo save description as image
# ./figures/data_description


data_cleaned = data.drop(["URL", "ID"], axis=1)
fig2 = msno.bar(data_cleaned, inline=False)

plt.title("null values", fontsize=24)
plt.savefig("./figures/null_values.png")
plt.clf()

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
plt.clf()

aur = data['Average User Rating'].value_counts().sort_index()
p = figure(x_range=list(map(str, aur.index.values)),
           plot_height=250, title="Average User Rating",
           toolbar_location=None,
           tools="")

p.vbar(x=list(map(str, aur.index.values)),
       top=aur.values,
       width=0.9)
p.xgrid.grid_line_color = None
p.y_range.start = 0
show(p)
plt.clf()
# plt.show()
