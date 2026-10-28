# -- coding: utf8 --
import pandas as pd


data = [1,2,3,-10]
indexes = ['A','B','C','D']
array = pd.Series(data,index=indexes)
print(array)

dct = {'Artur': 5, "Rinat":3, 'Ruslan': 2}
indexes = {'Artur', 'Rinat', 'Ruslan'}
s = pd.Series(dct, index=indexes)
print(s)

s.name = "Таблица успеваемости"
s.index.name = 'Имена'
print(s[['Artur']])
print(s[s>=3])