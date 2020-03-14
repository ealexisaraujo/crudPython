>>> country = 'Colombia'

>>> country[0]
C
>>> country[1]
o
>>> country[-1]
a
>>> country[-2]
i
>>> len(country)
8
>>> country[0]
C
>>> country[1]
o
>>> country[2]
l
>>> country[3]
o
>>> country[4]
m
>>> country[5]
b
>>> country[6]
i
>>> country[7]
a
>>> country[1]
o
>>> second_letter = country[1]
>>> print( second_letter )
o
>>> id( second_letter )
140375975117616
>>> other_var = 'o'
>>> id( other_var )
140375975117616
>>> id( 'i' )
140375975324720
>>> id( 'C' )
140375975041776
>>> id( 'c' )
140375975762864
>>> country = 'México'
>>> id(country)
140375974214912
>>> country += 's'
>>> country
Méxicos
>>> id(country)
140375974215152
