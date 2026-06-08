import funciones as fn

alumnos={}

while True:
    print("Menu alumnos")
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Ver promedios")
    print("4. Mejor alumno")
    print("5. Cantidad de aprobados")
    print("6. Salir")
    while True:
        try:
            opcion=int(input("Ingrese una opcion 1-6: "))
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
        print("Hasta luego.")
        break
    else:
        print("Seleccion invalida,intentelo nuevamente")