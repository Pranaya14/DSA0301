import nltk

# Define context-free grammar
cfg = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | 'John'
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'caught'
""")

# Create an Earley parser
earley_parser = nltk.EarleyChartParser(cfg)

# Example sentence
sentence = ["the", "dog", "chased", "a", "cat"]

# Parse the sentence
parsed_trees = list(earley_parser.parse(sentence))

# Print the parse trees
for idx, tree in enumerate(parsed_trees):
    print(f"Parse Tree {idx + 1}:")
    tree.pretty_print()
