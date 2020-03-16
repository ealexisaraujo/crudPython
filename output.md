>>> countries = ['México','Venezuela', 'Colombia','Argentna']
>>> ages = [12, 18, 24, 34, 50]
>>> id(countries)
140394847579184
>>> id(ages)
140394846190480
>>> weights = [12, 18, 24, 34, 50]
>>> id(weights)
140394847080352
>>> receta = ['Ensalda',2, 'lenguas',5,'Ajitomates']
>>> countries
['México', 'Venezuela', 'Colombia', 'Argentna']
>>> countries[0] = 'Ecuador'
>>> countries
['Ecuador', 'Venezuela', 'Colombia', 'Argentna']
>>> name = 'David'
>>> name[0]
D
>>> name[0] = 'd'
************************** ERROR **************************
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
************************** ERROR **************************


>>> countries
['Ecuador', 'Venezuela', 'Colombia', 'Argentna']
>>> global_countries = countries
>>>
>>>
>>>
>>> countries
['Ecuador', 'Venezuela', 'Colombia', 'Argentna']
>>> global_countries
['Ecuador', 'Venezuela', 'Colombia', 'Argentna']
>>> countries[0] = 'Guatemala'
>>> global_countries
['Guatemala', 'Venezuela', 'Colombia', 'Argentna']
>>>
>>>
>>>
>>> import copy
>>>
>>>
>>>
>>> countries
['Guatemala', 'Venezuela', 'Colombia', 'Argentna']
>>> global_countries = None
>>> global_countries
None
>>> countries
['Guatemala', 'Venezuela', 'Colombia', 'Argentna']
>>> global_countries = copy.copy(countries)
>>> countries
['Guatemala', 'Venezuela', 'Colombia', 'Argentna']
>>> global_countries
['Guatemala', 'Venezuela', 'Colombia', 'Argentna']
>>> countries[0] = 'Honduras'
>>> countries
['Honduras', 'Venezuela', 'Colombia', 'Argentna']
>>> global_countries
['Guatemala', 'Venezuela', 'Colombia', 'Argentna']
>>>
>>>
>>>
>>> for country in countries:
...     print(country)
...
Honduras
Venezuela
Colombia
Argentna
