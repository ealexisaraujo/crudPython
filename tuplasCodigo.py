# Declaracion de tuplas
a = 1, 2, 3
a = (1, 2, 3)
# Operaciones con tuplas:
# Acceder a un valor mediante indice de tupla
a[0] = 1
# Conteo de cuantas veces está un valor en la tupla
a.count(1)  # —> 1

# Declaración conjutos o Sets
a = set([1, 2, 3])
b = {1, 2, 3}
# Operaciones con conjuntos:

# NO se puede acceder a un valor mediante índice
# NO se puede agregar un valor ya existente, por ejemplo
# Agregar un valor a conjunto
a.add(1)  # —> error!! (valor existente en set)
a.add(20)  # —> a = {1, 2, 3, 20}
# Tenemos:
a = {1, 2, 3, 20}
b = {3, 4, 5}
a.intersection(b)  # –> {3}(elementos en común)
# (elementos de a + b pero sin repetir ninguno)
a.union(b)  # —> {1, 2, 3, 20, 4, 5}
a.difference(b)  # –> {1, 2, 20}  # (elementos de a que no se encuentran en b)
b.difference(a)  # –> {4, 5}  # (elementos de b que no se encuentran en a)
