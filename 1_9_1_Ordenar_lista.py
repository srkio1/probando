#ordenar lista
lista = [5,2,76,44,7,32]
lista.sort()
print(lista)
listaLetras = ["a", "e", "o", "u" ,"i", "p", "r" , "c"]
listaLetras.sort()
print(listaLetras)
#multiplicar los elementos de una lista
listaNumerica = [2,6,8,33,67,23,1,9]
resultado = [3*x for x in listaNumerica]  # multiplica cada numero de la lista x 3
print(resultado)

listaA = ["a", "of" , "word" , "list"]
listaB = [s.upper() for s in listaA] #coloca todos los elementos de la lista A en mayuscula
listaC = [s for s in listaA  if len(s)<= 2]
listaD = [s for s in listaA if 'w' in s]
print(listaA)
print(listaB)
print(listaC)
print(listaD)