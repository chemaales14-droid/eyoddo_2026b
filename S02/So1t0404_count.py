# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack'] # o(n)

def random_function(students):    #0(1)
    first = students[0] # 0(n)
    total = 0 # 0(1)
    new_list = [] # o(1)

    for student in students:
        total += 1 # o(1)
        new_list.append(student) # o(n)

    print(new_list) # 0(n)
    return total # 0(1)

print(random_function(student_list_01))

# Calcular O(n)