rango = int(input('Ingrese el rango de números a generar. '))  # 5

# Creando el generador de n números
def generador_numeros(ran):
    for numero in range(1,ran+1):
        if numero%2==0:
            yield numero


# Consumiendo el generador
for valor in generador_numeros(rango):
        print(f'Número producido -> {valor}')