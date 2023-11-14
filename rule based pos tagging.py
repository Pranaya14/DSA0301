import re

def rule_based_pos_tagging(sentence):
    tagged_sentence = []

    for word in sentence.split():
        if re.match(r'\b(?:The|the|A|a|An|an)\b', word):
            tagged_sentence.append((word, 'DT'))  # Determiner
        elif re.match(r'\b(?:quick|brown|lazy)\b', word):
            tagged_sentence.append((word, 'JJ'))  # Adjective
        elif re.match(r'\b(?:fox|dog)\b', word):
            tagged_sentence.append((word, 'NN'))  # Noun
        elif re.match(r'\b(?:jumps)\b', word):
            tagged_sentence.append((word, 'VBZ'))  # Verb
        elif re.match(r'\b(?:over)\b', word):
            tagged_sentence.append((word, 'IN'))  # Preposition
        else:
            tagged_sentence.append((word, 'NN'))  # Default: Noun

    return tagged_sentence

# Test sentence
test_sentence = "The quick fox jumps over the lazy dog."

# Perform rule-based POS tagging on the test sentence
result = rule_based_pos_tagging(test_sentence)

# Display the result
print("Original Sentence:")
print(test_sentence)
print("\nRule-Based POS Tags:")
for word, pos_tag in result:
    print(f"{word}: {pos_tag}")
