from SpacyToolKit.Tools import words_count
from spacy.util import filter_spans
from collections import Counter
from tqdm import tqdm
from itertools import chain
from copy import deepcopy
import random
import re

class Span():
    def __init__(self, lst):
      self.start = lst[0]
      self.end = lst[1]
      self.label = lst[2]

    def get_tuple(self):
        return self.start, self.end, self.label

def length_count(data):
    return Counter(len(i[1]["entities"]) for i in data).most_common()

def choice_element_length(data, length):
    return [data[i] for i in range(len(data)) if  len(data[i][1]['entities']) >= length]

def remove_empty(data):
    return [data[i] for i in range(len(data)) if len(data[i][1]['entities']) != 0]

def flatten(data, coef=0.3, seed=42):
    """
    function to straighten an array from an array
    """
    random.seed(seed)
    flat = [j for i in data for j in i]
    flat = [i[0] for i in words_count(flat)[::-1]]
    if coef:
        flat = random.sample(flat, round(len(flat)*coef))
    return flat

def unique(x):
    """
    returns a unique array value
    """
    return tuple(set(x))

def find_position(data, word):
    """
    the function finds all occurrences of a word in a text ignoring case
    """
    try:
      return [i.span() for i in re.finditer(r"\b{}\b".format(word.strip()), data, flags=re.IGNORECASE)]
    except:
      return [(0, 0)]

def to_format(text, data, label):
    """
    function formats data to standard Spacy models
    """
    res = []
    for word in data:
        position = find_position(text, word)
        for pos_start, pos_end in position:
            if pos_start + pos_end != 0:
                res.append(Span([pos_start, pos_end, label]))

    return [i.get_tuple() for i in filter_spans(res)]

def preprocessing(texts, words, label, coef=0.3, all_tasks=False, include_repeat=True, progressbar=True):
    """
    the function returns the processed array for the Spacy standard
    """
    train = []
    enit = {}

    assert 0 < coef <= 1, f"The argument must be in the range (0 < coef <= 1) --> {coef}"

    if all_tasks:
        words_f = unique(flatten(words, coef))
        if coef == 1:
            include_repeat = False
    else:
      assert len(texts) == len(words), f"Data must be same length: ({len(texts)}, {len(words)})"
      print("\n\033[31mcoef is ignored because you are using all_tasks=False")

    for i in tqdm(range((len(texts))), disable=not progressbar):
      if all_tasks:
        if include_repeat:
            words_f = unique(chain(words_f, words[i]))
        enit['entities'] = to_format(texts[i], words_f, label)
      else:
        enit['entities'] = to_format(texts[i], words[i], label)

      train.append((texts[i], deepcopy(enit)))
    return train