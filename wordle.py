import pandas as pd 
# import nltk 
# nltk.download('brown')
from nltk.corpus import brown
from random import sample 

vocab = sorted(list(set([w.upper() for w in brown.words() if len(w)==5 and w[0].islower() and w.isalpha()])))

f = pd.read_csv('prev-answers.txt') 
history = f.columns.tolist()
history = history[0].split(sep=" ")

def check_word(word, history): 
    return 'new word' if word not in history else 'already used'

def generate_word(vocab, history):
    new_word = sample(vocab, 1)[0]
    return new_word, check_word(new_word, history)

def word_with_char(vocab, history, char, char_idx=None, not_char_idx=None):
    if char_idx is not None:
        subset = [w for w in vocab if w[char_idx]==char.upper() and check_word(w, history) == 'new word']
    elif not_char_idx is not None:
        subset = [w for w in vocab if char.upper() in w and w[not_char_idx]!=char.upper() and check_word(w, history) == 'new word']
    else:
        subset = [w for w in vocab if char.upper() in w and check_word(w, history) == 'new word']
    return subset

def word_without_char(vocab, history, char):
    subset = [w for w in vocab if char.upper() not in w and check_word(w, history) == 'new word']
    return subset


# print(generate_word(vocab, history))

results = word_with_char(vocab=vocab, history=history, char='s', not_char_idx=3)
# results = word_with_char(vocab=results, history=history, char='g', not_char_idx=2)
# results = word_with_char(vocab=results, history=history, char='n', not_char_idx=4)
# results = word_with_char(vocab=results, history=history, char='r', not_char_idx=1)
# results = word_with_char(vocab=results, history=history, char='e', not_char_idx=4)

results = word_without_char(results, history, 'l')
results = word_without_char(results, history, 'e')
results = word_without_char(results, history, 'a')
results = word_without_char(results, history, 't')
# results = word_without_char(results, history, 'e')
# results = word_without_char(results, history, 'i')
# results = word_without_char(results, history, 'y')
# results = word_without_char(results, history, 'r')
print(results)

