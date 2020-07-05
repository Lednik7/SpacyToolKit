## Основной класс:

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
SpacyTools - это класс позволяющий быстро создавать и использовать модели для стеккинга. Основной язык - английский.

### load_text(self, text)

```python
model.load_text("your text here")
```

Функция просто сохраняет полученный текст в self.text.

### load_file(self, path)
```python
model.load_file("path to file.txt")
```

Функция считывает текст из файла до которого указан путь. Записывает текст в self.text.

### create(self, nlp=None)
```python
model.create(nlp=None)
```
Функция принимает self и nlp(отвечает за языковую модель). 
Позволяет быстро создавать модели для стекинкга.
Возвращает объект doc.

### Example

```python
from SpacyToolKit.Tools import SpacyTools
import en_core_web_sm

model = SpacyTools()

model.load_text(model.sample_text)

nlp = en_core_web_sm.load()

model.create(nlp)
```

## Побочные функции

Для работы всех примеров:
```python
from SpacyToolKit.Tools import import *
```

### get_translate(text)
```python
text = "имя"
print(get_translate(text)) #text translation into english
```

Для работы данной функции необходимо установить модуль - googletrans. 
Эта функция принимает один аргумент - string и возвращает - string.
Любой другой аргумент приведет к ошибке.

### sort_doc(doc)
```python
....
doc = model.create()
print(sort_doc(doc)) #filter the results
```

Данная функция принимает на вход объект doc, полученный при использовании SpacyTools().create().
В процессе работы алгоритма убираются лишнии значения: цифры, пропуски.
Функция возвращает очищенный список из объектов типа string.

### cleaning(data)
```python
....
data = cleaning(data) #after use sort_doc
print(data)
```

Функция принимает на вход список из объектов типа string и возвращает множество.
Удалаяются вхождения малого слова в более крупное.
Иногда стоит запустить 2 раза.

### words_count(text, num=None)
```python
data = "list or string"
print(words_count(data))
```

Функция принимает список и возвращает список в формате:
(количество вхождений, слово).
По умлочанию выводятся все слова.

### find_copy(data)
```python
data = [abx, abc, agb]
print(find_copy(data))
```

Функция принимает список и возвращает множество в формате:
(процент схожести, слово)
Можно вопспользоваться max() для нахождения наиболее похожего слова.

### delete_copy(data)
```python
data = [abx, abc, agb]
delete_copy(data)
print(data)
```

Функция принимает список и удаляет наиболее похожее слово(если процент >= 0.75).
Для работы необходима функция most_copy().

### Вы также можете вызвать описание функции с помощью help(your func here)
```python
help(get_translate)
```
