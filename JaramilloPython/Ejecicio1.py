
valores = [124, 113, 98,58,78]

            

total = sum(valores)
acomulada=0
decimal=0
i=0

for  valor in valores:

    r_frecuencia = round((valor * 100) / total)
    
    acomulada += r_frecuencia

    decimal=r_frecuencia/100

    print("R frecuencia de la variable {}: {}".format(i+1, r_frecuencia),"%")
    i+=1
    print("R frecuencia acomulada: ", acomulada)
    print("R frecuencia decimal: ",decimal)


    
