from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = ["This is the first document.",
              "This document is the second document.",
              "And this is the third one.",
              "Is this the first document?"]

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Compute TF-IDF matrix
tfidf_matrix = vectorizer.fit_transform(documents)

# Print document ranking based on TF-IDF
print("Document Ranking:")
for i, doc in enumerate(documents):
    print(f"Document {i + 1}: {tfidf_matrix[i].sum()}")
