print('>>> productos = {}')
productos = {}

print('>>> productos[\'leche\'] = 23.50')
productos['leche'] = 23.50

print('>>>\n>>>\n>>>')

print('>>> rae = {}')
rae = {}

print('>>> rae[\'pizza\'] = \'La comida más deliciosa del mundo\'')
rae['pizza'] = 'La comida más deliciosa del mundo'

print('>>> rae')
print(rae)

print('>>> rae[\'pasta\'] = \'La comida más sabrosa de Italia\'')
rae['pasta'] = 'La comida más sabrosa de Italia'

print('>>> rae[\'pizza\']')
print(rae['pizza'])

print('>>> rae[\'pasta\']')
print(rae['pasta'])

print('>>> rae[\'helado\']')
print('************************** ERROR **************************')
print('Traceback (most recent call last):')
print('  File "<stdin>", line 1, in <module>')
print('KeyError: \'helado\'')
print('************************** ERROR **************************\n\n')
print('Para evitar que se salga cuando no encuentra el objeto:')

print('>>> a = rae.get(\'helado\', None)')
a = rae.get('helado', None)

print('>>> print(a)')
print(a)

print('>>> a = rae.get(\'pizza\', None)')
a = rae.get('pizza', None)

print('>>> print(a)')
print(a)

print('>>>\n>>>\n>>>')
print('>>> rae.keys()')
print(rae.keys())

print('>>> rae.values()')
print(rae.values())

print('>>> rae.items()')
print(rae.items())

print('>>>\n>>>\n>>>')
print('>>> for key in rae.keys():')
print('...     print(key)')
print('...')
for key in rae.keys():
    print(key)

print('>>> for key in rae.values():')
print('...     print(key)')
print('...')
for key in rae.values():
    print(key)

print('>>> for key in rae.items():')
print('...     print(key)')
print('...')
for key in rae.items():
    print(key)