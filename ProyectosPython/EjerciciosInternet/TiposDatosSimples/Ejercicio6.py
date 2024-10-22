peso = float(input("Introduce tu peso en kg:"))
altura = float(input("Introduce tu altura en m:"))

imc = round(peso / altura **2,2)
print("Tu IMC es: ", str(imc))