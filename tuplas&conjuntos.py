print('>>> a = 1,2,3')
a = 1,2,3

print('>>> type(a)')
print( type(a))

print('>>> a[0]')
print(a[0])

print('>>> a[1]')
print(a[1])

print('>>> a[2]')
print(a[2])

print('>>> a[3]')
print('************************** ERROR **************************')
print('Traceback (most recent call last):')
print('  File "<stdin>", line 1, in <module>')
print('IndexError: tuple index out of range')
print('************************** ERROR **************************\n\n')


print('>>> a[0]= 10')
print('************************** ERROR **************************')
print('Traceback (most recent call last):')
print('  File "<stdin>", line 1, in <module>')
print('TypeError: \'tuple\' object does not support item assignment')
print('************************** ERROR **************************\n\n')

print('>>> a = \'Cristian\'')
a = 'Cristian'

print('>>> a[0]')
print(a[0])

print('>>> a[0]= d')
print('************************** ERROR **************************')
print('Traceback (most recent call last):')
print('  File "<stdin>", line 1, in <module>')
print('TypeError: \'str\' object does not support item assignment')
print('************************** ERROR **************************\n\n')

print('>>> a = (1,1,1,2,3,4)')
a = (1,1,1,2,3,4)

print('>>> type(a)')
print( type(a))

print('>>> dir(a)')
print(dir(a))

print('>>> a.count(1)')
print(a.count(1))

print('>>> a.count(2)')
print(a.count(2))

print('>>> a.index(3)')
print(a.index(3))

print('>>>\n>>>\n>>>')
print('>>> a = set([1,2,3])')
a = set([1,2,3])

print('>>> b = {3, 4, 5}')
b = {3, 4, 5}

print('>>> type(a)')
print( type(a))

print('>>> type(b)')
print( type(b))

print('>>> a[1]')
print('************************** ERROR **************************')
print('Traceback (most recent call last):')
print('  File "<stdin>", line 1, in <module>')
print('TypeError: \'set\' object is not subscriptable')
print('************************** ERROR **************************\n\n')

print('>>> a.add(3)')
print(a.add(3))

print('>>> a')
print(a)

print('>>> a.add(20)')
print(a.add(20))

print('>>> a')
print(a)

print('>>> a.intersection(b)')
print(a.intersection(b))

print('>>> a.union(b)')
print(a.union(b))

print('>>> a.difference(b)')
print(a.difference(b))

print('>>> b.difference(a)')
print(b.difference(a))