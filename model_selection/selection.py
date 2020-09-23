from sklearn.model_selection import train_test_split
import numpy as np
import random
from SpacyToolKit.metrics import evaluate

def cross_val_score(model, data, label=None, n_splits=5, shuffle=False, seed=42):
  """
  the function divides the array into pieces returns the average score for each metric
  """
  assert len(data) != 1, "Length of test data must be more than 1"
  assert len(data) >= n_splits >= 2, f"Please, change n_splits argument--> {n_splits}"
  assert label, "You have to set the test data label"

  random.seed(seed)
  if shuffle:
    data = random.shuffle(data)
  data = [data[i:i+n_splits] for i in range(0, len(data), len(data) // n_splits)]

  precision = []
  recall = []
  f1 = []

  for fold in data[:n_splits]:
    scores = evaluate(model, fold)
    if scores != dict():
      p, r, f = scores[label].values()
      precision.append(p)
      recall.append(r)
      f1.append(f)

  return [(label, np.mean(lst)) for label, lst in (("precision", precision), ("recall", recall), ("f1", f1))]

def train_test_val_split(data, test_size=0.3, val_size=0.3, random_state=42):
  """
  separator for train, test, validation
  """
  assert (test_size + val_size) < 1, f"train_size = 1 - (test_size + val_size). Your train_size --> {1 - (test_size + val_size)}"
  
  Train, Test = train_test_split(data, train_size=1-(test_size + val_size), random_state=random_state)
  Val, Test = train_test_split(Test, test_size=test_size/(test_size + val_size), random_state=random_state) 
  return Train, Test, Val