total=int(input('ingrese el total de la cuenta: '))
propina=float(input('ingrese el porcentaje de propina que desea dejar: '))
resultado=int(total*(propina/100))
print('El total de la cuenta es',total)
print('con el',int(propina),'% de propina seria',resultado)
