productos={}
# funcion que agrega producto
def agregandoProducto(nombre,stock,precio):
    """Agrega producto nuevo 
    usando el "nombre":[stock,precio] """
    productos[nombre]=[stock,precio]
    return productos


# funcion para buscar un producto
def buscarProducto(nombre):
    """usando el nombre del producto como parametro se recorre 
    un ciclo for hasta encontrar el producto, o devolver un error"""

    for i in productos:
        if nombre in productos:
            return f"{nombre}", productos[nombre]
        else:
            return print("Producto no encontrado")

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