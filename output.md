>>> mi_tupla = 1,2,3
>>> tup = (1,2,3)
>>> tup = mi_tupla
True
>>> a = set([1,2,3])
>>> b = set([3, 4, 5])
>>> a.union(b
{1, 2, 3, 4, 5}
>>> a.intersection(b)
{3}
>>> a.difference(b)
{1, 2}
>>> b.difference(b)
set()
>>> 1 in a
True
>>> 1 in b
False
>>> 1 not in a
False
>>> 1 not in b
True
