productos={}

# funcion que agrega producto
def agregandoProducto(nombre,stock,precio):
    """Agrega producto nuevo 
    usando el "nombre":[stock,precio] """
    if nombre in productos:
        print("ya se encuentra ese producto en la base de datos")
        return
    
    productos[nombre]=[stock,precio]
    print("Producto agregado correctamente")
    return productos

# funcion mostrar los productos

def mostrarProductos():
     """"Recorre la lista y muestra todos los productos"""
     producto=""
     if productos == {}:
          print("Aun no hay ningun registro guardado")
     else:
        for i in productos:
          print("Producto: ",i,": stock:",productos[i][0],", valor: $",productos[i][1])

# funcion para buscar un producto
def buscarProducto(nombre):
    """usando el nombre del producto como parametro se recorre 
    un ciclo for hasta encontrar el producto, o devolver un error"""
    
    revisarProductos()
    if revisarProductos()==True:
        if nombre in productos:
            print("Producto: ",nombre,
                ": stock:",productos[nombre][0],
                ", valor: $",productos[nombre][1])
      
# funcion para buscar producto mas caro
def productoMasCaro():
    """Recorrera dos ciclos for comparando y almacenando el mas caro"""
    productoCaro=""
    numMayor=0
    for i in productos:
            if productos[i][1] > numMayor:
                numMayor=productos[i][1]
                productoCaro=i
    return f"El producto con el valor mayor es : {productoCaro} a ${numMayor}"

# funcion para revisar si hay algun producto
def revisarProductos():
    if productos == {}:
          print("Aun no hay ningun registro guardado")
          return False
    return True
    