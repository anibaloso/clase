def agregar_alumno(alumnos):
    while True:
        nombre=input("Ingrese nombre del alumno: ")
        if nombre=="":
            print("El nombre no puede estar vacio")
        elif nombre.isdigit():
            print("El nombre solo pueden ser letras")
        else:
            break
    while True:    
        try:
            cantidadNotas=int(input("Cuantas notas va a ingresar: "))
            break
        except ValueError:
            print("Error, Solo pueden ser numeros la cantidad de notas")
            
    notas=[]
    for i in range(cantidadNotas):
        while True:
            try:
                nota=float(input(f"Ingrese la nota {i+1}: "))
                if nota>=1.0 and nota<=7.0:
                    break
                else:
                    print("La nota solo puede ser entre 1.0 y 7.0")
            except ValueError:
                print("Error, solo pueden ser digitos")
        notas.append(nota)
    alumnos[nombre]=notas
    print("Alumno agregado correctamente")
    
def mostrar_alumnos(alumnos):
    
    if not revision_alumnos(alumnos):
        return
    
    for alumno in alumnos:
        print(f"Alumno '{alumno}': {alumnos[alumno]}")
    
def ver_promedios(alumnos):
    if not revision_alumnos(alumnos):
        return
    for alumno in alumnos:
        promedio=promedio_alumno(alumnos,alumno)
        print(f"El promedio de {alumno} es {promedio:.2f}")
    
def mejor_alumno(alumnos):
    if not revision_alumnos(alumnos):
        return
    mejorPromedio=0
    mejorAlumno=""
    for alumno in alumnos:
        # normal
        # promedio=sum(alumnos[alumno])/len(alumnos[alumno])
        # intento funcion promedio
        promedio=promedio_alumno(alumnos, alumno)
        if promedio>mejorPromedio:
            mejorPromedio=promedio
            mejorAlumno=alumno
    print(f"El mejor alumno es {mejorAlumno} con promedio : {mejorPromedio:.2f}")
    

def cantidad_aprobados(alumnos):
    if not revision_alumnos(alumnos):
        return
    alumnosAprobados=0
    for alumno in alumnos:
        promedio=promedio_alumno(alumnos, alumno)
        if promedio>=4.0:
            alumnosAprobados+=1
    print(f"La cantidad de aprobados son : {alumnosAprobados}")

# -------------------funciones auxiliares---------------------------

def revision_alumnos(alumnos):
    """
    Revisa el diccionario si hay algun registro
    
    Parámetros:
        alumnos (dict): Diccionario que almacena alumnos y sus notas.
    
    """
    if alumnos=={}:
        print("Aun no hay registros de alumnos")
        return False
    return True

def promedio_alumno(alumnos,alumno):
    """
    Calcula y retorna el promedio de las notas del alumno
    
    Parámetros:
        alumnos (dict): Diccionario que almacena alumnos y sus notas.
        alumno (str): Nombre del alumno cuyo promedio se quiere calcular.
    
    Retorno:
        float: Promedio de las notas del alumno
    
    """
    return sum(alumnos[alumno])/len(alumnos[alumno])
