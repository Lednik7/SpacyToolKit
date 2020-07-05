import time
t = time.time()
from SpacyToolKit.Tools import *
import en_core_web_sm
import en_core_web_md
import en_core_web_lg

model = SpacyTools()

text = model.sample_text
trans = get_translate(text) #text translation into english

model.load_text(trans)

models = [en_core_web_sm.load(), en_core_web_md.load(), en_core_web_lg.load()]

words = []
for i in models: #use only english models
  doc = model.create(i)
  words.append(sort_doc(doc))
  
data = []
for i in words:
  data += i
  
for i in range(len(data)): #The occurrences of a small word in a larger one are deleted.
  data = cleaning(data)
  
delete_copy(data)

print(data)
print("Time on GPU:", time.time() - t)

"""
Output:
Time: 0.02
Time: 0.02
Time: 0.02
{'ssau', 'mathematics', 'github', 'python', 'data science'}
Time on GPU: 26.720438718795776
"""
