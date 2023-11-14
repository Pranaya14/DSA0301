import spacy

# Load the SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Apple Inc. is planning to open a new store in Paris next month."

# Perform Named Entity Recognition (NER)
doc = nlp(text)

# Print entities and their labels
for ent in doc.ents:
    print(f"{ent.text}: {ent.label_}")
