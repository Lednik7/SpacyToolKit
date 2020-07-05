"""
!git clone -b v2.1 https://github.com/buriy/spacy-ru.git && cp -r ./spacy-ru/ru2/. #русская модель
!python -m spacy download en_core_web_sm
!python -m spacy download en_core_web_lg
!python -m spacy download en_core_web_md
pip install spacy, googletrans
pip install pymorphy2==0.8
"""

from collections import Counter
import spacy
import time
from googletrans import Translator
from difflib import SequenceMatcher
from itertools import combinations

class SpacyTools():
  """
  A convenient class that allows you to quickly create and use models for stacking.
  The main language is English.
  """
  def __init__(self):

    self.text = ""

    self.sample_text = """Аналитик данных с опытом работы. Окончил СГАУ со степенью магистра по математике. 
    Имею опыт работы с различными БД и в написании макросов. Работал с различными фреймворками для анализа данных на Python. 
    Участвовал в разработке нескольких систем для анализа данных. Есть примеры своих проектов по Data Science на GitHub:"""

    self.functions = ["get_translate", "sort_doc", "cleaning", "words_count", "find_copy", "delete_copy"]

  def load_text(self, text):
    """
    load_text(self, text)
    The function simply saves the received text in self.text.
    """
    self.text = text
    return None

  def load_file(self, path):
    """
    load_file(path)
    The function reads the text from the file to which the path is specified.
    Writes text to self.text.
    """
    with open(path) as inf:
      self.text = inf.read()
    return None

  def create(self, nlp=None):
    """
    create(self, nlp)
    The function accepts self and nlp (responsible for the language model).
    Allows you to quickly create models for stacking.
    Returns a doc object.
    """
    t = time.time()

    doc = nlp(self.text)

    print("Time:", round(time.time() - t, 2))
    
    return doc

#------------------------------------------functions---------------------------------------------

def get_translate(text):
  """
  get_translate(text)
  For this function to work, you must install the module - googletrans.
  This function takes one argument - string and returns - string.
  Any other argument will result in an error.
  """
  translator = Translator()
  translations = (translator.translate(text)).text
  return translations

def sort_doc(doc):
  """
  sort_doc(doc)
  This function accepts the doc object obtained by using SpacyTools().Create().
  During the operation of the algorithm, excess values are removed: numbers, omissions.
  The function returns a cleared list of objects of type string.
  """
  lg = []
  for entity in doc.ents:
    temp = entity.text.split("\n")
    for i in temp:
      if (i != ''):
        try:
          int(i[0])
        except:
          lg.append(i)
  return lg

def cleaning(data):
  """
  cleaning(data)
  The function takes as input a list of objects of type string and returns a set.
  The occurrences of a small word in a larger one are deleted.
  Sometimes it’s worth running 2 times.
  """
  data = [i.lower() for i in data]
  for i in data:
    for j in data:
      if ((j.startswith(i)) and (j != i)) or ((j.endswith(i)) and (j != i)):
        data.remove(i)
  return set(data)
  
def words_count(text, num=None):
  """
  words_count(text, num=None)
  The function takes a list and returns a list in the format:
  (number of entries, word).
  By default, all words are displayed.
  """
  return [(i, j) for i, j in Counter(text).most_common(num)]

def find_copy(data):
  """
  find_copy(data)
  The function takes a list and returns a set in the format:
  (percent similarity, word)
  You can use max () to find the most similar word.
  """
  def ratio(pair):
    return (SequenceMatcher(None, *pair).ratio(), pair[0])

  def findword(wordlist):
      pairs = combinations(wordlist, 2)
      found = map(ratio, pairs)
      return found

  return set(findword(data))

def delete_copy(data):
  """
  delete_copy(data)
  The function takes a list and deletes the most similar word (if percentage> = 0.75).
  The find_copy() function is required for operation.
  """
  copy = max(find_copy(data))
  if copy[0] >= 0.75:
    data.remove(copy[1])

  return None

  #------------------------------------------other---------------------------------------------

  if __name__ == "__main__":
    main()
