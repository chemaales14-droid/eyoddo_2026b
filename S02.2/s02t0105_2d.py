from array import array as arr

table = [
    arr('i', [1,2,3]),
    arr('i', [4,5,6]),
    arr('i', [7,8,9]),
]

# Imprimiendo cada elementos
def print_table (input_table):
  for row in table:
    for column in row:
        print(column, end=",")
    print("\b ")


table=[


   
arr("i",[1,2,3]),
arr("i",[4,5,6]),
arr("i",[7,8,9]),

]
print_table (table)
#insercion
row=1
coulumn=2
value=99

#insertar en la fila corchete
table [row].insert(coulumn,value)

print ("Después de la inserción:")
print_table (table)

# Imprimiendo mensaje
print("--- Despues de la insercion de la fila---")
print_table(table) #DRY  

# Eliminacion de elementos
del table[2]

# Imprimiendo mensaje
print("--- Despues de la eliminacion de la fila 2 ---")
print_table(table) #DRY