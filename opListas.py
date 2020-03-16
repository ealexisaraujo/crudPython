print('>>> a = [1,2]')
a = [1,2]
print('>>> b = [2,3]')
b = [2,3]
print('>>> a + b')
print(a + b)
print('>>> a * 2')
print(a * 2)

print('>>> a = [1]')
a = [1]

print('>>> a')
print(a)

print('>>> a.append(2)')
a.append(2)

print('>>> a')
print(a)

print('>>> b = a.pop()')
b = a.pop()

print('>>> a')
print(a)

print('>>> b')
print(b)

print('>>> a = [3,8,1]')
a = [3,8,1]

print('>>> a')
print(a)

print('>>> a.sort()')
a.sort()

print('>>> a')
print(a)

print('>>> a = [1,2,3]')
a = [1,2,3]

print('>>> del a [-1]')
del a [-1]

print('>>> a')
print(a)

print('>>> a = list(range(0,100,2))')
a = list(range(0,100,2))

print('>>> a')
print(a)

print('>>> b = list(range(0,10))')
b = list(range(0,10))

print('>>> b')
print(b)

print('>>> b + a')
print(b + a)

print('>>> b * 2')
print(b * 2)

print('>>> b * 3')
print(b * 3)

print('>>> b / a')
print('************************** ERROR **************************')
print('Traceback (most recent call last):')
print('  File "<stdin>", line 1, in <module>')
print('TypeError: unsupported operand type(s) for /: \'list\' and \'list\'')
print('************************** ERROR **************************\n\n')

print('>>> b % a')
print('************************** ERROR **************************')
print('Traceback (most recent call last):')
print('  File "<stdin>", line 1, in <module>')
print('TypeError: unsupported operand type(s) for %: \'list\' and \'list\'')
print('************************** ERROR **************************\n\n')

print('>>> b - a')
print('************************** ERROR **************************')
print('Traceback (most recent call last):')
print('  File "<stdin>", line 1, in <module>')
print('TypeError: unsupported operand type(s) for -: \'list\' and \'list\'')
print('************************** ERROR **************************\n\n')

print('>>>\n>>>\n>>>')
print('>>> frutas = []')
frutas = []
print('>>> frutas')
print(frutas)
print('>>> fruits = list()')
fruits = list()
print('>>> fruits')
print(fruits)
print('>>> fruits == frutas')
print(fruits == frutas)

print('>>> fruits.append(\'apple\')')
fruits.append('apple')

print('>>> fruits')
print(fruits)

print('>>> len(fruits)')
print(len(fruits))

print('>>> fruits.append(\'banana\')')
fruits.append('banana')

print('>>> len(fruits)')
print(len(fruits))

print('>>> fruits.append(\'kiwi\')')
fruits.append('kiwi')

print('>>> fruits')
print(fruits)

print('>>> some_fruit = fruits.pop()')
some_fruit = fruits.pop()

print('>>> some_fruit')
print(some_fruit)

print('>>> fruits')
print(fruits)

print('>>> some_fruit = fruits.pop(0)')
some_fruit = fruits.pop(0)

print('>>> some_fruit')
print(some_fruit)

print('>>> fruits')
print(fruits)

print('>>> del fruits[0]')
del fruits[0]

print('>>> fruits')
print(fruits)

print('>>>\n>>>\n>>>')
print('>>> import random')
import random

print('>>> random_numbers = []')
random_numbers = []

print('>>> for i in range(10):')
print('...     random_numbers.append(random.randint(0,15))')
print('...')
for i in range(10):
    random_numbers.append(random.randint(0,15))

print('>>> random_numbers')
print(random_numbers)

print('>>> ordered_numbers = sorted(random_numbers)')
ordered_numbers = sorted(random_numbers)

print('>>> ordered_numbers')
print(ordered_numbers)

print('>>> random_numbers')
print(random_numbers)

print('>>> random_numbers.sort()')
print(random_numbers.sort())

print('>>> random_numbers')
print(random_numbers)

print('>>> dir(random_numbers)')
print(dir(random_numbers))