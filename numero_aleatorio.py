import random


def adivina_el_número(x):

    print("========================")
    print(" ¡Bienvenid@s al juego! ")
    print("========================")
    print("Tu objetivo es adivinar el numero secreto entre 1 y 10")

    número_aleatorio = random.randint(1, x) #numero aleatorio entre 1 y x inclusive

    pred = 0
    
    while pred != número_aleatorio:
        # Se le pide al usuario ingresar un número
        pred = int(input(f"Adivina el número entre 1 y {x}: ")) # f-string

        if pred < número_aleatorio:
            print("Intenta otra vez. Este número es muy pequeño.")
        elif pred > número_aleatorio:
            print("Intenta otra vez. Este número es muy grande.")

    print(f"¡Felicitaciones! Adivinaste el número {número_aleatorio} correctamente")


adivina_el_número(10)
          
        
        
        
       
