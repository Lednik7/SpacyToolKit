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
from difflib import SequenceMatcher
from itertools import combinations

class SpacyTools():
    """
    A convenient class that allows you to quickly create and use models for stacking.
    The main language is English.
    """
    def __init__(self, text=""):
        self.text = text
        sample_text = """Аналитик данных с опытом работы. Окончил СГАУ со степенью магистра по математике.
        Имею опыт работы с различными БД и в написании макросов. Работал с различными фреймворками для анализа данных на Python.
        Участвовал в разработке нескольких систем для анализа данных. Есть примеры своих проектов по Data Science на GitHub:""".split("\n")
        self.sample_text = "\n".join(element.strip() for element in sample_text)

    def load_text(self, text):
        """
        load_text(self, text)
        The function simply saves the received text in self.text.
        """
        self.text = text

    def load_from_file(self, path):
        """
        load_from_file(path)
        The function reads the text from the file to which the path is specified.
        Writes text to self.text.
        """
        with open(path) as inf:
            self.text = inf.read()

    def create(self, nlp=None):
        """
        create(self, nlp)
        The function accepts self and nlp (responsible for the language model).
        Allows you to quickly create models for stacking.
        Returns a doc object.
        """
        return nlp(self.text)

#------------------------------------------functions---------------------------------------------

def sort_doc(doc):
    """
    sort_doc(doc)
    This function accepts the doc object obtained by using SpacyTools().Create().
    During the operation of the algorithm, excess values are removed: numbers, omissions.
    The function returns a cleared list of objects of type string.
    """
    result = []
    for entity in doc.ents:
        for element in entity.text.split("\n"):
            if (element != '') and element[0].isalpha():
                result.append(element)
    return result

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
    return data

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

def delete_copy(data, coef=0.75):
    """
    delete_copy(data)
    The function takes a list and deletes the most similar word (if percentage> = 0.75).
    The find_copy() function is required for operation.
    """
    copy = find_copy(data)
    if len(copy):
        if copy[0] >= coef:
            return data.pop(copy[1])

def separator(data, sep=" "):
    return [i.split(sep) for i in data]

def load_models_from_dir(path: str):
    models = []
    for i in tqdm(os.listdir(path)):
        models.append(spacy.load(os.path.join(path, i)))
    return models

def spans_to_words(train):
    return [train[0][i[0]:i[1]] for i in train[1]["entities"]]