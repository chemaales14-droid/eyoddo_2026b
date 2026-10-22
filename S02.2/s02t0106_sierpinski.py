from array import array as arr   #imprta la bilblioteca importa la herramienta de la biblioteca y la renombra

rows=3

columns=2*rows-1

#crando grid2d
matriz=[]

#construllendo el grid
for _ in range(rows):
    new_row=arr('i',[0]*columns)
    matriz.append(new_row)#appen insertar datos

#validando la construccion del grid
print (f"cantidad de filas:{len(matriz)}")
print (f"cantidad de columnas:{len(matriz[0])}")

for row in matriz:
 print(list(row))
