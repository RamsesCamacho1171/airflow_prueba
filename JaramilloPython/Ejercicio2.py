valores = [8, 30, 30, 50, 86, 94, 102, 110, 169, 170,
           176, 236, 240, 241, 242, 255, 262, 276, 279, 282]

intervalo = 6


valores_ordenados = sorted(valores)

numero_mayor = valores_ordenados[-1]
numero_menor = valores_ordenados[0]

intervalo_suma = numero_menor

Amintervalo = (numero_mayor-numero_menor) / intervalo


Amintervalo_redondeado = round(Amintervalo)

Amintervalo_entero = int(Amintervalo_redondeado)


print("Amplitun del intervalo", Amintervalo_entero)



total_valores = 0

for i in range(intervalo):
    intervalo_final = intervalo_suma + Amintervalo_entero
    contador = 0
    for valor in valores:
        if intervalo_suma <= valor < intervalo_final:
            contador += 1
            total_valores += 1
    frecuencia_relativa = contador / len(valores)
    print("Intervalo inicial y final", ":", intervalo_suma, "-", intervalo_final,
          "Frecuencia absoluta:", contador, "Frecuencia relativa:", frecuencia_relativa)
    intervalo_suma = intervalo_final

print("Total de valores en todos los intervalos:", total_valores)
