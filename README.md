****STEMMING****
import nltk
from nltk.stem import PorterStemmer
nltk.download("punkt")
stemmer = PorterStemmer()
sentences = [ "i am running in the park" ,
              "the running shoes are on sale" ,
              "she ran to catch the bus"]
for sentence in sentences:
  words = nltk.word_tokenize(sentence)
  stemmed_words = [stemmer.stem(word) for word in words ]
  stemmed_sentence = " ".join(stemmed_words)
  print(f"original: {sentence}")
  print(f"stemmed: {stemmed_sentence}\n")
  
**OUTPUT:**
original: I am running in the park
stemmed: i am run in the park

original: the running shoes are on sales
stemmed: the run shoe are on sale

original: she ran to catch the busses
stemmed: she ran to catch the buss

****TOKENIZATION****
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))

txt = "your shirt collection in fantastic. "\
      " is everything okay ." \
      "are you fine ."

tokenized = sent_tokenize(txt)
for i in tokenized:
	wordsList = nltk.word_tokenize(i)
	wordsList = [w for w in wordsList if not w in stop_words]
	tagged = nltk.pos_tag(wordsList)
	print(tagged)
**OUTPUT:**
[('shirt', 'NN'), ('collection', 'NN'), ('fantastic', 'NN'), ('.', '.')]
[('everything', 'NN'), ('okay', 'PRP'), ('.are', 'JJ'), ('fine', 'JJ'), ('.', '.')]

****SENTENCE LEVEL CONSTRUCTION****
import random
sentence_patterns = [
    "The {noun} {verb} {adjective}.",
    "{Noun} {verb} {adjective} {noun}.",
    "I {verb} {adjective} {noun}.",
    "She {verb} {noun}.",
    "He {verb} {adjective} {noun} {adverb}.",
]
nouns = ["cat", "dog", "ball", "house", "book"]
verbs = ["runs", "jumps", "sleeps", "reads", "eats"]
adjectives = ["quick", "lazy", "smart", "tall", "small"]
adverbs = ["slowly", "quickly", "loudly", "silently"]
Noun = "John"
def construct_sentence():
    pattern = random.choice(sentence_patterns)
    sentence = pattern.format(
        noun=random.choice(nouns),
        verb=random.choice(verbs),
        adjective=random.choice(adjectives),
        adverb=random.choice(adverbs),
        Noun=Noun,
    )
    return sentence
for _ in range(5):
    sentence = construct_sentence()
    print(sentence)
**OUTPUT:**
He reads quick house loudly.
John sleeps quick book.
She jumps house.
I jumps tall house.
The house reads quick.

****STOP WORDS****
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))

txt = "your shirt collection in fantastic. "\
      " is everything okay ." \
      "are you fine ."

tokenized = sent_tokenize(txt)
for i in tokenized:
	wordsList = nltk.word_tokenize(i)
	wordsList = [w for w in wordsList if not w in stop_words]
	tagged = nltk.pos_tag(wordsList)
	print(tagged)
**OUTPUT:**
[('shirt', 'NN'), ('collection', 'NN'), ('fantastic', 'NN'), ('.', '.')]
[('everything', 'NN'), ('okay', 'PRP'), ('.are', 'JJ'), ('fine', 'JJ'), ('.', '.')]

****Parser Tree****

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag, word_tokenize, RegexpParser
sample_text = "The quick brown fox jumps over the lazy dog"
tagged = pos_tag(word_tokenize(sample_text))
chunker = RegexpParser("""
					NP: {<DT>?<JJ>*<NN>} 
					P: {<IN>}			 
					V: {<V.*>}			
					PP: {<p> <NP>}		 
					VP: {<V> <NP|PP>*}	 
          """)
output = chunker.parse(tagged)
print("After Extracting\n", output)
**Output:**
After Extracting
 (S
  (NP The/DT quick/JJ brown/NN)
  (NP fox/NN)
  (VP (V jumps/VBZ))
  (P over/IN)
  (NP the/DT lazy/JJ dog/NN))

