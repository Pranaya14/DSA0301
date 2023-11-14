import nltk

# Define a context-free grammar (CFG)
cfg = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | 'John'
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'ball'
    V -> 'chased' | 'caught'
""")

# Create a parser for the CFG
parser = nltk.ChartParser(cfg)

# Function to generate and display a parse tree for a given sentence
def generate_parse_tree(sentence):
    words = sentence.split()
    trees = list(parser.parse(words))

    if not trees:
        print(f"No parse tree found for the sentence: {sentence}")
    else:
        for tree in trees:
            print("Parse Tree:")
            tree.pretty_print()

# Example usage
generate_parse_tree("the dog chased a ball")
