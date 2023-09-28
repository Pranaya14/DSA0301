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





