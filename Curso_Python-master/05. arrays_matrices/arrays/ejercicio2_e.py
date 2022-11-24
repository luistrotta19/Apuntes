A = [20, 15, 12, 11, 8, 4, 1]

# #Asignar el mínimo
maxi = 20
mini = maxi 

for i in A:
   if i < mini:
        mini = i

# # Imprimiendo el mínimo
print(f'El minimo del array es: {mini}')