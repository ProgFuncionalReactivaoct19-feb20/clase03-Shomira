'''
dado un conjunto de palabras filtrar todas aquellas que sean palindromas
"oro", "pais", "ojo", "oso", "radar", "sol", "seres"
'''

palindromas= ["oro", "pais", "ojo", "oso", "radar", "sol", "seres", "shomira"]
#iteracio9nes mediante la funcion y filtra las palabras que si son palindromas
resultado = filter(lambda x: "".join(reversed(x)) == x, palindromas)
print(resultado)
#Es necesario usar una lista para poder entender lo que se a filtrado
print(list(resultado))


'''
cadena = "ecuador"
print("-".join(cadena)) ..se PARA LAS PALABRAS CON UN GUION 
print("%".join(reversed(cadena)))....SEPARA LAS PALABRAS CON UN %  PERO DEL LADO CONTRARIO
print("-".join(reversed(cadena)))...SEPARA LAS PALABRAS CON UN - PERO DEL LADO CONTRARIO


'''