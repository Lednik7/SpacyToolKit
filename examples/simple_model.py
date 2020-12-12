from SpacyToolKit.Tools import SpacyTools, sort_doc
from SpacyToolKit.other import get_translate
import en_core_web_sm

model = SpacyTools()

text = model.sample_text
trans = get_translate(text)

model.load_text(text)
nlp = en_core_web_sm.load()
doc = model.create(nlp)

print(sort_doc(doc))
print(model.text)

"""
Output:
Time: 1.41 - en_sm
['Python', 'Data Science', 'GitHub']
Data Analyst with work experience. He graduated from SSAU with a master's degree in mathematics.
I have experience working with various databases and in writing macros. Worked with various data analysis frameworks in Python.
He participated in the development of several systems for data analysis. There are examples of their Data Science projects on GitHub:
"""