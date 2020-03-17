print('>>> lista_de_numeros = list(range(100))')
lista_de_numeros = list(range(100))

print('>>> lista_de_numeros')
print (lista_de_numeros)

print('>>> pares = [numero for numero in lista_de_numeros if numero % 2 == 0]')
pares = [numero for numero in lista_de_numeros if numero % 2 == 0]

print('>>> student_uid = [1, 2, 3]')
student_uid = [1, 2, 3]

print('>>> students = [\'Juan\', \'Jose\', \'Larsen\']')
students = ['Juan', 'Jose', 'Larsen']

print('>>> students_with_id = {uid: student for uid, student in zip(student_uid, students)}')
students_with_id = {uid: student for uid, student in zip(student_uid, students)}

print('>>> students_with_id')
print(students_with_id)


print('>>>\n>>>\n>>>')
print('>>> import random')
import random

print('>>> random_numbers = []')
random_numbers = []

print('>>> for i in range(10):')
print('...     random_numbers.append(random.randint(1,3))')
print('...')
for i in range(10):
    random_numbers.append(random.randint(1,3))

print('>>> random_numbers')
print(random_numbers)

print('>>> non_repeated = {number for number in random_numbers}')
non_repeated = {number for number in random_numbers}

print('>>> non_repeated')
print(non_repeated)