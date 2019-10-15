'''
Dada las siguientes placas, filtrar aquellas que pertenecen a las provincias de :

Loja, Pichincha, Esmeraldas, Azuay, Imbabura

 

Placas: lba-001, gma-002, azx-003, ess-004,  oro-100, mab-001, iaj-002
'''

#Creacion de una funcion
def es_placa(x):
	inicial = ["l", "p", "a", "e", "i"]
	#ieraciones tomando la posicion 0 de la variable
	if x[0] in inicial:
		return True
	else:
		return False

placas = ["lba-001", "gma-002", "azx-003", "ess-004", "oro-100", "mab-001", "iaj-002"]

#Uso de la funcion dentro de otra 
resultado = filter(es_placa, placas)
print(list(resultado))



