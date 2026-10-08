"""
Escribe un programa que calcule 
la suma de los "n" numeros naturales.
por ejemplo si n = 100, el programa
claculara la suma del 1 al 100
42
"""
# import biblioteca time
import time
#funcion que suma los primeros n numeros naturales 
def sum_of_n(n):
    total_sum = 0
    #sumamos los n numeros
    # ciclo for
    for number in range(1,n+1):
        total_sum = total_sum + number 
        #retornando  total de la suma 
    return total_sum
   


#variable para guardad el data set
dataset =[]
for  repetition in range (1,11):
    #tomo tiempo 1
    # tomando el tiempo inicial
    timestamp_01 = time.time()
    #sumo los n numeros 
    n= repetition * 500
    #guardo el resultado
    reuslt =sum_of_n(n)

    #toma de tiempo
    timestamp_02 = time.time()

    #calculando tiempo
    elaps_time=  round ((timestamp_02-timestamp_01)*1e6,2)

    # agreagar la tripleta de los datos al datasset
    dataset.append ((n,elaps_time,reuslt))


for tup in dataset:
     print(tup)




