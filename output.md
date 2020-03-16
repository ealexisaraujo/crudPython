>>> a = [1,2]
>>> b = [2,3]
>>> a + b
[1, 2, 2, 3]
>>> a * 2
[1, 2, 1, 2]
>>> a = [1]
>>> a
[1]
>>> a.append(2)
>>> a
[1, 2]
>>> b = a.pop()
>>> a
[1]
>>> b
2
>>> a = [3,8,1]
>>> a
[3, 8, 1]
>>> a.sort()
>>> a
[1, 3, 8]
>>> a = [1,2,3]
>>> del a [-1]
>>> a
[1, 2]
>>> a = list(range(0,100,2))
>>> a
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> b = list(range(0,10))
>>> b
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b + a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> b * 2
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b * 3
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b / a
************************** ERROR **************************
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'list' and 'list'
************************** ERROR **************************


>>> b % a
************************** ERROR **************************
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for %: 'list' and 'list'
************************** ERROR **************************


>>> b - a
************************** ERROR **************************
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'list' and 'list'
************************** ERROR **************************


>>>
>>>
>>>
>>> frutas = []
>>> frutas
[]
>>> fruits = list()
>>> fruits
[]
>>> fruits == frutas
True
>>> fruits.append('apple')
>>> fruits
['apple']
>>> len(fruits)
1
>>> fruits.append('banana')
>>> len(fruits)
2
>>> fruits.append('kiwi')
>>> fruits
['apple', 'banana', 'kiwi']
>>> some_fruit = fruits.pop()
>>> some_fruit
kiwi
>>> fruits
['apple', 'banana']
>>> some_fruit = fruits.pop(0)
>>> some_fruit
apple
>>> fruits
['banana']
>>> del fruits[0]
>>> fruits
[]
>>>
>>>
>>>
>>> import random
>>> random_numbers = []
>>> for i in range(10):
...     random_numbers.append(random.randint(0,15))
...
>>> random_numbers
[11, 0, 9, 2, 10, 10, 8, 6, 11, 15]
>>> ordered_numbers = sorted(random_numbers)
>>> ordered_numbers
[0, 2, 6, 8, 9, 10, 10, 11, 11, 15]
>>> random_numbers
[11, 0, 9, 2, 10, 10, 8, 6, 11, 15]
>>> random_numbers.sort()
None
>>> random_numbers
[0, 2, 6, 8, 9, 10, 10, 11, 11, 15]
>>> dir(random_numbers)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
