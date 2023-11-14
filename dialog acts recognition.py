import spacy

def dialog_acts_recognition(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    dialog_acts = []
    for token in doc:
        if token.is_punct:
            dialog_acts.append("End of Utterance")
        elif token.dep_ == "punct" and token.text == "?":
            dialog_acts.append("Question")
        elif token.dep_ == "punct" and token.text == "!":
            dialog_acts.append("Exclamation")
        elif token.dep_ == "punct":
            dialog_acts.append("Statement")

    return dialog_acts

# Example usage
text = "How are you doing? This is fantastic!"
dialog_acts = dialog_acts_recognition(text)

print("Dialog Acts:", dialog_acts)
