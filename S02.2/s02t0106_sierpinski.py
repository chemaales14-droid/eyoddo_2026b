from array import array as arr   #imprta la bilblioteca importa la herramienta de la biblioteca y la renombra

rows=10

columns=2*rows-1
#funcion par a imprimir matriz
def print_matriz(input_matriz):

 for row in matriz:
   print(list(row))

#crando grid2d
matriz=[]

#construllendo el grid
for _ in range(rows):
    new_row=arr('i',[0]*columns)
    matriz.append(new_row)#appen insertar datos

#validando la construccion del grid
print (f"cantidad de filas:{len(matriz)}")
print (f"cantidad de columnas:{len(matriz[0])}")


#calculando el centro de la pirmera fila 
center=columns//2  #sehace divsion entere

# estableciendo el centro con 1
matriz[0][center]=1
# priemro es la filla(0)y lo otro es lomuna
#print_matriz(matriz)
#se calcula el resto de r matriz siguiendo la alogica del sierpinski 

print_matriz(matriz)
for row in range (1,rows):
    for col in range (0,columns):
          left_upper_cell=0
          right_upper_cell_upper_cell=0


       
       # print(f"[{row}_{col}]",end="")
   # print()
#si la columna es mayor a donde estamos es mayor a cero 
if col>0:
   left_upper_cell = matriz[row-1][columns-1]

   #si la columna esta un elemento antes de
   # 
   # 
   # 
   #  el borde derecho 
   if col <columns-1:
    right_upper_cell =  matriz[row-1][columns+1]
   #guardad arreglo
   if left_upper_cell !=  right_upper_cell :
      matriz[row][col]=1
   else:
       matriz[row][col]=0
print()
print_matriz(matriz)