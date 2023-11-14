import nltk

def check_agreement(sentence):
    # Define context-free grammar for agreement
    agreement_grammar = nltk.CFG.fromstring("""
        S -> NP_Singular VP_Singular
        S -> NP_Plural VP_Plural
        NP_Singular -> Det_Singular N_Singular
        NP_Plural -> Det_Plural N_Plural
        Det_Singular -> 'the' | 'a'
        Det_Plural -> 'the'
        N_Singular -> 'dog' | 'cat'
        N_Plural -> 'dogs' | 'cats'
        VP_Singular -> V_Singular
        VP_Plural -> V_Plural
        V_Singular -> 'chases' | 'catches'
        V_Plural -> 'chase' | 'catch'
    """)

    # Create parser
    parser = nltk.ChartParser(agreement_grammar)

    # Tokenize and parse the sentence
    tokens = nltk.word_tokenize(sentence)
    parses = list(parser.parse(tokens))

    # Check for agreement
    return len(parses) > 0

# Example usage
sentence1 = "The dog chases the cat."
sentence2 = "The dogs chase the cats."

print("Agreement for sentence 1:", check_agreement(sentence1))
print("Agreement for sentence 2:", check_agreement(sentence2))
