nombre = input("Ingrese su Nombre:")
l_nombre = nombre.lower()
edad = int(input("Ingrese su edad"))
calculo = 100 - edad
if 1 <= edad < 100:
    print(l_nombre, "tienes", edad, "y te falta", calculo, "para llegar a 100")
elif edad >= 100:
   print(l_nombre, "ya tienes 100 años")
