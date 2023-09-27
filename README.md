****STEMMING****
import nltk
from nltk.stem import PorterStemmer
nltk.download("punkt")
stemmer = PorterStemmer()
sentences = [ "i am running in the park" ,
              "the running shoes are on sale" ,
              "she ran to catch the bus"]
for sentence in sentences:
  words = nltk.word_tokenize(sentence)
  stemmed_words = [stemmer.stem(word) for word in words ]
  stemmed_sentence = " ".join(stemmed_words)
  print(f"original: {sentence}")
  print(f"stemmed: {stemmed_sentence}\n")
  OUTPUT: 
original: I am running in the park
stemmed: i am run in the park

original: the running shoes are on sales
stemmed: the run shoe are on sale

original: she ran to catch the busses
stemmed: she ran to catch the buss
