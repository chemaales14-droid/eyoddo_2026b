from array import array as arr


from s02t0102_1_d import print_array

my_array = arr('i',[2,10,15,20,80])

#antes de la insercion 
print ("antes de a insercion")
print_array(my_array)


# ver  como se hace una incersion 
my_array.insert(1,90)
print("despues de la insercion")
print_array(my_array)


print("simulacion con appen")
my_array.insert(len (my_array),9000)
print_array(my_array)