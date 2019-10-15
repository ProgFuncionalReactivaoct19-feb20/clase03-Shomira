

'''
usos del filter y la funcion anonima lambda
'''

datos = [1, 2, 10, 11, 12, 13]
#iteracio9nes mediante la funcion y filtra los numeros que su residuo es cero
resultado = filter(lambda x: x % 2 == 0, datos)
print(resultado)
#Es necesario usar una lista para poder entender lo que se a filtrado
print(list(resultado))