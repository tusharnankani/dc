### Common across all

#### Pre-processing

```python
import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("file_name.csv")

df.shape
df.head(5)
df.sample(10)
df.describe()
df.info()
```

#### Cleaning

```python
# remove missing values
df = df[df.user_location.notnull()][['user','tweet','additional_data']]

df['content'] = df['content'].astype(str)

#remove links
df['content']=df['content'].str.replace('https?://\S+',' ',regex=True)

#lowercase
df['content']=df['content'].str.lower()

#remove special characters
df['content']=df['content'].str.replace('[^A-Za-z\s]+','',regex=True)

#remove numbers
df['content']=df['content'].str.replace('\d','',regex=True)
```

#### Visualizing Styles

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

plt.rcParams['font.size'] = 12
plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['figure.facecolor'] = '#00000000'

plt.title('Number of Items per Product Type')
plt.xlabel('Product Type ID')
plt.ylabel('Count of Product')

plt.plot(cnt.items())
```