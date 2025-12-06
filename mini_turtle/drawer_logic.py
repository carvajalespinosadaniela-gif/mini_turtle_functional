# Estado global
posicion_x = 0

def adelante(pasos: int) -> None:
    """
    Mueve la 'tortuga' hacia la derecha y dibuja un tramo horizontal.
    """
    global posicion_x
    if pasos <= 0:
        return

    # Dibujar el tramo horizontal en la posición actual
    linea = " " * posicion_x + "_" * pasos
    print(linea)

    # Actualizar la posición horizontal
    posicion_x += pasos


def abajo(pasos: int) -> None:
    """
    Dibuja un poste vertical en la columna actual.
    """
    global posicion_x
    if pasos <= 0:
        return

    for _ in range(pasos):
        linea = " " * posicion_x + "|"
        print(linea)


def reiniciar() -> None:
    """
    Reinicia la posición horizontal.
    """
    global posicion_x
    posicion_x = 0