****PARTS OS SPEECH****
import nltk
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
text = "Natural language processing is a subfield of artificial intelligence that focuses on the interaction between computers and humans through natural language."
words = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(words)
print("Original Text:")
print(text)
print("\nPOS Tags:")
print(pos_tags)
**OUTPUT**
[('The', 'DET'), ('quick', 'ADJ'), ('brown', 'ADJ'), ('fox', 'NOUN'), ('jumps', 'VERB'), ('over', 'ADP'), ('the', 'DET'), ('lazy', 'ADJ'), ('dog', 'NOUN'), ('.', 'PUNCT')]

****SEMATIC ANALYSIS****
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
sentences = [
    "I love this product! It's amazing.",
    "The weather is terrible today.",
    "The movie was okay, but not great.",
    "I feel neutral about this.",
]
for sentence in sentences:
    sentiment_scores = sia.polarity_scores(sentence)
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        sentiment = "Positive"
    elif compound_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    print(f"Sentence: {sentence}")
    print(f"Sentiment: {sentiment} (Compound Score: {compound_score:.2f})\n")
**OUTPUT**
Sentence: I love this product! It's amazing.
Sentiment: Positive (Compound Score: 0.85)
Sentence: The weather is terrible today.
Sentiment: Negative (Compound Score: -0.48)
Sentence: The movie was okay, but not great.
Sentiment: Negative (Compound Score: -0.61)
Sentence: I feel neutral about this.
Sentiment: Neutral (Compound Score: 0.00)

****FIRST ORDER PREDICATE****
def Person(x):
    people = ["Alice", "Bob", "Charlie"]
    return x in people
def Knows(x, y):
    knowledge_base = [("Alice", "Bob"), ("Bob", "Charlie")]
    return (x, y) in knowledge_base
def Likes(x, y):
    return f"{x} likes {y}"
def rule(x, y):
    if Person(x) and Person(y) and Knows(x, y):
        return Likes(x, y)
    return None
for person1 in ["Alice", "Bob", "Charlie"]:
    for person2 in ["Alice", "Bob", "Charlie"]:
        if person1 != person2:
            result = rule(person1, person2)
            if result:
                print(result)
**OUTPUT:**
Alice likes Bob
Bob likes Charlie

****SYNTAX DRIVEN SEMATTIC ANALYSER****
import spacy
nlp = spacy.load("en_core_web_sm")
sentence = "The quick brown fox jumps over the lazy dog."
doc = nlp(sentence)
for token in doc:
    print(f"Token: {token.text}")
    print(f"Lemma: {token.lemma_}")
    print(f"POS (Part-of-Speech): {token.pos_}")
    print(f"Dependency Label: {token.dep_}")
    print(f"Semantic Meaning: {token.ent_type_}\n")
**OUTPUT**
Token: The
Lemma: the
POS (Part-of-Speech): DET
Dependency Label: det
Semantic Meaning: 

Token: quick
Lemma: quick
POS (Part-of-Speech): ADJ
Dependency Label: amod
Semantic Meaning: 

Token: brown
Lemma: brown
POS (Part-of-Speech): ADJ
Dependency Label: amod
Semantic Meaning: 

Token: fox
Lemma: fox
POS (Part-of-Speech): NOUN
Dependency Label: nsubj
Semantic Meaning: 

Token: jumps
Lemma: jump
POS (Part-of-Speech): VERB
Dependency Label: ROOT
Semantic Meaning: 

Token: over
Lemma: over
POS (Part-of-Speech): ADP
Dependency Label: prep
Semantic Meaning: 

Token: the
Lemma: the
POS (Part-of-Speech): DET
Dependency Label: det
Semantic Meaning: 

Token: lazy
Lemma: lazy
POS (Part-of-Speech): ADJ
Dependency Label: amod
Semantic Meaning: 

Token: dog
Lemma: dog
POS (Part-of-Speech): NOUN
Dependency Label: pobj
Semantic Meaning: 

Token: .
Lemma: .
POS (Part-of-Speech): PUNCT
Dependency Label: punct
Semantic Meaning: 






