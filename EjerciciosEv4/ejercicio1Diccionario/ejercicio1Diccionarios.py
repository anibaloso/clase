import funciones as fn

# TODO:Validaciones obligatorias

# TODO:El nombre del producto no puede estar vacio.
# TODO:No se debe permitir agregar un producto repetido.
# TODO:El stock debe ser un numero entero mayor o igual a 0.
# TODO:El precio debe ser un numero mayor que 0.
# TODO:La opcion del menu debe estar entre 1 y 5.
# TODO:Si no existen productos registrados, las opciones mostrar, buscar y producto mas caro deben indicarlo correctamente

productos={}
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
        producto=input("Ingrese nombre del producto: ")
        stock=int(input("Ingrese el stock del producto: "))
        valor=int(input("Ingrese el valor del producto: "))
        productos=fn.agregandoProducto(producto,stock,valor)

    elif opcion==2:
        print(productos)

    elif opcion==3:
        nombre=input("Ingrese el producto que desea buscar: ")
        print(fn.buscarProducto(nombre))

    elif opcion==4:
        print(fn.productoMasCaro())
    elif opcion==5:
        print("Saliendo gracias por usar nuestro programa")
        break
    else:
        print("Ingrese una opcion valida")
