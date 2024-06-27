import pandas as pd 
# import nltk 
# nltk.download('brown')
from nltk.corpus import brown
from random import sample 


def historical_answers():
    f = pd.read_csv('prev-answers.txt') 
    history = f.columns.tolist()
    history = history[0].split(sep=" ")
    return history

def get_vocab(source="nltk"):
    if source=="nltk": 
        vocab = sorted(list(set([w.upper() for w in brown.words() if len(w)==5 and w[0].islower() and w.isalpha()])))
    elif source=="github":
        vocab = pd.read_csv('english-words.txt')
        vocab = vocab['a'].tolist()
        vocab = [w.upper() for w in vocab if len(str(w))==5]
    return vocab

def check_word(word, history): 
    return 'new' if word not in history else 'used'

def generate_word(vocab, history):
    new_word = sample(vocab, 1)[0]
    return new_word, check_word(new_word, history)

def word_with_char(vocab, history, char, char_idx=None, not_char_idx=None):
    if char_idx is not None:
        subset = [w for w in vocab if w[char_idx]==char.upper() and check_word(w, history) == 'new']
    elif not_char_idx is not None:
        subset = [w for w in vocab if char.upper() in w and w[not_char_idx]!=char.upper() and check_word(w, history) == 'new']
    else:
        subset = [w for w in vocab if char.upper() in w and check_word(w, history) == 'new']
    return subset

def word_without_char(vocab, history, chars):
    # subset = [w for w in vocab if char.upper() not in w and check_word(w, history) == 'new']
    subset = [w for w in vocab if all(char.upper() not in w for char in chars) and check_word(w, history)=='new']
    return subset

def append_solution(word):
    with open('prev-answers.txt', 'a') as f:
        f.write(' ' + word.upper())



if __name__ == "__main__":

    # append_solution('order')
    
    vocab = get_vocab(source="nltk") 
    history = historical_answers()
    
    results = vocab
    # print(generate_word(vocab, history))
    print(check_word('PAINT', history))


    ### green letters ###
    # results = word_with_char(vocab=results, history=history, char='d', char_idx=2)
    # results = word_with_char(vocab=results, history=history, char='p', char_idx=2)
    
    ### yellow letters ####
    # results = word_with_char(vocab=results, history=history, char='e', not_char_idx=4)
    # results = word_with_char(vocab=results, history=history, char='e', not_char_idx=1)
    # results = word_with_char(vocab=results, history=history, char='a', not

    ### without char ####
    # results = word_without_char(results, history, ['l','a','t','s', 'n', 'u', 'g'])
    
    # print(results)

    # print(history[-10:])
