import pandas as pd 
# import nltk 
# nltk.download('brown')
from nltk.corpus import brown
from random import sample 


def historical_answers():
    """
    TODO
    scrape from https://www.rockpapershotgun.com/wordle-past-answers 
    """
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
    return new_word if check_word(new_word, history) == "new" else generate_word(vocab, history)

def word_with_char(vocab, history, char, char_idx=None, not_char_idx=None):
    if char_idx is not None:
        subset = [w for w in vocab if w[char_idx]==char.upper() and check_word(w, history) == 'new']
    elif not_char_idx is not None:
        subset = [w for w in vocab if char.upper() in w and w[not_char_idx]!=char.upper() and check_word(w, history) == 'new']
    else:
        subset = [w for w in vocab if char.upper() in w and check_word(w, history) == 'new']
    return subset

def word_without_char(vocab, history, chars):
    chars = [c for c in chars]
    subset = [w for w in vocab if all(char.upper() not in w for char in chars) and check_word(w, history) == 'new']
    return subset

def generate_potentials(vocab, history, guess, result, incorrect_letters, yellows): 
    if result == "ggggg":
        append_solution(guess)
        return "Solved!"
    else:
        n = len(result)
        subset = vocab.copy()
        # yellows = []
        
        for i in range(n):
            if result[i] == 'g':
                subset = word_with_char(vocab=subset, history=history, char=guess[i], char_idx=i)
            elif result[i] == "y":
                yellow = (i, guess[i].upper())
                yellows.append(yellow)
                # print(yellows)
        # print(yellows)
        for y in yellows:
            # subset = word_with_char(vocab=subset, history=history, char=guess[i], not_char_idx=i)
            # print(y[0], y[1])
            subset = word_with_char(vocab=subset, history=history, char=y[1], not_char_idx=y[0])

        subset = word_without_char(vocab=subset, history=history, chars=incorrect_letters)
        return subset 

def append_solution(word):
    fname = 'prev-answers.txt'
    with open(fname, 'r') as f:
        lst = f.read().split()
        if lst[-1] == word.upper():
            print(word.upper() + " already added to history")
        else:
            with open(fname, 'a') as ff:
                ff.write(' ' + word.upper())
                print(word.upper() + " now appended to history")



if __name__ == "__main__":

    vocab = get_vocab(source="github") # github or nltk
    history = historical_answers()
    results = vocab.copy()
    yellows = []
    results = generate_potentials(results, history, "malay", "yggxg", "oest", yellows=yellows)
    print(results)