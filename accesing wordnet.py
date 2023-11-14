from nltk.corpus import wordnet

# Retrieve synsets for a word
synsets = wordnet.synsets("play")

# Print meanings and examples
for synset in synsets:
    print(f"Meaning: {synset.definition()}")
    print(f"Example: {synset.examples()}\n")
