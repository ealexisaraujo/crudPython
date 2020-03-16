print('>>> countries = [\'México\',\'Venezuela\', \'Colombia\',\'Argentna\']')
countries = ['México','Venezuela', 'Colombia','Argentna']

print('>>> ages = [12, 18, 24, 34, 50]')
ages = [12, 18, 24, 34, 50]

print('>>> id(countries)')
print(id(countries))

print('>>> id(ages)')
print(id(ages))

print('>>> weights = [12, 18, 24, 34, 50]')
weights = [12, 18, 24, 34, 50]

print('>>> id(weights)')
print(id(weights))

print('>>> receta = [\'Ensalda\',2, \'lenguas\',5,\'Ajitomates\']')
receta = ['Ensalda',2, 'lenguas',5,'Ajitomates']

print('>>> countries')
print(countries)

print('>>> countries[0] = \'Ecuador\'')
countries[0] = 'Ecuador'

print('>>> countries')
print(countries)

print('>>> name = \'David\'')
name = 'David'

print('>>> name[0]')
print(name[0])

print('>>> name[0] = \'d\'')
print('************************** ERROR **************************')
print('Traceback (most recent call last):')
print('  File "<stdin>", line 1, in <module>')
print('TypeError: \'str\' object does not support item assignment')
print('************************** ERROR **************************\n\n')

print('>>> countries')
print(countries)

print('>>> global_countries = countries')
global_countries = countries
print('>>>\n>>>\n>>>')

print('>>> countries')
print(countries)
print('>>> global_countries')
print(global_countries)

print('>>> countries[0] = \'Guatemala\'')
countries[0] = 'Guatemala'

print('>>> global_countries')
print(global_countries)

print('>>>\n>>>\n>>>')
print('>>> import copy')
import copy
print('>>>\n>>>\n>>>')
print('>>> countries')
print(countries)

print('>>> global_countries = None')
global_countries = None

print('>>> global_countries')
print(global_countries)

print('>>> countries')
print(countries)

print('>>> global_countries = copy.copy(countries)')
global_countries = copy.copy(countries)

print('>>> countries')
print(countries)

print('>>> global_countries')
print(global_countries)

print('>>> countries[0] = \'Honduras\'')
countries[0] = 'Honduras'

print('>>> countries')
print(countries)

print('>>> global_countries')
print(global_countries)
print('>>>\n>>>\n>>>')

print('>>> for country in countries:')
print('...     print(country)')
print('...')
for country in countries:
    print(country)