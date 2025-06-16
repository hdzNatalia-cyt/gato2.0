tablero = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]
jugador_actual = "X"
contador_jugadas = 0
juego_activo = True


def mostrar_tablero():
    print("\n-------------")
    for fila in range(3):
        print(f"| {tablero[fila][0]} | {tablero[fila][1]} | {tablero[fila][2]} |")
        print("-------------")

def hacer_jugada(numero_casilla):
    global jugador_actual, contador_jugadas, juego_activo

    if not juego_activo:
        print("¡Juego Terminado! Inicia uno nuevo.")
        return

    fila = (numero_casilla - 1) // 3
    columna = (numero_casilla - 1) % 3

    if tablero[fila][columna] != "X" and tablero[fila][columna] != "O":
        tablero[fila][columna] = jugador_actual
        contador_jugadas += 1

        verificar_final_del_juego()
        if juego_activo:
            if jugador_actual == "X":
                jugador_actual = "O"
            else:
                jugador_actual = "X"
    else:
        print("¡Esa casilla ya está ocupada o no es válida! Elige otra.")

def verificar_final_del_juego():
    global juego_activo

    lineas_ganadoras = [
        [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
    ]

    for linea in lineas_ganadoras:
        (r1, c1), (r2, c2), (r3, c3) = linea
        if (tablero[r1][c1] == jugador_actual and
                tablero[r2][c2] == jugador_actual and
                tablero[r3][c3] == jugador_actual):
            mostrar_tablero()
            print(f"¡GANÓ: {jugador_actual}!")
            juego_activo = False
            return

    if contador_jugadas == 9:
        mostrar_tablero()
        print("¡Es un empate! Nadie ganó.")
        juego_activo = False

def reiniciar_juego():
    global tablero, jugador_actual, contador_jugadas, juego_activo

    tablero = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    jugador_actual = "X"
    contador_jugadas = 0
    juego_activo = True
    print("\n--- ¡Juego Reiniciado! ---")

if __name__ == "__main__":
    while juego_activo:
        mostrar_tablero()
        print(f"Es el turno de {jugador_actual}.")

        try:
            eleccion = int(input("Elige un número de casilla (1-9): "))
            if not (1 <= eleccion <= 9):
                print("Por favor, ingresa un número entre 1 y 9.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
            continue


        hacer_jugada(eleccion)
        if not juego_activo:
            respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower()
            if respuesta == 's':
                reiniciar_juego()
            else:
                print("¡Gracias por jugar! Adiós.")
                break