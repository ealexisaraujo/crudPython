>>> productos = {}
>>> productos['leche'] = 23.50
>>>
>>>
>>>
>>> rae = {}
>>> rae['pizza'] = 'La comida más deliciosa del mundo'
>>> rae
{'pizza': 'La comida más deliciosa del mundo'}
>>> rae['pasta'] = 'La comida más sabrosa de Italia'
>>> rae['pizza']
La comida más deliciosa del mundo
>>> rae['pasta']
La comida más sabrosa de Italia
>>> rae['helado']
************************** ERROR **************************
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'helado'
************************** ERROR **************************


Para evitar que se salga cuando no encuentra el objeto:
>>> a = rae.get('helado', None)
>>> print(a)
None
>>> a = rae.get('pizza', None)
>>> print(a)
La comida más deliciosa del mundo
>>>
>>>
>>>
>>> rae.keys()
dict_keys(['pizza', 'pasta'])
>>> rae.values()
dict_values(['La comida más deliciosa del mundo', 'La comida más sabrosa de Italia'])
>>> rae.items()
dict_items([('pizza', 'La comida más deliciosa del mundo'), ('pasta', 'La comida más sabrosa de Italia')])
>>>
>>>
>>>
>>> for key in rae.keys():
...     print(key)
...
pizza
pasta
>>> for key in rae.values():
...     print(key)
...
La comida más deliciosa del mundo
La comida más sabrosa de Italia
>>> for key in rae.items():
...     print(key)
...
('pizza', 'La comida más deliciosa del mundo')
('pasta', 'La comida más sabrosa de Italia')
