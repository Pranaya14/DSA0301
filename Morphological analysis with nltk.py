import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

# Download necessary NLTK resources (if you haven't already)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Sample text for morphological analysis
text = "The quick brown foxes are jumping over the lazy dogs."

# Tokenize the text
words = word_tokenize(text)

# Perform part-of-speech tagging
pos_tags = nltk.pos_tag(words)

# Initialize the WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to convert POS tags to WordNet tags
def get_wordnet_pos(tag):
    # Map POS tag to first character used by WordNetLemmatizer
    tag = tag[0].upper()
    tag = tag if tag in 'ANVR' else None
    return tag

# Perform lemmatization
lemmatized_words = []
for word, pos in pos_tags:
    wordnet_tag = get_wordnet_pos(pos)
    if wordnet_tag:
        lemmatized_word = lemmatizer.lemmatize(word, wordnet_tag)
        lemmatized_words.append(lemmatized_word)
    else:
        lemmatized_words.append(word)

# Display the lemmatized words
print("Original words:", words)
print("Lemmatized words:", lemmatized_words)
