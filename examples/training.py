# -*- coding: utf-8 -*-
from SpacyToolKit import separator
from SpacyToolKit.utils import preprocessing
from SpacyToolKit.training import create_blank, begin_training
from SpacyToolKit.model_selection import train_test_val_split
from SpacyToolKit.metrics import evaluate
import pandas as pd
import os
#  проверяем наличие файлов
directory = os.listdir()
directory

if "SpacyToolKit" not in directory:
    !git clone https://github.com/Lednik7/SpacyToolKit.git

df = pd.read_csv("vacs_train_5000.csv")[:100]
print(df.head())

y = separator(df["key_skills"], sep=" | ")
X = df["description"]
#  coef регулирует долю всех возможных values из key_skills(елси all_tasks=True)
#  При coef = 1 используются все values, это сильно сказывается на времени выполнения
train = preprocessing(X, y, "Skills", coef=1, all_tasks=False)

Train, Test, Val = train_test_val_split(train)
nlp, ner = create_blank(Train, lang="en") #  создадим пустой шаблон
#  будем сохранять модель после каждой итерации
nlp = begin_training(nlp, Train, Val, n_iter=2, save_iter=True)

# f - f1 score
# p - precision
# r - recall
print(evaluate(nlp, Test))