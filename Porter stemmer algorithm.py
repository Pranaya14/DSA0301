pip install nltk
from nltk.stem import PorterStemmer

def stem_words(words):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words

# Example list of words
word_list = ["running", "jumps", "beautifully", "friendship", "happily", "largest"]

# Perform stemming
stemmed_list = stem_words(word_list)

# Display the results
for original, stemmed in zip(word_list, stemmed_list):
    print(f"{original} => {stemmed}")
