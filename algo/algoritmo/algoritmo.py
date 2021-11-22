import matplotlib.pyplot as plt
'''Vamos en primer lugar a importar la libreria matplotlib, pues el proposito de este codigo es mostrar las graficas 
de un cierto algoritmo. Despues definiremos la funcion la cual recoge el algoritmo que queremos visualizar'''

def collatz(a):
    '''La funcion Collatz recibe una entrada, que es el numero a apartir del cual vamos a crear nuestra serie de valores.
    Nuestro algoritmo va a discernir primeramente si e numero introducido es par o impar.
    De ser par, nuestro numero se dividira entre 2.
    De ser impar, nuestro numero se multiplicara por 3 y luego se le sumara 1.
    Este proceso se repetira, hasta que nuestro numero alcance el valor de uno, generando asi una huella unica para cada
     numero.
     Por ejemplo:
     El valor 8 se dividira entre 2 dando 4, que igualmente al ser par se volvera a dividir entre 2,
     dando 2, que nuevamente se dividira entre 2 dando finalmente 1.
     El valor 3, se multiplicara por tres y se le sumara 1, dando 10, el cual es par, por lo que se dividira entre 2,
     obteniendo 5. Al ser 5 impar otra vez multiplicaremos por 3 y sumaremos 1, qudandonos 16, el cual se dividira
     entre 2 4 veces, hasta llegar a 1.
     La huella de estos numeros se almacenara en una lista, obteniendo asi para el 8 la lista [8,4,2,1],
     y para el 3 la siguiente lista [3,10,5,16,8,4,2,1]
     Esta lista sera nuestro return.'''
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

'''Implementamos un bucle para hacer una grafica de distintas listas obtenidas con la anterior funcion. 
Representando en el eje x el numero de iteracion, y en el eje y el valor numerico alcanzado en dicha iteracion.'''
for i in range(1,50):
    plt.plot(collatz(i), "-o")




'''Aplicamos un poco de formato para hacer la visiualizacion mas agradable.'''
plt.ylabel('Valor')
plt.xlabel('Iteracion')
plt.title("Algoritmo 3n+1",
          fontdict={'family': 'serif',
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 18})
plt.show()