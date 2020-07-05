## Main class:

### __ init __(self)
```python
self.text = ""
self.sample_text = """Аналитик данных с опытом работы. Окончил СГАУ со степенью магистра по математике. 
    Имею опыт работы с различными БД и в написании макросов. Работал с различными фреймворками для анализа данных на Python. 
    Участвовал в разработке нескольких систем для анализа данных. Есть примеры своих проектов по Data Science на GitHub:"""
self.functions = ["get_translate", "sort_doc", "cleaning", "words_count", "find_copy", "delete_copy"]
```

### SpacyTools():
```python
from SpacyToolKit.Tools import SpacyTools
model = SpacyTools()
```
SpacyTools is a class that allows you to quickly create and use models for stacking. The main language is English.

### load_text(self, text)

```python
model.load_text("your text here")
```

The function simply saves the received text in self.text.

### load_file(self, path)
```python
model.load_file("path to file.txt")
```

The function reads the text from the file to which the path is specified. Writes text to self.text.

### create(self, nlp=None)
```python
model.create(nlp=None)
```
The function accepts self and nlp (responsible for the language model).
Allows you to quickly create models for stacking.
Returns a doc object.

### Example

```python
from SpacyToolKit.Tools import SpacyTools
import en_core_web_sm

model = SpacyTools()

model.load_text(model.sample_text)

nlp = en_core_web_sm.load()

model.create(nlp)
```

## Side functions

For all examples to work:
```python
from SpacyToolKit.Tools import *
```

### get_translate(text)
```python
text = "имя"
print(get_translate(text)) #text translation into english
```

For this function to work, you must install the module - googletrans.
This function takes one argument - string and returns - string.
Any other argument will result in an error.

### sort_doc(doc)
```python
....
doc = model.create()
print(sort_doc(doc)) #filter the results
```

This function accepts the doc object obtained by using SpacyTools (). Create ().
During the operation of the algorithm, excess values are removed: numbers, omissions.
The function returns a cleared list of objects of type string.

### cleaning(data)
```python
....
data = cleaning(data) #after use sort_doc
print(data)
```

The function takes as input a list of objects of type string and returns a set.
The occurrences of a small word in a larger one are deleted.
Sometimes it’s worth running 2 times.

### words_count(text, num=None)
```python
data = "list or string"
print(words_count(data))
```

The function takes a list and returns a list in the format:
(number of entries, word).
By default, all words are displayed.

### find_copy(data)
```python
data = [abx, abc, agb]
print(find_copy(data))
```

The function takes a list and returns a set in the format:
(percent similarity, word)
You can use max () to find the most similar word.

### delete_copy(data)
```python
data = [abx, abc, agb]
delete_copy(data)
print(data)
```

The function takes a list and deletes the most similar word (if percentage> = 0.75).
The find_copy () function is required to work.

### You can also call the function description with help (your func here)
```python
help(get_translate)
```
