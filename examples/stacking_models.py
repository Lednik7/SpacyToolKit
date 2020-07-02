from SpacyTools import SpacyTools, get_translate, sort_doc, cleaning

model = SpacyTools()

text = model.sample_text
trans = get_translate(text) #text translation into english

model.load_text(trans)

words = []
for i in model.lang[:-1]: #use only english models
  doc = model.create(i)
  words.append(sort_doc(doc))
  
data = []
for i in words:
  data += i
  
for i in range(len(data)): #The occurrences of a small word in a larger one are deleted.
  data = cleaning(data)
  
delete_copy(data)

print(data)

"""
Output:
{'data science', 'github', 'mathematics', 'python', 'sgau'}
"""
