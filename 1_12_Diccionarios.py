'''No tienen indices
Almacenan difrentes tipos de datos (Tipos , Listas , Diccionarios)
Cada Valor tiene una llave unica.'''

miDiccionario = {}
miDiccionario = dict()

#key: value
miDiccionario = {"auto": "Renault"}
diccionario2 = {"nombre": "Carlos", "apellido": "Ruiz", "hijos": 2}
print(diccionario2["hijos"])
diccionario2["hijos"] = 3
print(diccionario2)
diccionario2["Sueldo"]=5000
print(diccionario2.keys()) # imprime las llaves
print(diccionario2.values()) # imprime solo los valores
for llave , valor in diccionario2.items():
    print(llave , valor)

#Validar llave (get con segundo parametro)

data= diccionario2.get("nombre", 'No existe')
print(f"el valor de la llave nombre  es {data}")
