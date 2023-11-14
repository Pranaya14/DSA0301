import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Perform part-of-speech tagging
    pos_tags = nltk.pos_tag(words)

    return pos_tags

# Example text
text = "The quick brown fox jumps over the lazy dog."

# Perform part-of-speech tagging
tags = pos_tagging(text)

# Display the result
print("Original Text:")
print(text)
print("\nPart-of-Speech Tags:")
for word, pos_tag in tags:
    print(f"{word}: {pos_tag}")
s
