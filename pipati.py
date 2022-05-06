import random


def jugar():
    usuario = input("Escoge una opción: pi para piedra, pa para papel y ti para tijera.\n").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])

    print(f"La computadora seleccionó: {computadora}")

    if usuario == computadora:
        return '¡Empate!'

    if gano_eljugador(usuario, computadora):
        return '¡Ganaste!'

    return '¡Perdiste!'


def gano_eljugador(jugador, oponente):
    #retorna true si el jugador gana la partida
    # Piedra gana a tijera (pi > ti)
    # Tijera gana a Papel (ti > pa)
    # Papel gana a Piedra (pa > pi)
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())

    
