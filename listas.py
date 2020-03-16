import copy
countries = ['Mexico', 'Venezuela', 'Colombia', 'Argentina']

ages = [12, 18, 24, 34, 50]

print(countries)
print(ages)

weights = [12, 18, 24, 34, 50]
receta = ['Ensalada', 2, 'Lechugas', 5, 'Jitomates']
countries[0] = 'Ecuador'
global_countries = countries
countries[0] = 'Guatemala'
global_countries = None
global_countries = copy.copy(countries)
countries[0] = 'Honduras'

for country in countries:
    print(country)
