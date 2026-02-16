import spacy
from material import mpbc_3p
from collections import Counter
from spacy import displacy
import random

#Loading Portuguese model into processing variable
nlp = spacy.load("pt_core_news_sm")

#Inserting charpter's text inside processor function
doc = nlp(mpbc_3p)

# EXERCISE 1 - Extract the characters mentioned on the 3rd charpter of Machado de Assis' classic.
print(
    "1st exercise answer ->",
    [ent for ent in doc.ents if ent.label_ == "PER"]
)

# EXERCISE 2 - Excract all pronouns from the same charpter. Extra: count how many times they repeat.
print(
    "2nd exercise answer ->",
    list(
        Counter(
            token.text for token in doc if token.pos_ == "PRON"
            ).items()
        )
)

# EXERCISE 3 - Display a Dependency Tree of a random sentence from the charpter. Plus: customize visualizers settings.

#Inserting a random choice from a doc's sentences list into a variable
sent = random.choice(list(doc.sents))

#Showing user the sentence loaded onto displacy
print("The chosen sentence was ->", sent)

#Loading parameters into DisplaCy's displaying function
displacy.serve(sent,
               style="dep",
               port=5001,
               options={
                   "compact": True,
                   "bg" : "#2d2b55",
                   "color" : "#a5ff90",
                   "font" : "Poppins"
               }
)