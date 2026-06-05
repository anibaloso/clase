alumnos={}

def agregar_alumno():
    alumno=input("Ingrese nombre del alumno: ")
    cantidadNotas=int(input("cuantas notas quiere registrar: "))
    notas=[]
    for i in range(cantidadNotas):
        nota=float(input(f"Ingrese la nota {i+1} : "))
        notas.append(nota)
    alumnos[alumno]=notas    
    print(f"El alumno {alumno} fue agregado correctamente")
    return alumnos
    
def mostrar_alumnos():
    for alumno in alumnos:
        print(f"Alumno {alumno}, notas: {alumnos[alumno]}")
    
def ver_promedios():
    for alumno in alumnos:
        sumaNotas=0
        for nota in alumnos[alumno]:    
            sumaNotas=sumaNotas+nota
        promedio=sumaNotas/len(alumnos[alumno])
        print(f"El alumno {alumno} tiene promedio: {promedio}")
    
    return promedio
    
    
def mejor_alumno():
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


def cantidad_aprobados():
    aprobados=0
    for alumno in alumnos:
        promedio=0
        for nota in alumnos[alumno]:
            promedio=promedio+nota
        promedio=promedio/len(alumnos[alumno])
        if promedio>=4.0:
            aprobados+=1       
    print(f"La cantidad de alumnos aprobados es : {aprobados}")