# SpacyToolKit
This is a small library designed to quickly stack Spacy models.

Choose the language of documantation:
1) English [here](https://github.com/Lednik7/SpacyTools/blob/master/documentation-en.md)
2) Russian [here](https://github.com/Lednik7/SpacyTools/blob/master/documentation-ru.md)

## Getting started
### Installing: ###

```
!git clone https://github.com/Lednik7/SpacyToolKit.git
```
### Needed packages: ###
For the library to work correctly, you need to download packages
```python
pip install spacy
pip install googletrans
pip install pymorphy2==0.8
```

## Your first model ##

### Prerequisites: ###

Before you run the code below, you need to install one of the models:
```python
Russian models:
!git clone -b v2.1 https://github.com/buriy/spacy-ru.git && cp -r ./spacy-ru/ru2/.
English models:
!python -m spacy download en_core_web_sm #size 11 mb
!python -m spacy download en_core_web_md #size 48 mb
!python -m spacy download en_core_web_lg #size 746 mb
```

More information about models [en](https://spacy.io/models/en) and [ru](https://github.com/buriy/spacy-ru)

### Simple model: ###

To begin, we import the necessary functions and the main class:
```python
from SpacyToolKit.Tools import SpacyTools, get_translate, sort_doc
import en_core_web_sm #!python -m spacy download en_core_web_sm
```
Now create an instance of the class:
```python
model = SpacyTools()
```
Since the model works best in English, we’ll use a translation from Google:
```python
text = model.sample_text #your text
trans = get_translate(text) #text translation into english
```

Now we are ready to load the text into the model and make a prediction:
```python
model.load_text(trans)
nlp = en_core_web_sm.load()
doc = model.create(nlp)
```
Let's look at the result:
```python
print(sort_doc(doc)) #filter the results
print(model.text)
```
Output:
```
Time: 1.39 - en_sm
['Python', 'Data Science', 'GitHub']
Data Analyst with work experience. He graduated from SSAU with a master's degree in mathematics.
I have experience working with various databases and in writing macros. Worked with various data analysis frameworks in Python.
He participated in the development of several systems for data analysis. There are examples of their Data Science projects on GitHub:
```
Fine! Now you are ready to delve into the topic.

You can see examples [here](https://github.com/Lednik7/SpacyTools/tree/master/examples)

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Lednik7/SpacyTools/blob/master/LICENSE) file for details
