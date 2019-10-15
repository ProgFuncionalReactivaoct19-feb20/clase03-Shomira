
'''
usos del lambda y de filter(Propias de python)

'''
datos = [18, 19, 20, 10, 11, 12]
#iteraciones mediante la funcion y filtra los numeros que sean >=18
resultado = filter(lambda x: x >=18 or x <=10, datos)
print(resultado)
#Es necesario usar una lista para poder entender lo que se a filtrado
print(list(resultado))