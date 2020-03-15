print('>>> x = 2')
x = 2

print('>>> y = 3')
y = 3

print('>>>')
print('>>> x == y')
print( x == y )

print('>>> y = 2')
y = 2

print('>>> x == y')
print( x == y )

print('>>> y = 3')
y = 3

print('>>>')
print('>>> x != y')
print( x != y )

print('>>> x > y')
print( x > y )

print('>>> x < y')
print( x < y )


print('>>> x >= y')
print( x >= y )

print('>>> x <= y')
print( x <= y )

print('>>> x => y')
print('************************** ERROR **************************')
print('  File "<stdin>", line 1')
print('     x => y')
print('        ^')
print('SyntaxError: invalid syntax')
print('************************** ERROR **************************\n\n')

print('>>> x = 2')
x = 2

print('>>> y = 3')
y = 3

print('>>> a = 5')
a = 5

print('>>> b = 7')
b = 7

print('>>>')
print('>>> (x < y) and (a < b)')
print( (x < y) and (a < b) )

print('>>> (x < y) and (a > b)')
print( (x < y) and (a > b) )

print('>>> (x < y) or (a > b)')
print( (x < y) or (a > b) )

print('>>> if x < y:')
print('...     print(\'x es menos que y\')')
print('... else:')
print('...     print(\'x NO es menos que y\')')
print('... ')
if x < y:
    print('x es menor que y')
else:
    print('x NO es menor que y')