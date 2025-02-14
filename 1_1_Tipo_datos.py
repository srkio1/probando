#boolean
miBoolean = False
nombre = "Carlos"
numeroFlotante= 7.5
resultado = nombre == numeroFlotante #esto nos deberia volver falso
print(miBoolean)
print(f"el resultado es {resultado}")

#int
numero = 1
print(numero)

#String
miCadena = "Hola mundo"
print(miCadena)

#tupla
miTupla = (1,2,3,4)
print(miTupla)
print(type(miTupla))

#diccionario
diccionario = {"nombre": "Daniel"}
print(type(diccionario))
print(diccionario)

#lista
miListaNumerica=[1,2,3,4]
#lista flotante
listaFlotante = [2.8 , 3.9 ,6.9]
#lista boleana
listaBooleana = [True , False, 5== 8]
#lista generica
listaGenerica= [1,2, "Daniel",True, "daniel" == "mensaje2", 7.6 , {"nombre":"daniel"}]
print(f" es {miListaNumerica} es de tipo {type(miListaNumerica)}" )
print(listaGenerica[0:-1:1])
print(listaBooleana)
print(f"{listaGenerica} es de tipo {type(listaGenerica)}")

nuevaLista = listaGenerica
print(nuevaLista)
nuevaLista.append("nuevo elemento4")
print(nuevaLista)
nuevaLista.count(5)
print(nuevaLista)
