
#creacion de un funcion 
def es_vocal(x):
	#Creacuion de una lista 
	vocales = ["a", "e", "i", "o", "u"]
	#Ciclo que permite la iteracion de un dato en la lista anterior
	if x in vocales:
		#retorno d valores
		return True
	else:
		return False
datos=["e", "c", "u", "a", "d", "o", "r"]

resultado = filter(es_vocal, datos)
print(list(resultado))