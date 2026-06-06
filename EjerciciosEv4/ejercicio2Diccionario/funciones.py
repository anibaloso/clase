alumnos={}

# funcion para agregar un alumno
def agregar_alumno():
    
    while True:
        alumno=input("Ingrese nombre del alumno: ").strip()
        if alumno=="":
            print("El nombre del alumno no puede estar vacio. Intentelo nuevamente")
        elif alumno.isdigit():
            print("Solo pueden ser letras. Intentelo nuevamente")
        elif alumno in alumnos:
            print("Este alumno ya existe. Intentelo nuevamente")
            
        else:
            while True:    
                try:
                    cantidadNotas=int(input("cuantas notas quiere registrar: "))
                    if cantidadNotas<=0:
                        print("La cantidad de notas solo puede ser un entero mayor que 0")
                except ValueError:
                    print("Error, Solo puede ser un dígito")

                else:
                    notas=[]
                    for i in range(cantidadNotas):
                        while True:
                            try:
                                nota=float(input(f"Ingrese la nota {i+1} : "))
                                if nota>=1.0 and nota<=7.0:
                                    notas.append(nota)
                                    break
                                else:
                                    print("La nota solo puede ser entre 1.0 y 7.0")
                            except ValueError:
                                print("Error, la nota solo puede ser un digito")
                                continue
                    alumnos[alumno]=notas    
                    print(f"El alumno {alumno} fue agregado correctamente")
                    return alumnos

# se crea funcion para validar nota
# def validaNota():
#     while True:
#         try:
#             nota=float(input(f"Ingrese la nota {i+1} : "))
#             if nota>=1.0 and nota<=7.0:
#                 notas.append(nota)
#                 break
#             else:
#                 print("La nota solo puede ser entre 1.0 y 7.0")
#         except ValueError:
#             print("Error, la nota solo puede ser un digito")
#             continue



# funcion para mostrar todos los alumnos    
def mostrar_alumnos():
    if not alumnos :
        print("Aun no hay ningun alumno registrado")
    else:
        for alumno in alumnos:
            print(f"Alumno {alumno}, notas: {alumnos[alumno]}")


# ********************************************************************************************
# funcion mostrar alumnos con parametro
# def mostrar_alumnos(alumnos):
#     if not alumnos :
#         print("Aun no hay ningun alumno registrado")
#     else:
#         for alumno in alumnos:
#             print(f"Alumno {alumno}, notas: {alumnos[alumno]}")
# ********************************************************************************************



# funcion para mostrar los promedios de los alumnos
def ver_promedios():
    if not alumnos :
        print("Aun no hay ningun alumno registrado")
    else:
        for alumno in alumnos:
            sumaNotas=0
            for nota in alumnos[alumno]:    
                sumaNotas=sumaNotas+nota
            promedio=sumaNotas/len(alumnos[alumno])
            print(f"El alumno {alumno} tiene promedio: {promedio}")
        

# ********************************************************************************************
# funcion para mostrar los promedios de los alumnos
# def ver_promedios(alumnos):
#     if not alumnos :
#         print("Aun no hay ningun alumno registrado")
#         return
#     for alumno in alumnos:
#         promedio=sum(alumnos[alumno])/len(alumnos[alumno])
#         print(f"El alumno {alumno} tiene promedio: {round(promedio,2)}")
# ********************************************************************************************
        

# funcion para mostrar el mejor promedio de los alumnos
def mejor_alumno():
    if not alumnos :
        print("Aun no hay ningun alumno registrado")
    else:
        mejorPromedio=0
        mejorAlumno=""
        for alumno in alumnos:
            promedio=0
            for nota in alumnos[alumno]:
                promedio=promedio+nota
            promedio=promedio/len(alumnos[alumno])
            if mejorPromedio<promedio:
                mejorPromedio=promedio
                mejorAlumno=alumno
        print(f"el mejor alumno es {mejorAlumno} con promedio {mejorPromedio}")

# funcion para mostrar la cantidad de alumnos aprobados
def cantidad_aprobados():
    if not alumnos :
        print("Aun no hay ningun alumno registrado")
    else:
        aprobados=0
        for alumno in alumnos:
            promedio=0
            for nota in alumnos[alumno]:
                promedio=promedio+nota
            promedio=promedio/len(alumnos[alumno])
            if promedio>=4.0:
                aprobados+=1       
        print(f"La cantidad de alumnos aprobados es : {aprobados}")