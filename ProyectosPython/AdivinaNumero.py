secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
numUsuario = int(input("Introduce un número: "))

while secret_number != numUsuario:
    if secret_number != numUsuario:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")

    numUsuario = int(input("Introduce un número: "))

print("el numero  secreto es", secret_number)
print("¡Bien hecho, muggle! Eres libre ahora.")
print("¡Muy bien! ¡Has adivinado el número secreto!")