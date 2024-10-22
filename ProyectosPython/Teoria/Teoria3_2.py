# FOR
# Comienza su rango desde 0 y finaliza antes del valor del argumento
for i in range(10):
    print("El valor de i es", i) 

#LLevando 2 argumentos 1º Inicio y 2º Final
for i in range(2, 8):
    print("El valor de i es", i)


#El tercer argumento es un incremento para cada giro
#el valor predeterminado es 1
for i in range(2, 8, 3):
    print("El valor de i es", i)

#Ejercicio corto para usarlo
power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

#Ejercicio Mississippi
import time

for i in range(1, 6):
    print(i, " Mississippi")
    time.sleep(1)
print("FIN DEL PROGRAMA")

# break - ejemplo
print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo (SE SALTA ESA VUELTA DEL BUCLE)
print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")