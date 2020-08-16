"""
This module is used to preprocess data for the Spacy format of models for training
"""
import copy
from tqdm import tqdm
import re

def delete_None(train):
  new_train = []
  for i in range(len(train)):
    if train[i][1] == {'entities': []}:
      pass
    else:
      new_train.append(train[i])
  return new_train

def choice(new_train, param=3):
  train = []
  for i in range(len(new_train)):
    if len(new_train[i][1]['entities']) >= param:
      train.append(new_train[i])
  return train

def find_position(data, word):
  temp = []
  try:
    for i in re.finditer(word, data, flags=re.IGNORECASE):
      temp.append(i.span())
    return temp
  except:
    return [(0, 0)]

def cleaning(data):
  data = copy.deepcopy(data)
  for i in data:
    for j in data:
      if ((j.startswith(i)) and (j != i)) or ((j.endswith(i)) and (j != i)):
        try:
          data.remove(i)
        except:
          pass
  return data

def to_format(text, data, label):
  data = cleaning(data)
  res = [text, {'entities': []}]
  for word in data:
    position = find_position(text, word)
    for pos in position:
      res[1]['entities'].append(tuple([pos[0], pos[1], label]))
  return tuple(res)

def preprocessing(desc, skill, label):
  train = []
  enit = {}
  for i in tqdm(range((len(desc)))):
    enit['entities'] = list(set(to_format(desc[i], skill[i].split(" | "), label)[1]['entities']))
    res = (desc[i], copy.deepcopy(enit))
    try:
      res[1]['entities'].remove((0, 0, label))
    except:
      pass
    train.append(res)
  return train
