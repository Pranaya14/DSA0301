from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

# Input sentence
sentence = "I went to the bank to deposit money."

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Perform Word Sense Disambiguation with Lesk Algorithm
sense = lesk(tokens, "bank")

# Print the disambiguated sense
print(f"Sense: {sense.name()}")
print(f"Definition: {sense.definition()}")
