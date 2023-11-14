import spacy
from nltk.corpus import wordnet

def syntax_driven_semantic_analysis(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)

    noun_phrases = []
    for chunk in doc.noun_chunks:
        noun_phrases.append(chunk.text)

    meanings = {}
    for noun_phrase in noun_phrases:
        synsets = wordnet.synsets(noun_phrase)
        meanings[noun_phrase] = [synset.definition() for synset in synsets]

    return noun_phrases, meanings

# Example usage
sentence = "The quick brown fox jumps over the lazy dog."
noun_phrases, meanings = syntax_driven_semantic_analysis(sentence)

print("Noun Phrases:", noun_phrases)
print("Meanings:")
for noun_phrase, meanings_list in meanings.items():
    print(f"{noun_phrase}: {meanings_list}")
