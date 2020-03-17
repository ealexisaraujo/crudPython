>>> a = 1,2,3
>>> type(a)
<class 'tuple'>
>>> a[0]
1
>>> a[1]
2
>>> a[2]
3
>>> a[3]
************************** ERROR **************************
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
************************** ERROR **************************


>>> a[0]= 10
************************** ERROR **************************
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
************************** ERROR **************************


>>> a = 'Cristian'
>>> a[0]
C
>>> a[0]= d
************************** ERROR **************************
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
************************** ERROR **************************


>>> a = (1,1,1,2,3,4)
>>> type(a)
<class 'tuple'>
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> a.count(1)
3
>>> a.count(2)
1
>>> a.index(3)
4
>>>
>>>
>>>
>>> a = set([1,2,3])
>>> b = {3, 4, 5}
>>> type(a)
<class 'set'>
>>> type(b)
<class 'set'>
>>> a[1]
************************** ERROR **************************
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
************************** ERROR **************************


>>> a.add(3)
None
>>> a
{1, 2, 3}
>>> a.add(20)
None
>>> a
{1, 2, 3, 20}
>>> a.intersection(b)
{3}
>>> a.union(b)
{1, 2, 3, 20, 4, 5}
>>> a.difference(b)
{1, 2, 20}
>>> b.difference(a)
{4, 5}
