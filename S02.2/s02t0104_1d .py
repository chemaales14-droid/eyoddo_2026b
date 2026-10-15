from array import array as arr


from s02t0102_1_d import print_array

my_array = arr('i',[2,10,15,20,10])

#antes de la eliminacion
print ("antes de la eliminacion")
print_array(my_array)


# ver  como se hace una eliminacion
try:
 my_array.remove (100)
except:
 print(f"no se encuentra  el arreglo")
print("despues de la eliminacion")
print_array(my_array)


