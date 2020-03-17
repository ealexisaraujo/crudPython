>>> lista_de_numeros = list(range(100))
>>> lista_de_numeros
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> pares = [numero for numero in lista_de_numeros if numero % 2 == 0]
>>> student_uid = [1, 2, 3]
>>> students = ['Juan', 'Jose', 'Larsen']
>>> students_with_id = {uid: student for uid, student in zip(student_uid, students)}
>>> students_with_id
{1: 'Juan', 2: 'Jose', 3: 'Larsen'}
>>>
>>>
>>>
>>> import random
>>> random_numbers = []
>>> for i in range(10):
...     random_numbers.append(random.randint(1,3))
...
>>> random_numbers
[3, 1, 1, 2, 3, 2, 1, 1, 2, 1]
>>> non_repeated = {number for number in random_numbers}
>>> non_repeated
{1, 2, 3}
