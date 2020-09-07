import nltk
import gensim

# Download the corpora needed. They will get stored on your PC and automatically detected later.
nltk.download('abc')
nltk.download('punkt')

from nltk.corpus import abc

# Create word embeddings using word2vec
model= gensim.models.Word2Vec(abc.sents())

# Looking for words most similar to the word 'science'
data=model.wv.most_similar('science')
for word in data:
    print(word)