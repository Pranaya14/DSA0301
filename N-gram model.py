import random
from collections import defaultdict

def build_bigram_model(corpus):
    model = defaultdict(list)
    for i in range(len(corpus) - 1):
        current_word, next_word = corpus[i], corpus[i + 1]
        model[current_word].append(next_word)
    return model

def generate_text_bigram(model, start_word, max_length=10):
    current_word = start_word
    generated_text = [current_word]

    for _ in range(max_length - 1):
        if current_word in model:
            next_word = random.choice(model[current_word])
            generated_text.append(next_word)
            current_word = next_word
        else:
            break

    return ' '.join(generated_text)

# Example usage
corpus = "This is a sample text for demonstrating a bigram model for text generation.".split()
bigram_model = build_bigram_model(corpus)

# Generate text starting with a random word from the corpus
start_word = random.choice(corpus)
generated_text = generate_text_bigram(bigram_model, start_word, max_length=10)

print("Original Corpus:")
print(" ".join(corpus))
print("\nGenerated Text (Bigram Model):")
print(generated_text)
