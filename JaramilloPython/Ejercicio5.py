import statistics

data=[ 62000,64000,49000,324000,1264000,54330,64000,51000,55000,48000,53000]

# Convertir cada elemento de la lista a un número entero
data = [int(x) for x in data]

# Calcular la media de los datos
media = statistics.mean(data)

# Calcular la moda de los datos
moda = statistics.mode(data)

# Calcular la mediana de los datos
mediana = statistics.median(data)

# Imprimir los resultados
print("La media es:", media)
print("La mediana es:", mediana)
print("La moda es:", moda)
