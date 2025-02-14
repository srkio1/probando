#funcion sin parametro
def suma():
    numero1= int(input("ingrese un numero: "))
    numero2= int(input("ingrese un numero: "))
    numero3= int(input("ingrese un numero: "))
    resultado=numero1+numero2+ numero3
    print(resultado)

suma()

#funcion con parametro
def suma2(valorA, valorB, valorC):
    resultado = valorA + valorB + valorC
    print(resultado)

suma2(10,20,30)
