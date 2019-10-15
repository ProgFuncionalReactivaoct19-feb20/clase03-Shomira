
'''
Clase de funciones superiores .. se crea funciones
y luego se pe puede hacer el llamada a una funcion dentro de otra 

'''
def suma(a,b):
	return a+b

def producto(a,b):
	return a*b

def disparador (f,a,b):
	print(f(a,b))

disparador(producto,1,10)
disparador(suma,1,10)