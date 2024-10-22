print("-Calculo total de peso del ultimo pedido-")

nmunecas = int(input("Introduce el numero de muñecas"))
npayasos = int(input("Introduce el numero de payasos"))

gmunecas = 75
gpayasos = 115

pesoTotal = ((nmunecas*gmunecas)+(npayasos*gpayasos))

print("El peso total del pedido :",
       str(pesoTotal), "g")
      