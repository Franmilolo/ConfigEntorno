import random


numero = random.randint(1, 100)
intentos = 0

print("Adivina el numero del 1 al 100")


while True:
    try:
        adivinanza = int(input("Introduce tu numero: "))
        intentos += 1

        if adivinanza < 1 or adivinanza > 100:
            print("Elige un numero entre 1 y 100.")
        elif adivinanza < numero:
            print("Intenta con un numero mas alto.")
        elif adivinanza > numero:
            print("Intenta con un numero mas bajo.")
        else:
            print(f"¡Felicidades! Adivinaste el numero en {intentos} intentos.")
            break
    except ValueError:
        print("Introduce un número válido.")
