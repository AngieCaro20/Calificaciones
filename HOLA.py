print("Hola Mundo")
#mini sistema de regitro de calificaiones 

#Memoria estatica (inmutable)
#Tupla que no cambia con los cursos del semestre 
cursos = ("Matematias", "Fisica", "Programacion", "Estadistica")

#nombre del estudiante no cambia 
estudiante = "Sara Rodriguez"


#Mamoria dinamica (mutable)
#Lista donde se guardan las calificaciones de cada curso 
calificaciones = []

#Pedir al usurio las notas de cada curso 
for curso in cursos:
    nota=float(input(f"Ingrese la nota de {curso}: "))
    calificaciones.append(nota)

print("\n Calificaciones iniciales registradas: ", calificaciones)


#Menu interactivo (permite interactuar hasta que el usuario decida salir.) 
while True:
    print("\n  Menu de opciones")
    print("1. Ver calificaciones")
    print("2. Modificar la calificacion")
    print("3. Eliminar la calificacion")
    print("4. Calucular el promedio")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    #Opcion 1 
    if opcion == "1":
        print(f"\n Calificaciones de {estudiante}:")
        for i, curso in enumerate(cursos):
            #enumerate da el indice o el valor (se usa para mostrar cursos con número y su nota.)
            print(f"{i+1}. {curso}: {calificaciones[i]}")

    #Opcion 2 
    elif opcion == "2":
        indice = int(input("Ingrese el nombre del curso que va a modificar: ")) -1
        if 0 <= indice < len(calificaciones):
            nueva_nota = float(input("Ingrese la nueva nota:" ))
            calificaciones[indice] = nueva_nota
            print("Calificacion modificada con exito. ")
        else:
            print("Curso no valido. ")

    #Opcion 3
    elif opcion == "3":
        indice = int(input("Ingrese el numero del curso que va a eliminar: ")) -1
        if 0 <= indice < len(calificaciones):
            calificaciones[indice] = None  #Se coloca None para no perder el orden de curso-calificacion
            print("Calificacion eliminada (ahora es None). ")
        else:
            print("Curso no valido. ")

    #Opcion 4 
    elif opcion == "4":
        #Solo se toman las notas que no sean None
        notas_validas =[n for n in calificaciones if n is not None]
        if notas_validas:
            promedio = sum(notas_validas) / len(notas_validas)
            print(f"El promedio final de {estudiante} es: {promedio: .2f}")
        else:
            print("No hay calificaciones registradas. ")

    #Opcion 5
    elif opcion == "5": 
        print("Saliendo del sistema..... ") 
        break

    #Si la opcion no existe 
    else: 
        print("Opcion no valida, intente de nuevo :) ")
