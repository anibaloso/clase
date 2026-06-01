# Tienda necesita crear inventario y la informacion 
# debe almacenarse en un diccionario
# ejemplo
# productos = {
#     "Mouse": [10, 15000],
#     "Teclado": [5, 25000],
#     "Monitor": [3, 180000]
# }

# debe tener un menu que sea asi 
# 1. Agregar producto
# 2. Mostrar productos
# 3. Buscar producto
# 4. Producto mas caro
# 5. Salir

productos={}
producto=""
stock=0
valor=0



def agregandoProducto(nombre,stock,precio):
    """Agrega producto nuevo 
    usando el "nombre":[stock,precio] """
    productos[nombre]=[stock,precio]
    return productos

print("--- Bienvenido al menu ---")
print("1. Agregar producto")
print("2. Mostrar productos")
print("3. Buscar producto")
print("4. Producto mas caro")
print("5. Salir")
opcion=int(input("Ingrese una opción 1-5"))

if opcion==1:
    producto=input("Ingrese nombre del producto")
    stock=int(input("Ingrese el stock del producto"))
    valor=int(input("Ingrese el valor del producto"))
    agregandoProducto(producto,stock,valor)
elif opcion==2:
    print(productos)
elif opcion==3:
    print("buscando producto")
elif opcion==4:
    print("producto mas caro")
elif opcion==5:
    print("Saliendo gracias por usar nuestro programa")
else:
    print("Ingrese una opcion valida")
