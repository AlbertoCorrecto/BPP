## Apartado 1:
from functools import reduce

lista = [[2,4,1], [1,2,3,9,4,5,6,7,8], [100, 250, 43]]

#item = [item for i in lista for item in range(len(i)) if item % 2 == 0]

'''for i in lista:
    max = i[0]
    for a in i:
        if max < a:
            max = a
    print(max)'''

for i in lista:
    max = [i[0]]
    max = [numero for numero in i if max[-1] < numero]
    print(max)
print("*****************************************************\n")
# Con reduce si lo veo claro

def elige(a, b):
    if a < b:
        return b
    else:
        return a


maximos = [reduce(elige, i) for i in lista]
print(f"Los maximo son {maximos}")



## Apartado 2:

def es_primo(n):
    primo = True
    for i in range(2,n):
        if n%i == 0:
            primo = False
    return primo

lista2 = [3, 4, 8, 5, 5, 22, 13]

primos = list(filter(es_primo, lista2))
print(f"Los primos son {primos}")
