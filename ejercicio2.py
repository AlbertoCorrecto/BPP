# Como en la actividad 1 no tengo funciones, voy a crear aqui unas cuantas con las que testear pytest

# 1) Esta es una función básica de suma
def suma(a, b):
  return a + b

# 2) Esta es una función básica de resta
def resta(a,b):
    return a - b

# 3) Esta es una función básica de multiplicación
def multiplicacion(a, b):
    return a * b

# 3) Esta es una función exponencial, el primer termino indica la base y el segundo el exponente
def exp(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result

# 4) Conjetura de Collatz: Esta se basa en; si el numero es par divido entre 2, y si es impar multiplico por 3 y sumo 1
# El objetivo es tener la lista de numeros por las q pasa, pues cada lista es diferente (grafo)

def collatz(a):
    result = [a]
    if a % 2 == 0:
        result.append(a/2)
    else:
        b = (a * 3) + 1
        result.append(b)
    while result[-1] != 1:
        if result[-1] % 2 == 0:
            result.append(result[-1] / 2)
        else:
            b = (result[-1] * 3) + 1
            result.append(b)
    return result