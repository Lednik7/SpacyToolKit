from SpacyTools import SpacyTools, get_translate, sort_doc

model = SpacyTools()

text = model.sample_text
trans = get_translate(text)

model.load_text(trans)
doc = model.create()

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
