import nltk

# Define a probabilistic context-free grammar (PCFG)
pcfg = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.5] | 'John' [0.5]
    VP -> V NP [0.9] | VP PP [0.1]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'dog' [0.7] | 'ball' [0.3]
    V -> 'chases' [0.5] | 'sees' [0.5]
    PP -> P NP [1.0]
    P -> 'with' [1.0]
""")

# Create a PCFG parser
parser = nltk.ViterbiParser(pcfg)

def parse_sentence(sentence):
    words = sentence.split()
    trees = list(parser.parse(words))

    if not trees:
        print(f"No parse tree found for the sentence: {sentence}")
    else:
        for tree in trees:
            print("Parse Tree:")
            tree.pretty_print()

# Example usage
parse_sentence("John chases the dog")
