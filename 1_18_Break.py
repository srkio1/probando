

lista = [1,2,3,4,5,6,"mensaje",8,4,2]
indice=0
while indice< len(lista):
    print(lista[indice])
    if indice == 3:
        break # hace que finalice la condicional cuando el indice es igual a 3
    else:
        indice +=1
else:
    print("while finalizado")


lista2=[1,2,3,5,"cinco","camion", 28]
for elementoLista in lista2:
    print(elementoLista)
    if elementoLista == 5:
        break

