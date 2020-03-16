# Las ** list comprehension **: son maneras de escribir listas, diccionarios y conjuntos de manera compacta y legible,
# Listas—> [element for element in element_list if element_meets_condition]
# Diccionarios–> {key: element for element in element_list if element_meets_condition}
# Conjuntos–> {element for element in element_list if elements_meets_condition}

# EJEMPLOS:

# - Generar lista de números de 1 al 100 y obtener los números pares(divisibles por dos):
import random
lista_de_numeros = list(range(100))
pares = [numero for numero in lista_de_numeros if numero % 2 == 0]
# **pares = [numero for numero in lista_de_numeros if numero % 2 == 0] —> list comprehension **

# -Generar diccionario a partir de dos listas:
student_uid = [1, 2, 3]
students = ['Natalia', 'Luis', 'Juan']
students_and_uid = {uid: student for uid, student in zip(
    student_uid, students)}  # - -> {1: ‘Natalia’, 2: ‘Luis’, 3: ‘Juan’}

# -Crear un conjunto(set) de números que no estén repetidos a partir de una lista con números repetidos:
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 3))
random_numbers = [3, 3, 3, 3, 2, 2, 2, 2, 1, 2]
non_repeated = {number for number in random_numbers}  # —> {1, 2, 3}
