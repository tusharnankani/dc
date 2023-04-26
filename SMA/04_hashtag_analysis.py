import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import ast

df = pd.read_csv("tweets.csv")

df['content'] = df['tweet'].copy()
df['content'] = df['content'].apply(lambda tweet: tweet.split())

df['hashtags'] = df['content'].apply(lambda tokens: [token for token in tokens if token.startswith("#")])

df['country'] = 'None'
for i, row in df.iterrows():
    loc_data = ast.literal_eval(row['additional_data'])

    if loc_data['place']:
        df['country'][i] = loc_data['place']['country']

df = df[df.country != "None"]

dataset = df[['country', 'hashtags']]

# Important
dataset = dataset.explode('hashtags')

'''
1   India	[#NewProfilePic, #AndrewTate, #khabib, ...]

~ explosion ~

1	India	#NewProfilePic
1	India	#AndrewTate
1	India	#khabib
1	India	#ConorMcGregor
1	India	#AskSR
'''


for country in dataset['country'].unique():
    dataset_country = dataset[dataset['country'] == country]

    # Important
    dataset_country['hashtags'].value_counts().plot(kind = 'barh')
    
    plt.xlabel('Hashtag Count')
    plt.ylabel('Hashtags')
    plt.title(f'Hashtag Popularity in {country}')
    plt.show()
