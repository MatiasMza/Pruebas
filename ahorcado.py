# Proyecto basico de Python para probar ciclos

import random
import string 

from palabras import palabras
from diagramas import vidas_diccionario_visual


def obtener_palabra_valida(palabras):
    palabra = random.choice(palabras) # Seleccionamos una palabra al azar de un diccionario

    # si la palabra tiene un guion o un espacio, seguir seleccionando palabras al azar
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()

def ahorcado():

    print("===================================")
    print(" ¡Bienvenido al juego del ahorcado!")
    print("===================================")

    palabra = obtener_palabra_valida(palabras)
    letras_por_adivinar = set(palabra) # Letras que deben ser adivinadas
    abecedario = set(string.ascii_uppercase) # Conjunto de letras en el abecedario
    letras_adivinadas = set() # Letras que el jugador ha adivinado en el juego

    vidas = 7

    # Obtener respuesta del usuario mientras existan letras pendientes
    while len(letras_por_adivinar) > 0 and vidas > 0:
        # Muestra las letras adivinadas y las separa por un espacio
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        # Muestra el estado actual de la palabra que debe adivinar
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas]) # Muestra el estado del ahorcado
        print(f"Palabra: {' '.join(palabra_lista)}") # Muestra las letras adivinadas separadas por un espacio

        # El usuario escoge una letra nueva
        letra_usuario = input('Escoge una letra: ').upper()

        # Si la letra escogida esta en el abecedario y no esta en el conjunto de letras que ya se 
        # han ingresado, se añade la letra al conjunto de letras ingresadas.
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            # Si la letra esta en la palabra, quitar la letra del conjunto de letras pendientes
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            # Si la letra no esta en la palabra, quitar una vida
            else: 
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")

          # Si la letra es repetida 
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")    

        else:
            print("\nEsa letra no es válida")
        
    # El juego llega a esta linea cuando se acaban las vidas del jugador o cuando 
    # se adivinan todas las letras de la palabra.
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste wachin! La palabra era {palabra}")
    
    else:
        print(f"¡Excelente! ¡Adivinaste la palabra {palabra}!")


if __name__ == '__main__':
    ahorcado()



        
        
        



