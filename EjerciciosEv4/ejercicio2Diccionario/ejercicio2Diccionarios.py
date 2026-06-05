import funciones as fn
while True:
    # menu alumnos
    print("########## Menu #########")
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Ver promedios")
    print("4. Mejor alumno")
    print("5. Cantidad de aprobados")
    print("6. Salir")
    opcion=int(input("Ingrese una opcion de 1-6: "))
    if opcion==1:
        print("1. Agregar alumno")
        fn.agregar_alumno()
    elif opcion==2:
        print("2. Mostrar alumnos")
        fn.mostrar_alumnos()
    elif opcion==3:
        print("3. Ver promedios")
        fn.ver_promedios()
    elif opcion==4:
        print("4. Mejor alumno")
        fn.mejor_alumno()
    elif opcion==5:
        print("5. Cantidad de aprobados")
        fn.cantidad_aprobados
    elif opcion==6:
        print("Salimos")
        break        
    else:
        print("Escriba una alternativa correcta")