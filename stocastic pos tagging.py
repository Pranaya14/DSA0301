import nltk
from nltk import FreqDist, ConditionalFreqDist
from nltk.tokenize import word_tokenize

# Training data (a small example)
training_data = [
    ("The", "DT"),
    ("quick", "JJ"),
    ("brown", "JJ"),
    ("fox", "NN"),
    ("jumps", "VBZ"),
    ("over", "IN"),
    ("the", "DT"),
    ("lazy", "JJ"),
    ("dog", "NN"),
]

# Function to train the POS tagger
def train_pos_tagger(training_data):
    # Create frequency distributions
    word_freq = FreqDist(training_data)
    bigram_freq = ConditionalFreqDist(training_data)

    # Calculate probabilities
    word_prob = {word: FreqDist(tags) for word, tags in bigram_freq.items()}
    for word in word_prob:
        total_count = word_freq[word]
        for tag in word_prob[word]:
            word_prob[word][tag] /= total_count

    return word_prob

# Function to perform stochastic POS tagging
def stochastic_pos_tagging(sentence, word_prob):
    tokens = word_tokenize(sentence)
    tagged_sentence = []

    for token in tokens:
        if token in word_prob:
            # Choose the most probable tag for the word
            most_probable_tag = word_prob[token].max()
            tagged_sentence.append((token, most_probable_tag))
        else:
            # Use a default tag (e.g., 'NN') for unknown words
            tagged_sentence.append((token, 'NN'))

    return tagged_sentence

# Train the POS tagger
word_probabilities = train_pos_tagger(training_data)

# Test sentence
test_sentence = "The quick fox jumps over the lazy dog."

# Perform stochastic POS tagging on the test sentence
result = stochastic_pos_tagging(test_sentence, word_probabilities)

# Display the result
print("Original Sentence:")
print(test_sentence)
print("\nStochastic POS Tags:")
for word, pos_tag in result:
    print(f"{word}: {pos_tag}")
