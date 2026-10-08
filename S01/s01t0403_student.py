# creando una lista de eestudiantes 
"""1.-identifico el tamaño de la entrada "n"
2.-es cuanto crece el numero de operaciones en 
algoritmos conforme crece el tamaño de entrada
agrego las big 0 indentificadas
teniendo en cuenta la cota superior 
 o(n)+ 4(1)=o(n+4)=o(n)

"""

student_list_01=["jordan","pipen","curry","sofia"]
student_list_02=["mike","saul","walter","jessy"]

# verificando la presencia de un estudiante 
def check_student(input_student,student_list):
    for student in student_list:
        if   input_student  == student:
            print("Estudiante encontrado")
            return student # o(1)
# si no encuentro al estudiante entonces 

        print ("Estudiante no enconttrado")#o(1)
        
        return None

# probando algoritmo 
check_student("walter",student_list_01)
