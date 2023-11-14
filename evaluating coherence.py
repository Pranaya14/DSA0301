from sklearn.metrics.pairwise import cosine_similarity
import spacy

def coherence_evaluation(text):
    nlp = spacy.load("en_core_web_sm")
    sentences = [sent.text for sent in nlp(text).sents]

    vectors = [nlp(sentence).vector for sentence in sentences]
    similarity_matrix = cosine_similarity(vectors, vectors)

    coherence_score = similarity_matrix.sum(axis=1).mean()

    return coherence_score

# Example usage
text = "The quick brown fox jumps over the lazy dog. It was a sunny day in the forest."
coherence_score = coherence_evaluation(text)

print("Coherence Score:", coherence_score)
