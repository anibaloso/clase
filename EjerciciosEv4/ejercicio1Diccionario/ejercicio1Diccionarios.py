import funciones as fn

# productos={}
producto=""
stock=0
valor=0
opcion=0
while opcion!=5:
    print("--- Bienvenido al menu ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Producto mas caro")
    print("5. Salir")
    while True:
        try:
            opcion=int(input("Ingrese una opción (1-5): "))
            break
        except ValueError:
            print("Las opciones solo pueden ser numeros del 1 al 5")

    if opcion==1:
        while producto=="":    
            producto=input("Ingrese nombre del producto: ")
            if producto=="":
                print("El nombre del producto no puede estar vacio")
        while True:
            try:
                stock=int(input("Ingrese el stock del producto: "))
            except ValueError:
                print("El valor del stock solo puede ser numeros y enteros")
                continue
            if stock<0:
                print("El stock del producto debe ser entero y mayor o igual a 0")
            else:
                break
        while True:
            try:
                valor=int(input("Ingrese el valor del producto: "))
            except ValueError:
                print("el valor del producto solo puede ser numeros")
                continue
            if valor<=0:
                print("El valor del producto debe ser entero y mayor 0")
            else:
                break
        productos=fn.agregandoProducto(producto,stock,valor)
        producto=""

    elif opcion==2:
        fn.mostrarProductos()

    elif opcion==3:
        
        if not fn.revisarProductos():
            continue
        nombre=input("Ingrese el producto que desea buscar: ")
        fn.buscarProducto(nombre)


    elif opcion==4:
        
        if not fn.revisarProductos():
            continue
        print(fn.productoMasCaro())

    elif opcion==5:
        print("Saliendo gracias por usar nuestro programa")
        break

    else:
        print("Ingrese una opcion valida")
