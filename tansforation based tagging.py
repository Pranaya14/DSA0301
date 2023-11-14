import nltk
from nltk.tag import brill
from nltk.tag import untag

# Sample training data
train_data = [
    [('The', 'DT'), ('quick', 'JJ'), ('brown', 'JJ'), ('fox', 'NN'), ('jumps', 'VBZ'), ('over', 'IN'), ('the', 'DT'), ('lazy', 'JJ'), ('dog', 'NN')],
    # Add more training data as needed
]

# Sample test data
test_data = [('A',), ('lazy',), ('dog',), ('jumps',), ('over',,), ('a',), ('quick',,), ('brown',,), ('fox',,)]

# Function to train a BrillTagger
def train_brill_tagger(train_data):
    templates = [
        brill.Template(brill.Pos([-1])),
        brill.Template(brill.Pos([1])),
        brill.Template(brill.Pos([-2])),
        brill.Template(brill.Pos([2])),
        brill.Template(brill.Pos([-2, -1])),
        brill.Template(brill.Pos([1, 2])),
        brill.Template(brill.Pos([-3, -2, -1])),
        brill.Template(brill.Pos([1, 2, 3])),
        brill.Template(brill.Pos([-1]), brill.Pos([1])),
    ]

    trainer = brill.FastBrillTaggerTrainer(initial_tagger=nltk.DefaultTagger('NN'), templates=templates, trace=3)
    brill_tagger = trainer.train(train_data, max_rules=10)

    return brill_tagger

# Train the BrillTagger
brill_tagger = train_brill_tagger(train_data)

# Apply the BrillTagger to the test data
tagged_test_data = brill_tagger.tag_sents(test_data)

# Display the result
print("Original Test Data:")
print(test_data)
print("\nTransformed POS Tags:")
print(tagged_test_data)
