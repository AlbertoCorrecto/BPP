import csv
import pandas as pd



lst = []
lst_def = []

try:
    with open('finanzas2020.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            lst.append(row[0].split())
except:
    print("El archivo no se pudo abrir, quizas no exista, o tenga un nombre diferente.")
try:
    len(lst) == 12
except:
    print("La primera fila no tiene 12 columnas.")


lst_def.append(lst[0])

for row in range(1,len(lst)):
    new_row = []
    for item in lst[row]:
        try:
            new_row.append(int(item))
        except:
            new_row.append(0)
        try:
            len(new_row) == 12
        except:
            print("Alguna de las filas no tiene 12 columnas.")
    lst_def.append(new_row)

# Aqui ya tengo una lista definitiva, con todas las listas año por año
# A partir de aqui se resolveran los ejercicios, pero antes pasemos a df nuestros datos

df = pd.DataFrame(columns = lst_def[0])
for row in range(1,len(lst)):
    df.loc[row] = lst_def[row]

# print(df)

# Que mes se ha gastado mas

maximo_gasto = 0
maximo_mes = ''

gastoMes = [] # Esta variable se usara mas adelante

for mes in lst_def[0]:
    gasto = abs(df[mes][df[mes] < 0].sum())
    gastoMes.append(gasto)
    print(f'\nEn {mes} se ha gastado en total {gasto}€')
    if gasto > maximo_gasto:
        maximo_gasto = gasto
        maximo_mes = mes

print("\n================================================================================")
print(f'El mes que mas se ha gastado ha sido {maximo_mes}, en el cual hubo un gasto de {maximo_gasto}€.')

# Que mes ha producido mas

maximo_prod = 0
prodMes = [] # Esta variable se usara mas adelante

for mes in lst_def[0]:
    prod = abs(df[mes][df[mes] > 0].sum())
    prodMes.append(prod)
    print(f'\nEn {mes} se ha producido en total {prod}€')
    if prod > maximo_prod:
        maximo_prod = prod
        maximo_mes = mes

print("\n================================================================================")
print(f'El mes que mas se ha producido ha sido {maximo_mes}, en el cual hubo un gasto de {maximo_prod}€.')


# Que mes se ha ahorrado mas (es decir el mes mas positivo, contando gastos y dinero producido)

ahorro_max = 0

for mes in lst_def[0]:
    ahorro = (df[mes].sum())
    print(f'\nEn {mes} se ha ahorrado en total {ahorro}€')
    if ahorro > ahorro_max:
        ahorro_max = ahorro
        maximo_mes = mes

print("\n================================================================================")
print(f'El mes que mas se ha ahorrado ha sido {maximo_mes}, en el cual hubo un ahorro de {ahorro_max}€.')


# Cual ha sido la media de gastos del año y el gasto total
gastoMedia = 0
for i in range(0,11):
    gastoMedia += gastoMes[i]

print("\n================================================================================")
print(f"El gasto total del año es {gastoMedia}€")

gastoMedia = gastoMedia/12

print("\n================================================================================")
print(f"El gasto medio del año es {gastoMedia}€")


# Cual han sido los ingresos totales en el año

prodAnual = 0
for i in range(0,11):
    prodAnual += prodMes[i]



print("\n================================================================================")
print(f"Los ingresos totales del año son {prodAnual}€")


