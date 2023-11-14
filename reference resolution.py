import spacy

def reference_resolution(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    resolved_text = doc._.coref_resolved

    return resolved_text

# Example usage
text = "John called his friend. He was happy."
resolved_text = reference_resolution(text)

print("Original Text:", text)
print("Resolved Text:", resolved_text)
