
def mi_decorador(funcion):  # suma
     def nueva_funcion(a, b):  # 1, 2
         print("Se va a llamar")
         c = funcion(a, b)  # suma(1, 2)
         print("Se ha llamado")
         return c  # 3
     return nueva_funcion

@mi_decorador
def suma(a, b):
     print("Entra en funcion suma")
     return a + b

print(suma(1,2))