import random
print("Bienvenido al Juego Pidra Papel o Tijera")

#Se declara las variables para el juego.
opciones = ["piedra", "papel", "tijera"]

eleccion = input("Que opcion eliges? (piedra, papel, tijera): ").lower()

computador = random.choice(opciones)

#Definimos la funcion para el juego.
def juegoPiedraPapelTijera ():

    if eleccion not in opciones:
        print("Opcion no valida. Por favor, elige entre piedra, papel o tijera.")
        return
    
    if eleccion == computador:
        print("Ambos eligieron", eleccion + ". Es un empate.")

    elif (eleccion == "piedra" and computador == "tijera") or \
         (eleccion == "papel" and computador == "piedra") or \
         (eleccion == "tijera" and computador == "papel"):
        print("¡Ganaste!\n")
    else:
        print("Perdiste...\n")

#Llamamos a la funcion. 
print(juegoPiedraPapelTijera())



    
