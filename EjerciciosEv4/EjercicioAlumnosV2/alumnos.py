import funciones as fn
import base_datos as bd
bd.crear_tabla()

alumnos={}

while True:
    print("Menu alumnos")
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Ver promedios")
    print("4. Mejor alumno")
    print("5. Cantidad de aprobados")
    print("6. ingresa un alumno con su curso")
    print("7. ingresa una nota al alumno por su id")
    print("8. muestra las notas de un alumno por su id")
    print("9. Salir")
    
    while True:
        try:
            opcion=int(input("Ingrese una opcion 1-9: "))
            break
        except ValueError:
            print("Error, solo pueden ser digitos, intentelo nuevamente")
    if opcion==1:
        fn.agregar_alumno(alumnos)
    elif opcion==2:
        fn.mostrar_alumnos(alumnos)
    elif opcion==3:
        fn.ver_promedios(alumnos)
    elif opcion==4:
        fn.mejor_alumno(alumnos)
    elif opcion==5:
        fn.cantidad_aprobados(alumnos)
    elif opcion==6:
        fn.agregar_alumno_db()
    elif opcion==7:
        fn.agregar_nota_alumno_db()
    elif opcion==8:
        fn.ver_notas_alumno_db()
    elif opcion==9:
        print("Hasta luego.")
        break
    else:
        print("Seleccion invalida,intentelo nuevamente")