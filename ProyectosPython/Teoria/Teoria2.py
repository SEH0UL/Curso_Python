#Pedir algo al usuario
print("Escribe como te llamas:")
nombre = input()
print("En serio te llamas ", nombre, "????")

# Se puede usar la funcion input sin ayuda del print
anything = input("Dime lo que sea...")
print("Hmm...", anything, "...¿en serio?")

#no se debe utilizar como un argumento para operaciones matemáticas
# Para ello debemos declararle su tipo de valor
anything2 = float(input("Ingresa un número: "))
something = anything2 ** 2.0
print(anything2, "a la potencia de 2 es", something)

# AHORRAMOS CODIGO
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")
#El signo de * (asterisco), cuando es aplicado a una cadena y a un número (o a un número y cadena) se convierte en un operador de replicación:
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# PODEMOS PASAR NUMEROS A STRING CON LA FUNCION str(number)
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))


#Ejercicio para mostrar las horas
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
mins = mins + dura # encuentra el número total de minutos
hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
print(hour, ":", mins, sep='')
