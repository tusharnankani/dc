# Social Media Analysis Cheat Sheet

## Exp 2: Location Analysis
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import plotly.express as px


counts = df["location"].value_counts()
[print(counts)]

plt.scatter(df.location.unique(),counts)
plt.bar(df.location.unique(),counts)
plt.pie(counts,labels=df.location.unique(),autopct='% 1.1f %%')
px.scatter(df, 'dislikes' , 'likes','location')
```

## Exp 3: Trend Analysis
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Read in the CSV file
df = pd.read_csv('trend_analysis.csv')
# Convert the 'date' column to a datetime data type
df['date'] = pd.to_datetime(df['date'])
print(df.head())

#You can do the following to split into day month and year:
df["day"] = df.date.dt.day()
df["month"] = df.date.dt.month()
df["year"] = df.date.dt.year()

# Set the 'date' column as the index of the DataFrame
df.set_index('date', inplace=True)
# Resample the data by day and count the number of entries in each day
# argument 'D' indicating that we want to resample by day.
daily_counts = df.resample('D').count()
print("Daily Counts: \n", daily_counts)
# Plot the daily counts over time
plt.plot(np.array(daily_counts.index), np.array(daily_counts['id']))
plt.xlabel('Day')
plt.ylabel('Number of Entries')
plt.title('Social Media Trends')
plt.show()
```

## Exp5: Sentiment Analysis
```python
import pandas as pd
import numpy as np
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
import nltk
nltk.download('vader_lexicon')
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

comments = df['comments']
comments = str(comments).encode('utf-8')

scoring = []
for com in df.comments:
    score = sia.polarity_scores(str(com))['compound']
    scoring.append(score)
df['score'] = scoring
# OR
# df['score'] = df['comments'].apply(lambda comments:sia.polarity_scores(str(comments))['compound'])
df['Sentiment'] = df['score'].apply(lambda s : 'Positive' if s > 0 else ('Neutral' if s == 0 else 'Negative'))
df.head()
df.Sentiment.value_counts()
positiveCount = df.Sentiment.value_counts()[0]
neutralCount = df.Sentiment.value_counts()[1]
negativeCount = df.Sentiment.value_counts()[2]
arr = [positiveCount,neutralCount,negativeCount]
labels = ["Positive", "Neutral", "Negative"]
plt.pie(arr, labels=labels, autopct='%1.1f%%')

pos_tweets = df[df["Sentiment"] == "Positive"]
neg_tweets = df[df["Sentiment"] == "Negative"]
sns.kdeplot(pos_tweets["score"], shade=True, label="Pos")
sns.kdeplot(neg_tweets["score"], shade=True, label="Neg")
plt.xlabel("Polarity Score")
plt.ylabel("Density")
plt.title("Sentiment Analysis of Tweets")
plt.legend()
plt.show()
```
