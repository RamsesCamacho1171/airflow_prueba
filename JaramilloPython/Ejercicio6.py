datos = [212,869,220,654,511,624,420,121,428,865,799,405,230,670,870,366,99,55,489,312,493,163,221,84,144,48,375,86,168,100]

media = sum(datos) / len(datos)

diferencias = [(dato - media) for dato in datos]

suma_cuadrados = sum([(dato - media)**2 for dato in datos])
desviacion_estandar = (suma_cuadrados / len(datos))**0.5

suma_cubos = sum([(dato - media)**3 for dato in datos])
sesgo = suma_cubos / ((len(datos) - 1) * desviacion_estandar**3)

print(sesgo)