
cant =  int(input('Ingrese la cantidad de nombres'))
delimitador = input('Ingrese la condición de inicio de las cadenas ')

for j in range(cant):
    
    array = input('Ingrese cadenas de texto separadas por comas y sin espacios ')
    array_sin_repetidos = list(set(array.split(',')))
    
    resultado = filter(lambda x: x.startswith(delimitador), array_sin_repetidos)
    print(delimitador)

print(list(resultado))
'''


array = input('Ingrese cadenas de texto separadas por comas y sin espacios ')
array_sin_repetidos = list(set(array.split(',')))
delimitador = input('Ingrese la condición de inicio de las cadenas ')
resultado = filter(lambda x: str(x).startswith(delimitador), array_sin_repetidos)
print(sorted(list(resultado)))

'''