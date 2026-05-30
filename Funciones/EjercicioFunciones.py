import funcionesDetalle as fn
# from funcionesDetalle import sumar                       //esta es otra forma de llamarlo

fn.sumarDosNumeros()

res=fn.sumar(4,5)
print(res)

num1=int(input("numero1"))
num2=int(input("numero2"))
res=fn.sumar(num1,num2)
print(f"la suma es {res}")