import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")

df['tokens'] = df['content'].apply(word_tokenize)

# is history repeating itselfdontnormalizehate  
# [is, history, repeating, itselfdontnormalizehate]
# _____________________________________________________________________


from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
df['tokens'] = df['tokens'].apply(lambda lst: [word for word in lst if word not in stop_words])

# [history, repeating, itselfdontnormalizehate]
# _____________________________________________________________________


from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
df['lemma'] = df['tokens'].apply(lambda lst: [lemmatizer.lemmatize(word) for word in lst])

# [history, repeat, itselfdontnormalizehate]
# _____________________________________________________________________

# LDA
from gensim.corpora.dictionary import Dictionary
from gensim.model.ldamodel import LdaModel

# list of lists
tokens = [lst for lst in df['lemma']]

dictionary = Dictionary(tokens) # word mapping

# Convert document into the bag-of-words (BoW) format = list of (token_id, token_count) tuples.
corpus = [dictionary.doc2bow(row_tokens) for row_tokens in tokens] # frequency mapping

# id2word - Mapping from word IDs to words. It is used to determine the vocabulary size, as well as for debugging and topic printing.
lda = LdaModel(corpus = corpus, num_topics = 10, id2word = dictionary, random_state = 13, passes = 10)

print("Following are the topics: ")
for num, topic in lda.show_topics():
    print(f"Topic {num}: {topic}")

print("LDA Model Perplexity")
print(lda.log_perplexity(corpus)) # Lower the perplexity, better the model

# Visualize topics
import pyLDAvis
import pyLDAvis.gensim

# pyLDAvis.gensim_models.prepare
vis = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
pyLDAvis.save_html(vis,'lda_vis.html')