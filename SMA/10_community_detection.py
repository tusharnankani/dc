import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import networkx as nx
from networkx.algorithms import community

df = pd.read_csv('tweets.csv')
df.info()

dataset = df[df.user_location.notnull()].sample(10)

dataset['hashtags'] = dataset['tweet'].apply(lambda tweet: [item for item in tweet.split() if item.startswith("#")])

dataset = dataset.explode('hashtags')

users = list(dataset['user'].unique())
hashtags = list(dataset['hashtags'].unique())

vis = nx.Graph() # Create Graph
vis.add_nodes_from(users + hashtags) # Add nodes from unique entities

# IMPORTANT
for name, group in dataset.groupby(['hashtags','user']):
    hashtag, user = name
    weight = len(group)
    vis.add_edge(hashtag, user, weight=weight)


# Community Detection
# ____________________________

community_gen = community.girvan_newman(vis)
top_level_communities = next(community_gen)

communities = list(top_level_communities) # [{"#sample", "#sample", ...}, {"#sample", "sample", ...}]

# Assigning a node_colors map/dict
colors = ['red', 'orange', 'yellow']
node_colors = {}

for i, comm in enumerate(communities):
  for node in comm:
    node_colors[node] = colors[i]

nx.set_node_attributes(vis, node_colors, name='color') # set attributes
node_colors = nx.get_node_attributes(vis, 'color') # get color attributes

nx.draw(vis, with_labels=True, node_color=node_colors.values())
plt.axis("off")
plt.show()


# Influential Node Analysis
# ____________________________

centrality = nx.betweenness_centrality(vis) # dict
inf_nodes = sorted(centrality.items(), key = lambda item:item[1], reverse=True)[:5]

for nodes in inf_nodes:
    print(f'{nodes[0]} : {nodes[1]}')