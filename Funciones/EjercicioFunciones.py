# Funciones

def sumarDosNumeros():
    #esto me permite dar una explicacion ala funcion
    '''Esta funcion permite sumar dos números,        
    ingresados dentro de la funcion    
    '''


    num1=int(input("Ingrese numero 1: "))
    num2=int(input("Ingrese numero 2: "))

    suma=num1+num2

    print(f"la suma de {num1} + {num2} es = {suma}")

sumarDosNumeros()

def sumar(a,b):
    '''Esta funcion permite sumar dos números, 
    ingresados por parametros'''
    suma=a+b

    return suma            #lo que esta retornando es la funcion completa


res=sumar(4,5)
print(res)

num1=int(input("numero1"))
num2=int(input("numero2"))
res=sumar(num1,num2)
print(f"la suma es {res}")