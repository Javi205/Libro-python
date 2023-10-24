
# OPERADORES ARITMETICOS
a = 10
b = 3
suma = a + b
print(suma)
>> 13

# OPERADORES ARITMETICOS
a = 10
b = 3
resta = a - b
print(resta)
>> 7

# OPERADORES ARITMETICOS
a = 10
b = 3
multiplicacion = a * b
print(multiplicacion)
>> 30

# OPERADORES ARITMETICOS
a = 10
b = 4
division = a / b
print(division)
>> 2.5

# OPERADORES ARITMETICOS
a = 10
b = 4
division_entera = a // b
print(division_entera)
>> 2

# OPERADORES ARITMETICOS
a = 10
b = 2
modulo = a % b
print(modulo)
>> 0

# OPERADORES ARITMETICOS
a = 10
b = 3
potencia = a ** b
print(potencia)
>> 1000

############################################################################

# OPERADORES DE COMPARACION
a = 10
b = 5
c = "cinco"
d = 5.0

# Igualdad
print(a==b)  >> False #10 no es igual a 5
print(b==d)  >> True #5 es igual a 5.0
print(b==c)  >> False #5 no es igual a "cinco"
print(a==10) >> True #10 es igual a 10

# OPERADORES DE COMPARACION
a = 10
b = 5
c = "cinco"
d = 5.0

# Desigualdad
print(a!=b)  >> True #10 no es igual a 5
print(b!=d)  >> False #5 es igual a 5.0
print(b!=c)  >> True #5 no es igual a "cinco"
print(a!=10) >> False #10 es igual a 10


# OPERADORES DE COMPARACION
a = 10
b = 5
c = 5.0
d = "Manzana"
e = "Arroz"

# Mayor que
print(a>b) >> True #10 es mayor que 5
print(b>a) >> False #5 no es mayor que 10
print(b>c) >> False #5 no es mayor que 5.0
print(d>e) >> True #"Manzana" es mayor que "Arroz"
print(a>e) >> Error #No podemos comparar el valor de un string con un int o un float

# OPERADORES DE COMPARACION
a = 10
b = 5
c = 5.0
d = "Manzana"
e = "Arroz"

# Menor que
print(a<b) >> False #10 no es menor que 5
print(b<a) >> True #5 es menor que 10
print(b<c) >> False #5 no es menor que 5.0
print(d<e) >> False #"Manzana" no es menor que "Arroz"
print(a<e) >> Error #No podemos comparar el valor de un string con un int o un float


# OPERADORES DE COMPARACION
a = 10
b = 5
c = 5.0
d = "Manzana"
e = "Arroz"

# Mayor o igual que
print(a>=b) >> True #10 es mayor o igual que 5
print(b>=a) >> False #5 no es mayor o igual que 10
print(b>=c) >> True #5 es mayor o igual que 5.0
print(d>=e) >> True #"Manzana" es mayor o igual que "Arroz"
print(a>=e) >> Error #No podemos comparar el valor de un string con un int o un float

# OPERADORES DE COMPARACION
a = 10
b = 5
c = 5.0
d = "Manzana"
e = "Arroz"

# Menor o igual que
print(a<=b) >> False #10 no es menor o igual que 5
print(b<=a) >> True #5 es menor o igual que 10
print(b<=c) >> True #5 es menor o igual que 5.0
print(d<=e) >> False #"Manzana" no es menor o igual que "Arroz"
print(a<=e) >> Error #no podemos comparar el valor de un string con un int o un float

##############################################################################################

# OPERADORES LOGICOS
a = True
b = False
c = True
d = False

print(a and b) >> False #Solo una variable tiene el valor True
print(a and c) >> True #Ambas variables tienen el valor True
print(b and d) >> False #Ninguna variable tiene el valor True

# OPERADORES LOGICOS
a = True
b = False
c = True
d = False

print(a or b) >> True #Al menos una variable tiene el valor True
print(b or d) >> False #Ninguna variable tiene el valor True

# OPERADORES LOGICOS
a = True
b = False

print(not a) >> False #El valor opuesto de True es False
print(not b) >> True #El valor opuesto de False es True

##############################################################################################

# OPERADORES DE ASIGNACION

a = 10 # A la variable a se le asigna el valor 10

# OPERADORES DE ASIGNACION

a = 10
a += 2 #Se suman 2 a la variable y se reasigna su valor
print(a) >> 12

# OPERADORES DE ASIGNACION

a = 10
a -= 2 #Se restan 2 a la variable y se reasigna su valor
print(a) >> 8

# OPERADORES DE ASIGNACION

a = 10
a *= 2 #La variable se multiplica por 2 y se reasigna su valor
print(a) >> 20

# OPERADORES DE ASIGNACION

a = 10
a /= 2 #La variable se divide en dos y se reasigna su valor
print(a) >> 5

################################################################################################

# OPERADORES DE PERTENENCIA E IDENTIDAD

lista = [1, 2, 3, 4, 5]

print(3 in lista) >> True #3 si está presente en la lista
print(6 in lista) >> False #6 no está presente en la lista

print(6 not in lista) >> True #6 no esta presente en la lista
print(3 not in lista) >> False #3 si está presente en la lista

# OPERADORES DE PERTENENCIA E IDENTIDAD

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) >> False #a y b no son el mismo objeto en la memoria 
print(a is a) >> True #corresponde al mismo objeto en la memoria

print(a is not b) >> True #a y b no son el mismo objeto en la memoria
print(a is not a) >> False #corresponde al mismo objeto en la memoria
