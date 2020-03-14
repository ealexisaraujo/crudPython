>>> x = 2
>>> y = 3
>>>
>>> x == y
False
>>> y = 2
>>> x == y
True
>>> y = 3
>>>
>>> x != y
True
>>> x > y
False
>>> x < y
True
>>> x >= y
False
>>> x <= y
True
>>> x => y
************************** ERROR **************************
  File "<stdin>", line 1
     x => y
        ^
SyntaxError: invalid syntax
************************** ERROR **************************


>>> x = 2
>>> y = 3
>>> a = 5
>>> b = 7
>>>
>>> (x < y) and (a < b)
True
>>> (x < y) and (a > b)
False
>>> (x < y) or (a > b)
True
>>> if x < y:
...     print('x es menos que y')
... else:
...     print('x NO es menos que y')
... 
x es menor que y
