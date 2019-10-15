'''
Dadas las siguiente ciudades, filtrar aquellas que tienen un número par como longitud en sus caracteres.

Loja, Pichincha, Guayaquil, Zamora, Ibarra, Manabi, Machala,  Portoviejo, Macas
'''
#Lista de ciudades 
datos = ["Loja", "Pichincha", "Guayaquil", "Zamora",
 "Ibarra", "Manabi", "Machala", "Portoviejo", "Macas"]

#funcion lambda que filtra las palabras que su tamaño es un numero par
resultado = filter(lambda x: len(x) % 2 == 0, datos)
#imprimir el resultado de las palabras en una lista 
print(list(resultado))